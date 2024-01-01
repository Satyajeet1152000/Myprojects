// eslint-disable-next-line import/no-extraneous-dependencies
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const { genResponse, StatusCodes } = require('../../../utils');
const db = require('../../../models');

// eslint-disable-next-line consistent-return, no-unused-vars
const login = async (req, res) => {
  const jwtSecretKey = 'secretKey';
  try {
    const user = await db.user.findOne({
      where: { email: req.body.email },
      attributes: ['id', 'name', 'email', 'password', 'token'],
    });
    if (!user) { res.send(genResponse(StatusCodes.NOT_FOUND, 'user not found')); }
    /// //...'''

    const passMatch = await bcrypt.compare(req.body.password, user.password);
    if (!passMatch) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'invalid password')); }

    const data = {
      time: Date(),
      email: user.email,
    };
    const token = jwt.sign(data, jwtSecretKey, { expiresIn: '2d' }); // generating jwt token

    // inserting token in user database after successfull login.
    await db.user.update({ token }, { where: { email: req.body.email } });
    user.token = token;

    return res.send(genResponse(StatusCodes.OK, 'user login success.', user));
  } catch (err) {
    return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR));
  }
};

module.exports = login;
