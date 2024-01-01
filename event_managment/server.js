/* eslint-disable no-console */
/* eslint-disable import/no-extraneous-dependencies */
const express = require('express');

// ================= Router Call ====================
const userRoute = require('./modules/user/routes/user-route');
const eventRoute = require('./modules/event/routes/event-route');
// const eventRoute = require('./modules/event/routes/event-route');
//= ================================================

const app = express();
const PORT = 3080;

// =================== Middleware ====================
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// ------------ Routes -------
app.use('/api/user/', userRoute);
app.use('/api/user/', eventRoute);
// ==========================================================

// Database connectioN
const db = require('./models/index');

db.sequelize.authenticate().then(() => {
  console.log('Databae Connected Successfully.');
  // db.sequelize.sync().then(() => {
  //   console.log('DB synced');
  // });

  // Start listening server
  app.listen(PORT, () => {
    console.log('Server listening on port', PORT);
  });
}).catch((err) => {
  console.log(`Sequelize DB Authentication Error : ${err}`);
});
