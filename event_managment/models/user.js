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
    static associate() {
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
    token: {
      type: Sequelize.STRING,
      allowNull: true,
    },
  }, {
    sequelize,
    modelName: 'user',
    freezeTableName: true,
  });

  user.associate = (models) => {
    user.belongsToMany(models.event, {
      through: models.userEventData,
    });
  };

  // user.associate = (models) => {
  //   user.hasMany(models.event, {
  //     foreignKey: 'createdBy',
  //     sourceKey: 'email',
  //   });
  // };

  return user;
};
