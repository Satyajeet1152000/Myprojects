const express = require('express');
const bocyParser = require('body-parser');
const graphHttp = require('express-graphql');

const app = express();

app.use(bocyParser.json());

app.get('/graphql', graphHttp({
  schema: null,
  route: {},
}));
app.listen(3000);
