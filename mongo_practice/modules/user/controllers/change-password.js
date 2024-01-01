/* eslint-disable consistent-return */
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { genResponse, StatusCodes } = require('../../../utils');
const { User } = require('../../../models');

const changePassword = async (req, res) => {
  const { email, newPassword, confirmPassword } = req.body;
  try {
    const jwtSecretKey = 'secretKey';
    const userToken = req.header('userToken');
    const tokenVerify = jwt.verify(userToken, jwtSecretKey);

    if (newPassword !== confirmPassword) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'password did not matched')); }

    const password = await bcrypt.hash(confirmPassword, 10); // hashing new password
    try {
      const user = await User.updateOne({ email: tokenVerify.email }, { password });
      if (user.acknowledged === true && user.matchedCount === 1) {
        return res.send(genResponse(StatusCodes.OK, 'password changed successfully'));
      }
      return res.send(genResponse(StatusCodes.BAD_REQUEST, 'password not updated'));
    } catch (err) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'error! while updating password', err)); }
  } catch (err) { res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR), email); }
};

module.exports = changePassword;
