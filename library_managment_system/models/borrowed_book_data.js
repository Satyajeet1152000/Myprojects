const {
  Model, Sequelize,
} = require('sequelize');
const user = require('./user');

module.exports = (sequelize) => {
  class borrowed_book_data extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  borrowed_book_data.init({
    userId: {
      type: Sequelize.INTEGER,
      allowNull: false,
    },
    bookId: {
      type: Sequelize.INTEGER,
      allowNull: false,

    },
    issuedDate: {
      type: Sequelize.DATE,
      allowNull: false,
    },
    dueDate: {
      type: Sequelize.DATE,
      allowNull: false,
    },
    issuedBy: {
      type: Sequelize.INTEGER,
      allowNull: false,

    },
    returnDate: {
      type: Sequelize.DATE,
      allowNull: false,
    },
  }, {
    sequelize,
    modelName: 'borrowed_book_data',
  });
  borrowed_book_data.associate = (models) => {
    borrowed_book_data.belongsTo(
      models.user,
      {
        foreignKey: 'userId',
        targetKey: 'id',
      },
    );
  };

  return borrowed_book_data;
};
