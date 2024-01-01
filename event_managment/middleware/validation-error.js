const { validationResult } = require('express-validator');
const { genResponse, StatusCodes } = require('../utils');

// eslint-disable-next-line consistent-return
const error = (req, res, next) => {
  const errors = validationResult(req);
  // if there is error then return Error
  if (!errors.isEmpty()) {
    return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'validation error', errors.array()));
  }
  next();
};

module.exports = error;
