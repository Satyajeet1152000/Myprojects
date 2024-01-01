/* eslint-disable consistent-return */
const bcrypt = require('bcrypt');
const { genResponse, StatusCodes } = require('../../../utils');
const db = require('../../../models');

const forgotPasswordUpdate = async (req, res) => {
  const { hashOTP, email } = req.query;
  const { otp, newPassword, confirmPassword } = req.body;

  try {
    const otpMatch = await bcrypt.compare(otp, hashOTP);
    if (!otpMatch) { return res.send(genResponse(StatusCodes.BAD_REQUEST, 'invalid otp')); }
    if (newPassword !== confirmPassword) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'password did not matched')); }

    const password = await bcrypt.hash(confirmPassword, 10);
    try {
      await db.user.update({ password }, { where: { email } });

      return res.send(genResponse(StatusCodes.OK, 'password update successfully'));
    } catch (err) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'error! while updating password')); }
  } catch (err) { res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR)); }
};

module.exports = forgotPasswordUpdate;
