const db= require('../../../models');

const jwt = require('jsonwebtoken');

module.exports = display_books = async (req, res, next) => {
  try {

    const books = await db.book.findAll({
      attributes:['id', 'name', 'available']
    });

    const token = req.header('userToken');
    const jwtSecretKey = 'secretKey';

    try{
      const varified = jwt.verify(token, jwtSecretKey);

      if(varified){
        console.log("Token vrified");
      }
      else{
        console.log('token not avialable');
      }
    }
    catch(err){
      console.log('header section error.');
    }


    
    return res.json({
      message: "librarian display_books router",
      data: books,
    });

  } catch (err) {
    console.log(err);
  }
};