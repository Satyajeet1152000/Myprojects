const express = require('express');
const bodyParser = require('body-parser');
const User = require('./user');

//Database connection
const db = require('./db');
db.authenticate().then(() => {
  console.log('Database Connected Successfully.');
}).catch((error) => {
  console.error('Database connection Error: ', error);
});



const app = express();

app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended:false}));

// app.get('/', (req,res)=>{
//   res.sendFile(__dirname + "/" + "index.html");
// });

app.post('/insert', (req,res) => {
  User.create({
    firstName: req.body.firstName,
    lastName:  req.body.lastName
  }).then(()=>{
    console.log("Data inserted successfully");
  }).catch((error)=>{
    console.log("Error while insertion == "+error);
  });
  res.send("Hello " + req.body.firstName + " " + req.body.lastName);
  res.json({
    firstName : req.body.firstName,
    lastName : req.body.lastName   
  });
});

app.post('/check', (req,res) => {
  res.json({message : "Just checking"});
});
const server = app.listen(8081);