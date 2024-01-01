const {
  Model, Sequelize,
} = require('sequelize');

module.exports = (sequelize) => {
  class userEventData extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate() {
      // define association here
    }
  }
  userEventData.init({
    userId: {
      type: Sequelize.INTEGER,
      references: {
        model: 'user',
        key: 'email',
      },
    },
    eventId: {
      type: Sequelize.INTEGER,
      references: {
        model: 'event',
        key: 'id',
      },
    },
  }, {
    sequelize,
    modelName: 'userEventData',
    freezeTableName: true,
  });
  return userEventData;
};
