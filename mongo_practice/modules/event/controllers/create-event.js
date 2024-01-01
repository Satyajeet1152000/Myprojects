/* eslint-disable consistent-return */
const { Event } = require('../../../models');
const { genResponse, StatusCodes } = require('../../../utils');

// eslint-disable-next-line consistent-return
const createEvent = async (req, res) => {
  const { createdBy, startDate, endDate } = req.body;
  let { name } = req.body;

  if (name === 'RandEventData') {
    const randNum = Math.floor(Math.random() * (500 - 1)) + 1;
    name = `event${randNum}`;
  }
  try {
    const result = {};
    result.name = name;
    result.createdBy = createdBy;
    result.startDate = startDate;
    result.endDate = endDate;

    const event = new Event({
      name, createdBy, startDate, endDate,
    });

    await event.save((err) => {
      if (err) {
        return res.send(genResponse(StatusCodes.BAD_REQUEST, err));
      }
    });
    return res.send(genResponse(StatusCodes.OK, 'event created successfully', result));

    // return res.send(genResponse(StatusCodes.OK, 'event created successfully'));
  } catch (err) { return res.send(genResponse(StatusCodes.EXPECTATION_FAILED, 'not able to create event')); }
};

module.exports = createEvent;
