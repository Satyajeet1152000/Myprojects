/* eslint-disable consistent-return */
const jwt = require('jsonwebtoken');
const {
  genResponse, StatusCodes, dbTokenAvailability, userExistance,
} = require('../utils');

const auth = async (req, res, next) => {
  try {
    const jwtSecretKey = 'secretKey';
    const userToken = req.header('userToken');
    if (!userToken) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'authorization failed - userToken not found')); }

    const tokenVerify = jwt.verify(userToken, jwtSecretKey);
    if (!tokenVerify) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'authorization failed - token not valid')); }

    const email = req.body.email || req.query.email || req.body.createdBy || tokenVerify.email;

    const userExist = await userExistance(email);
    if (!userExist) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'authorization failed - user not found.')); }

    const userTokenAvailability = await dbTokenAvailability(email);
    if (userTokenAvailability === null) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'authorization failed - please login')); }
    if (userTokenAvailability !== userToken) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'authorization failed - token does not match')); }
    next();
  } catch (err) {
    return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR, err));
  }
};

module.exports = auth;
