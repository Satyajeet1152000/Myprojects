const db = require('../../../models');

const book = require('../../../models/book')(db.sequelize);

module.exports = insert_book = async(req, res, next) => {
  try {
    const randNum = Math.floor(Math.random() * 500);
    let randName = 'book'+randNum;
    let randAuthor = 'author'+randNum;


    
    const bk = await book.create({
      name: randName,
      author: randAuthor,
      price: 200,
      totalBook: randNum,
      available: randNum
    });

    return res.json({
      message: "librarian insert_book router",
      name: bk.name,
      author: bk.author
    });
  } catch (err) {
  }
};