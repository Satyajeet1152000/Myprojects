const {
  Model, Sequelize,
} = require('sequelize');

module.exports = (sequelize) => {
  class book extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  book.init({
    name: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    author: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    price: {
      type: Sequelize.INTEGER,
      allowNull: false,
    },
    totalBook: {
      type: Sequelize.INTEGER,
      allowNull: false,
    },
    available: {
      type: Sequelize.INTEGER,
      allowNull: false,
    },
  }, {
    sequelize,
    modelName: 'book',
    freezeTableName: true,
  });

  // book.associate = (models) => {
  //   book.belongsToMany(models.user, {
  //     through: models.borrowed_book_data,
  //     // foreignKey: 'user_id'
  //   });
  // };

  return book;
};
