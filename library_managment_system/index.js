const express = require('express');

// ================= Router Call ====================
const studentRoute = require('./modules/student/Routes/student.route');
const librarianRoute = require('./modules/librarian/Routes/librarian.route');
//= ================================================

const app = express();
const PORT = 3000;

// =================== Middlewares ====================
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// ------------ Routes -------
app.use('/api/student/', studentRoute);
app.use('/api/librarian/', librarianRoute);
// ==========================================================

// Database connectio
const db = require('./models/index');

db.sequelize.authenticate().then(() => {
  console.log('Databae Connected Successfully.');

  // db.sequelize.sync().then(()=>{
  //   console.log('DB synced');
  // })

  // Start listining server
  app.listen(PORT, () => {
    console.log('Server listening on port', PORT);
  });
}).catch((err) => {
  console.log(`Error : ${err}`);
});
