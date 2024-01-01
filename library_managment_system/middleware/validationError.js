const { validationResult } = require("express-validator");

module.exports = error = (req, res, next) => {
  const errors = validationResult(req);

  // if there is error then return Error
  if (!errors.isEmpty()) {
    return res.status(400).json({
      success: false,
      errors: errors.array(),
    }); 
  }
  next();
};