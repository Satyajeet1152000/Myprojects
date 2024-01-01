/* eslint-disable global-require */
module.exports = {
  userExistance: require('./check-user-existance'),
  genResponse: require('./response-genrator'),
  dbTokenAvailability: require('./db-token-availability'),
  StatusCodes: require('http-status-codes').StatusCodes,
  otpGenerator: require('./otp-generator'),
};
