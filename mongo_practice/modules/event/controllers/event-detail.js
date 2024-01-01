const db = require('../../../models');
const { genResponse, StatusCodes } = require('../../../utils');

const eventDetail = async (req, res) => {
  try {
    const { eventId } = req.query;
    const event = await db.event.findOne({ where: { id: eventId }, attributes: ['id', 'name', 'createdBy', 'startDate', 'endDate'/*  */] });
    if (!event) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'event not found')); }

    const result = {};
    result.event = event;

    const invitedUsers = await event.getUsers({
      attributes: ['id', 'name', 'email'],
    });

    result.invitedUsers = invitedUsers;

    return res.send(genResponse(StatusCodes.OK, 'event found', result));
  } catch (err) {
    return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR));
  }
};

module.exports = eventDetail;
