const jwt = require('jsonwebtoken');
const db = require('../../../models');
const { genResponse, StatusCodes } = require('../../../utils');

const updateEvent = async (req, res) => {
  try {
    const {
      eventId, eventName, startDate, endDate,
    } = req.body;

    // fetch email from jwt token
    const jwtSecretKey = 'secretKey';
    const userToken = req.header('userToken');
    const { email } = await jwt.verify(userToken, jwtSecretKey);

    const event = await db.event.findOne({ where: { createdBy: email, id: eventId } });
    if (!event) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'event not found')); }

    const update = await db.event.update({ name: eventName, startDate, endDate }, {
      where: { id: eventId },
    });

    if (!update) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'not able to update event')); }
    return res.send(genResponse(StatusCodes.OK, 'event updated successfully'));
  } catch (err) { return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR)); }
};

module.exports = updateEvent;
