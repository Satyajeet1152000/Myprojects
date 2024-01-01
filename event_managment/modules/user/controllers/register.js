/* eslint-disable consistent-return */
const bcrypt = require('bcrypt');
const { genResponse, userExistance, StatusCodes } = require('../../../utils');
const db = require('../../../models');

const register = async (req, res) => {
  const { name, email, password } = req.body;

  const hashPassword = await bcrypt.hash(password, 10);

  const userExist = await userExistance(email);
  if (userExist) {
    return res.send(genResponse(StatusCodes.BAD_REQUEST, 'user already exist'));
  }

  try {
    const user = await db.user.create({ name, email, password: hashPassword });
    return res.send(genResponse(StatusCodes.OK, 'user created succesfully', user));
  } catch (err) {
    res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR));
  }
};

module.exports = register;
