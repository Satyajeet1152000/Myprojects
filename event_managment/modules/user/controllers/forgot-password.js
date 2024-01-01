// const db = require('../../../models');
const bcrypt = require('bcrypt');
const {
  genResponse, StatusCodes, userExistance, otpGenerator,
} = require('../../../utils');

const forgotPassword = async (req, res) => {
  const { email } = req.body;
  const result = {};

  const userExist = await userExistance(email);
  if (!userExist) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'invalid email', userExist)); }

  const otp = otpGenerator();
  const hashOTP = await bcrypt.hash(otp, 10);

  const redirectURL = `http://localhost:3080/api/user/forgotPassword/update?hashOTP=${hashOTP}&email=${email}`;
  result.redirectURL = redirectURL;
  result.includeParams = { otp: '', newPassword: '', confirmPassword: '' };

  return res.send(genResponse(StatusCodes.OK, `your OTP is ${otp}`, result));
};

module.exports = forgotPassword;
