const path = require('path');
const Sequelize = require('sequelize');

const env = process.env.NODE_ENV || 'development';
const sequelizeConfig = require('./src/config/config.json')[env];
const operatorsAliases = require('./schema/sequelize-operators-aliases');
const glob = require('glob');

let sequelize;
if (sequelizeConfig.databaseUrl) {
  sequelize = new Sequelize(sequelizeConfig.databaseUrl, {
    dialect: sequelizeConfig.dialect,
    operatorsAliases,
    logging: false,
    pool: {
      max: 200,
      min: 0,
      acquire: 1200000,
      idle: 10000,
    },
    // Specify options, which are used when sequelize.define is called.
    define: {
      hooks: {
        beforeCount(options) {
          options.raw = true;
        },
      },
      freezeTableName: true,
      timestamps: true,
      underscored: true,
      paranoid: true,
    },
  });
} else {
  sequelize = new Sequelize(
    Object.assign(sequelizeConfig, {
      operatorsAliases,
      logging: false,
      pool: {
        max: 200,
        min: 0,
        acquire: 1200000,
        idle: 10000,
      },
      // Specify options, which are used when sequelize.define is called.
      define: {
        freezeTableName: true,
        timestamps: true,
        underscored: true,
        paranoid: true,
      },
    }),
  );
}

// fs
//   .readdirSync(path.join(__dirname, 'schema/models'))
glob.sync('**/*.model.js')
  .forEach((file) => {
    require(path.join(__dirname, '../', file))(sequelize, Sequelize.DataTypes);
  });

const { models } = sequelize;

Object.keys(models).forEach((key) => {
  if ('associate' in models[key]) {
    models[key].associate(models);
  }
});

const getInstance = () => sequelize;

module.exports = { sequelize, models, getInstance };
