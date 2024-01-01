const {Sequelize, DataTypes} = require('sequelize');
const db = require('./db');

const User = db.define('User', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true
  },
  firstName:{
    type: DataTypes.STRING,
    allowNull: false
  },
  lastName:{
    type: DataTypes.STRING,
    allowNull: false
  }
});


module.exports = User;