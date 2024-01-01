/* eslint-disable consistent-return */
const db = require('../../../models');
const { genResponse, StatusCodes, userExistance } = require('../../../utils');

const inviteUser = async (req, res) => {
  try {
    const { email, eventId, invite } = req.body;

    // only allow event creator to invite user to event
    const event = await db.event.findOne({ where: { id: eventId } });
    if (event.createdBy !== email) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'You are not event creator')); }

    const inviteUserExist = await userExistance(invite);
    if (!inviteUserExist) { return res.send(genResponse(StatusCodes.NOT_FOUND, 'Invited user not found.')); }
    if (email === invite) { return res.send(genResponse(StatusCodes.UNAUTHORIZED, 'not allowed to invite self')); }

    const user = await db.user.findOne({ where: { email: invite } });
    if (user && event) {
      await event.addUser(user); // add user using association
      return res.send(genResponse(StatusCodes.OK, 'user invited successfully'));
    }
  } catch (err) { return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR)); }
};

module.exports = inviteUser;
