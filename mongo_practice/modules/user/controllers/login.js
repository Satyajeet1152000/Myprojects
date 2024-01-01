// eslint-disable-next-line import/no-extraneous-dependencies
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const { genResponse, StatusCodes } = require('../../../utils');
const { User } = require('../../../models');

// eslint-disable-next-line consistent-return, no-unused-vars
const login = async (req, res) => {
  const jwtSecretKey = 'secretKey';
  const result = {};
  try {
    let user = await User.find({ email: req.body.email });
    if (!user) { res.send(genResponse(StatusCodes.NOT_FOUND, 'user not found')); }

    result.name = user[0].name;
    result.email = user[0].email;

    const passMatch = await bcrypt.compare(req.body.password, user[0].password);
    if (!passMatch) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'invalid password')); }

    const data = {
      time: Date(),
      email: user[0].email,
    };
    const token = jwt.sign(data, jwtSecretKey); // generating jwt token

    // insert token in user database after successfull login.
    user = await User.updateOne({ email: req.body.email }, { token });
    if (user.acknowledged === true && user.matchedCount === 1) {
      result.token = token;
      return res.send(genResponse(StatusCodes.OK, 'user login success.', result));
    }
    return res.send(genResponse(StatusCodes.BAD_REQUEST, 'user login failed.'));

    // await db.user.update({ token }, { where: { email: req.body.email } });
    // user.token = token;
  } catch (err) {
    return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR));
  }
};

module.exports = login;
