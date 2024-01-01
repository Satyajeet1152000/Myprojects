/* eslint-disable no-console */
/* eslint-disable import/no-extraneous-dependencies */
const { ApolloServer } = require('apollo-server');
const { mergeTypeDefs, mergeResolvers } = require('@graphql-tools/merge');
const { mapSchema, getDirective, MapperKind } = require('@graphql-tools/utils');
require('dotenv').config();
const { makeExecutableSchema } = require('graphql-tools');

// Subscription Server
// ----------------------------------------------
const express = require('express');
const { createServer } = require('http');
const { ApolloServerPluginDrainHttpServer } = require('@apollo/server/plugin/drainHttpServer');
const { expressMiddleware } = require('@apollo/server/express4');
const cors = require('cors');
const bodyparser = require('body-parser');

const { WebSocketServer } = require('ws');
const { useServer } = require('graphql-ws/lib/use/ws');

const httpServer = createServer(express());

// ----------------------- U S E R  -----------------
const { userQueries, userMutations, userSubscription } = require('./src/schema');
const { userQueryResolver, userMutationResolver } = require('./src/resolvers');

const typeDefs = mergeTypeDefs([userQueries, userMutations, userSubscription]);
const resolvers = mergeResolvers([userQueryResolver,
  userMutationResolver,
  // userSubscriptionResolver
]);

const tokens = ['dummyToken1', 'dummyToken2'];
const isAuthenticated = (token) => tokens.includes(token);

const authDirectiveTransformer = (schema, directiveName) => mapSchema(schema, {
  [MapperKind.OBJECT_FIELD]: (fieldConfig) => {
    const authDirective = getDirective(schema, fieldConfig, directiveName);

    if (authDirective) {
      const { resolve } = fieldConfig;

      fieldConfig.resolve = async (parent, args, context, info) => {
        const { authToken } = context;
        if (!isAuthenticated(authToken)) {
          throw new Error('you are not authenticated.');
        }

        const result = await resolve(parent, args, context, info);
        return result;
      };
    }
  },
});

let schema = makeExecutableSchema({
  typeDefs,
  resolvers,
});
schema = authDirectiveTransformer(schema, 'auth');

// Creating the WebSocket server

// Hand in the schema we just created and have the
// WebSocketServer start listening.

// Database connection
// const db = require('./src/models/index');

// db.sequelize.authenticate().then(() => {
//   console.log('📭 Database connected successfully.');
//   server.listen().then(({ url, subscriptionUrl }) => {
//     console.log(`🚀  Server is running! at ${url}`);
//     console.log(`🚀  Server is running! at ${subscriptionUrl}`);
//   });
// }).catch((err) => {
//   console.log(`Database connection error. : ${err}`);
// });

// steps
// 1. ws Server
const wsServer = new WebSocketServer({
  server: httpServer, // This is the `httpServer` we created in a previous step.
  path: '/graphql',
});
const serverCleanup = useServer({ schema }, wsServer);

// 2. apollo server
const server = new ApolloServer({
  schema,
  context: ({ req }) => ({
    authToken: req.headers.authorization,
  }),
  plugins: [
    ApolloServerPluginDrainHttpServer({ httpServer }), // Proper shutdown for the HTTP server.
    // Proper shutdown for the WebSocket server.
    {
      async serverWillStart() {
        return {
          async drainServer() {
            await serverCleanup.dispose();
          },
        };
      },
    },
  ],
  // formatError: (error) => {
  //   const { extensions, ...rest } = error; // Remove the `extensions` field from the error object
  //   return rest;
  // },
});

// 3. start our server both combined
await server.start();

// 4. apply middleware like cors bodyparser
app.use('/graphql');
