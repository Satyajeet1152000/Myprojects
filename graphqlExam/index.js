/* eslint-disable no-console */
const { ApolloServer } = require('apollo-server');
require('dotenv').config();
const { makeExecutableSchema } = require('graphql-tools');
const { rateLimitDirective } = require('graphql-rate-limit-directive');

const depthLimit = require('graphql-depth-limit');

const { rateLimitDirectiveTypeDefs, rateLimitDirectiveTransformer } = rateLimitDirective();

// const Redis = require('ioredis');
// const Bull = require('bull');

// ============ call merger typeDefs and Resolver Fils ================
const typeDefs = require('./src/graphql/schema');
const resolvers = require('./src/graphql/resolvers');

// ===================== Directives ========================
const { authDirectiveTransformer } = require('./src/graphql/directives');

// const start = async () => {
let schema = makeExecutableSchema({
  typeDefs: [rateLimitDirectiveTypeDefs, typeDefs],
  resolvers,
});
schema = authDirectiveTransformer(schema, 'auth');
schema = rateLimitDirectiveTransformer(schema);

// ----------------------- I O R E D I S -----------------------------------

// const redisClient = new Redis({
//   host: 'redis-15939.c301.ap-south-1-1.ec2.cloud.redislabs.com',
//   port: 15939,
//   password: 'FUeEmr5VfyLuYItG16Qfp68ftZtFdEBt',
// });

// redisClient.on('ready', () => {
//   console.log('redis client is ready.');
// });

// redisClient.on('error', (err) => {
//   console.log('redis is disconnected: ', err);
// });

// redisClient.set('username', 'Satyajeet Singh');

// redisClient.get('username', (err, result) => {
//   console.log(result);
// });

// redisClient.exists('username', (err, result) => {
//   if (result === 1) {
//     console.log('key exists');
//   } else {
//     console.log('key does not exist');
//   }
// });

// ================================ B U L L ========const =======================

// const bullPractice = async () => {
//   const myQueue = new Bull('my-Queue'); // creating new job

//   const job = await myQueue.add({
//     data: 'job 1',
//   });
//   // process job in queue
//   myQueue.process(async (job) => {
//     console.log('==========================================');
//     console.log(`job is processing- ${job.data}`);
//   });
// };
// bullPractice();
// steps
// 1. ws Server

// 2. apollo server
const server = new ApolloServer({
  schema,
  introspection: true,
  playground: false,
  context: ({ req }) => ({
    authToken: req.headers.authorization,
  }),
  validationRules: [
    depthLimit(2),
  // queryCost(100),
  // QueryComplexity({
  //   maximumComplexity: 20,
  //   variables: {},
  //   onComplete: (complexity) => {
  //     console.log(`Query complexity: ${complexity}`);
  //   },
  // }),
  ],
  // plugins: [
  //   {
  //     requestDidStart({ request }) {
  //       console.log(queryCost);
  //       queryCost(schema, request.query, {}, 100)
  //         .then((result) => {
  //           console.log(`Query cost exceeds limit: ${result.cost}`);
  //         });
  //     },
  //   },
  // ],
  // formatError: (error) => {
  // Remove the `extensions` field from the error object
  //   const { extensions, ...rest } = error;
  //   return rest;
  // },
});

// 3. start our server both combined
// await server.start();
// Database connection
const db = require('./src/models/index');

db.sequelize.authenticate().then(() => {
  console.log('📭 Database connected successfully.');
  server.listen().then(({ url }) => {
    console.log(`🚀  Server is running! at ${url}`);
  });
}).catch((err) => {
  console.log(`Database connection error. : ${err}`);
});

// 4. apply middleware like cors bodyparser
// };

// start();
