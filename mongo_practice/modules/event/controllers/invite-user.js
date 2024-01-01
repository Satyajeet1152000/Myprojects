/* eslint-disable consistent-return */
const { Event, User } = require('../../../models');
const { genResponse, StatusCodes, userExistance } = require('../../../utils');

const inviteUser = async (req, res) => {
  try {
    const { email, eventId, invite } = req.body;
    let event;

    try {
      event = await Event.findOne({ _id: eventId });
    } catch (err) {
      return res.send(genResponse(StatusCodes.NOT_FOUND, 'invalid event id'));
    }

    if (!event) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'event not found')); }
    if (event.createdBy !== email) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'You are not event creator')); }

    const inviteUserExist = await userExistance(invite);
    if (!inviteUserExist) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'Invited user not found.')); }
    if (email === invite) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'not allowed to invite self')); }

    const eventUpdate = await Event.findByIdAndUpdate({ eventId }, inviteUsers.push(inviteUserExist._id));
    // if (user && event) {
    //   await event.addUser(user); // add user using association
    return res.send(genResponse(StatusCodes.OK, 'user invited successfully'));
    // }
  } catch (err) {
    console.log(err);
    return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR, err));
  }
};

module.exports = inviteUser;
