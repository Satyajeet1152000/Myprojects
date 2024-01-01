const { body } = require('express-validator');

const register = [
  body('name')
    .exists().withMessage('Name is required')
    .isString()
    .withMessage('Name should be string'),

  body('email')
    .exists().withMessage('Email is required')
    .isEmail()
    .withMessage('Provide valid email'),

  body('password')
    .exists().withMessage('Password is required')
    .isString()
    .withMessage('Password should be string')
    .isLength({ min: 5 })
    .withMessage('Password should be at least 5 characters'),

];

const login = [
  body('email')
    .exists().withMessage('Password is required')
    .isEmail()
    .withMessage('Provide valid email'),

  body('password')
    .exists().withMessage('Password is required')
    .isString()
    .withMessage('Password should be string')
    .isLength({ min: 5 })
    .withMessage('Password should be at least 5 characters'),
];

const updatePassword = [
  body('email')
    .exists().withMessage('Email is required')
    .isEmail()
    .withMessage('Provide valid email'),

  body('newPassword')
    .exists().withMessage('Password is required')
    .isString()
    .withMessage('Password should be string')
    .isLength({ min: 5 })
    .withMessage('Password should be at least 5 characters'),

  body('confirmPassword')
    .exists().withMessage('Password is required')
    .isString()
    .withMessage('Password should be string')
    .isLength({ min: 5 })
    .withMessage('Password should be at least 5 characters'),
];

const forgotPassword = [
  body('email')
    .exists().withMessage('Email is required')
    .isEmail()
    .withMessage('Provide valid email'),
];

const forgotPasswordUpdate = [
  body('otp')
    .exists().withMessage('otp is required'),

  body('newPassword')
    .exists().withMessage('Password is required')
    .isString()
    .withMessage('Password should be string')
    .isLength({ min: 5 })
    .withMessage('Password should be at least 5 characters'),

  body('confirmPassword')
    .exists().withMessage('Password is required')
    .isString()
    .withMessage('Password should be string')
    .isLength({ min: 5 })
    .withMessage('Password should be at least 5 characters'),
];

const cancleInvitation = [
];

module.exports = {
  login,
  register,
  updatePassword,
  forgotPassword,
  cancleInvitation,
  forgotPasswordUpdate,
};
