const jwt = require('jsonwebtoken');
const { User } = require('../../../models');
const {
  genResponse, StatusCodes,
} = require('../../../utils');

const logout = async (req, res) => {
  try {
    const jwtSecretKey = 'secretKey';
    const userToken = req.header('userToken');
    const tokenVerify = jwt.verify(userToken, jwtSecretKey);

    await User.updateOne({ email: tokenVerify.email }, { token: null });

    return res.send(genResponse(StatusCodes.OK, 'logged out successfully.'));
  } catch (err) {
    return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR));
  }
};

module.exports = logout;
