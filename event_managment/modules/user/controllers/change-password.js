/* eslint-disable consistent-return */
const bcrypt = require('bcrypt');
const { userExistance, genResponse, StatusCodes } = require('../../../utils');
const db = require('../../../models');

const changePassword = async (req, res) => {
  const { email, newPassword, confirmPassword } = req.body;
  try {
    const userExist = await userExistance(email);
    if (!userExist) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'user not found', userExist)); }
    if (newPassword !== confirmPassword) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'password did not matched')); }

    const password = await bcrypt.hash(confirmPassword, 10); // hashing new password
    try {
      await db.user.update({ password }, { where: { email } });
      return res.send(genResponse(StatusCodes.OK, 'password changed successfully', password));
    } catch (err) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'error! while updating password', err)); }
  } catch (err) { res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR), email); }
};

module.exports = changePassword;
