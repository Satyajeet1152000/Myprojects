const db = require('../../../models');
const { genResponse, StatusCodes } = require('../../../utils');

// eslint-disable-next-line consistent-return
const createEvent = async (req, res) => {
  const { createdBy, startDate, endDate } = req.body;
  const { name } = req.body;

  try {
    const event = await db.event.create({
      name, createdBy, startDate, endDate,
    });

    return res.send(genResponse(StatusCodes.OK, 'event created successfully', event));
  } catch (err) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'not able to create event')); }
};

module.exports = createEvent;
