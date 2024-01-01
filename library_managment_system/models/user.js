const {
  Model, Sequelize,
} = require('sequelize');

module.exports = (sequelize) => {
  class user extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  user.init({
    name: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    email: {
      type: Sequelize.STRING,
      allowNull: false,
      unique: true,
      validate: {
        isEmail: true, // check for email format
      },
    },
    password: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    role: {
      type: Sequelize.STRING,
      validate: {
        isIn: [['student', 'librarian']],
      },
    },
    totalBorrowedBook: {
      type: Sequelize.INTEGER,
      validate: {
        max: 3,
      },
    },
    penalty: {
      type: Sequelize.INTEGER,
    },
  }, {
    sequelize,
    modelName: 'user',
    freezeTableName: true,
  });

  user.associate = (models) => {
    user.hasMany(models.borrowed_book_data, {
      foreignKey: 'userId',
      sourceKey: 'id',
    });
  };

  return user;
};
