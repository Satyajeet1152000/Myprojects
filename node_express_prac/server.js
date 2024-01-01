const bodyParser = require('body-parser');
let { response } = require('express');
const express = require('express');
const multer = require('multer');




// const urlencodedParser = bodyParser.urlencoded({extended:false});


const app = express();


app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended:false}));

app.get('/index.html', (req, res) => {
  res.sendFile(__dirname + "/" + "index.html");

});

app.post('/process_get', (req,res) => {
  // response = {
  //   first_name : req.query.first_name,
  //   last_name : req.query.last_name 
  // };

  // console.log(response);

  // res.end(JSON.stringify(response));
  res.send('<P> Hello ' + req.body.first_name + ' ' + req.body.last_name + '</p>');

});


const server = app.listen(8080);