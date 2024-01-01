/* eslint-disable consistent-return */
const bcrypt = require('bcrypt');
// const { genResponse, userExistance, StatusCodes } = require('../../../utils');
const { genResponse, StatusCodes } = require('../../../utils');
const { User } = require('../../../models');

const register = async (req, res) => {
  let { name, email, password } = req.body;

  if (name === 'RandUserData') {
    const randNum = Math.floor(Math.random() * (500 - 1)) + 1;
    name = `user${randNum}`;
    email = `${name}@gmail.com`;
    password = '2324xcdc';
  }
  const hashPassword = await bcrypt.hash(password, 10);

  try {
    const result = {};
    result.name = name;
    result.email = email;
    result.password = hashPassword;
    const user = new User({ name, email, password: hashPassword });
    await user.save((err) => {
      if (err) {
        return res.send(genResponse(StatusCodes.BAD_REQUEST, err));
      }
    });
    return res.send(genResponse(StatusCodes.OK, 'user created succesfully', user, result));
  } catch (err) {
    res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR));
  }
};

module.exports = register;
