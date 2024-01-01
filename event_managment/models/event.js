const {
  Model, Sequelize,
} = require('sequelize');

module.exports = (sequelize) => {
  class event extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate() {
      // define association here
    }
  }
  event.init({
    name: {
      type: Sequelize.STRING,
      allowNull: false,
    },
    createdBy: {
      type: Sequelize.STRING,
      // references: {
      //   model: 'user',
      //   key: 'email',
      // },
    },
    startDate: {
      type: Sequelize.DATE,
      allowNull: false,
    },
    endDate: {
      type: Sequelize.DATE,
      allowNull: false,
    },
  }, {
    sequelize,
    modelName: 'event',
    freezeTableName: true,
  });

  event.associate = (models) => {
    event.belongsToMany(models.user, {
      through: models.userEventData,
    });
  };

  return event;
};
