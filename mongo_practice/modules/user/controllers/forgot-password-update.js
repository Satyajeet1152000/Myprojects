/* eslint-disable consistent-return */
const bcrypt = require('bcrypt');
const { genResponse, StatusCodes } = require('../../../utils');
const { User } = require('../../../models');

const forgotPasswordUpdate = async (req, res) => {
  const { hashOTP, email } = req.query;
  const { otp, newPassword, confirmPassword } = req.body;

  try {
    const otpMatch = await bcrypt.compare(otp, hashOTP);
    if (!otpMatch) { return res.send(genResponse(StatusCodes.BAD_REQUEST, 'invalid otp')); }
    if (newPassword !== confirmPassword) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'password did not matched')); }

    const password = await bcrypt.hash(confirmPassword, 10);
    try {
      const user = await User.updateOne({ email }, { password });
      if (user.acknowledged === true && user.matchedCount === 1) {
        return res.send(genResponse(StatusCodes.OK, 'password update successfully'));
      }
      return res.send(genResponse(StatusCodes.OK, 'password updation failed'));
    } catch (err) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'error! while updating password')); }
  } catch (err) { return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR)); }
};

module.exports = forgotPasswordUpdate;
