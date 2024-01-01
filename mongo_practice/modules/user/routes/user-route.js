/* eslint-disable max-len */
const router = require('express').Router();

const validationError = require('../../../middleware/validation-error');
const userValidation = require('../../../validation/user-validation');
const auth = require('../../../middleware/auth');

// const {
//   register, login, logout, changePassword, forgotPassword, forgotPasswordUpdate,
// } = require('../controllers');
const {
  register, login, logout, changePassword, forgotPassword, forgotPasswordUpdate,
} = require('../controllers');

router.post('/register', userValidation.register, validationError, register);

router.post('/login', userValidation.login, validationError, login);

router.post('/login/logout', auth, logout);

router.patch('/login/changePassword', userValidation.updatePassword, validationError, auth, changePassword);

router.post('/forgotPassword', forgotPassword);
// router.post('/forgotPassword');

router.post('/forgotPassword/update', userValidation.forgotPasswordUpdate, validationError, forgotPasswordUpdate);
// router.post('/forgotPassword/update', userValidation.forgotPasswordUpdate, validationError);

module.exports = router;
