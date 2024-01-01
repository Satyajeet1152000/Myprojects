const { Event } = require('../../../models');
const { genResponse, StatusCodes } = require('../../../utils');

// eslint-disable-next-line consistent-return
const list = async (req, res) => {
//   const { email } = req.query;
//   const limit = req.query.limit || 10;
//   const offset = req.query.offset || 0;
//   const sort = req.query.sort || 'ASC';
//   const search = req.query.search || '';
  const result = {};
  try {
    const events = await Event.find();
    //   where: {
    //     createdBy: email,
    //     name: { [Op.like]: `%${search}%` },
    //   },
    //   offset,
    //   limit,
    //   order: [
    //     ['name', sort],
    //   ],
    // });

    // const user = await db.user.findOne({
    //   where: {
    //     email,
    //   },
    // });
    // const invitedIn = await user.getEvents();

    // result.totalCreatedEvents = events.length;
    // result.createdEvents = events;
    // result.totalInvitedInEvents = invitedIn.length;
    // result.invitedIn = invitedIn;
    result.events = events;
    return res.send(genResponse(StatusCodes.OK, 'user event details', result));
  } catch (err) {
    return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR));
  }
};

module.exports = list;
