const {Sequelize, DataTypes, Model} = require('sequelize');
const dbConfig = require('./db.config.js');

const db = new Sequelize(
  dbConfig.DBNAME,
  dbConfig.USERNAME,
  dbConfig.PASSWORD,
  {
    host : dbConfig.HOST,
    dialect : dbConfig.DIALECT
  }
);

module.exports = db;

// const User = sequelize.define('User', {
//   id:{
//     type: DataTypes.INTEGER,
//     primaryKey: true,
//     autoIncrement: true
//   },
//   firstName:{
//     type: DataTypes.STRING,
//     allowNull: false
//   },
//   lastName:{
//     type: DataTypes.STRING,
//     allowNull: false
//   }
// });

// User.sync().then(()=>{
//   console.log("User Table created succefully.");
// }).catch((error)=>{
//   console.log("Error while creating table User." + error);
// });

// User.create({
//   firstName: "Satyajeet",
//   lastName: "Singh"
// });