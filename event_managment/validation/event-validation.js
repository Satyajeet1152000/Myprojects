const { body } = require('express-validator');

const createEvent = [
  body('name')
    .exists().withMessage('Name is required')
    .isString()
    .withMessage('Name should be string'),

  body('createdBy')
    .exists().withMessage('createdBy is required'),

  body('startDate')
    .exists().withMessage('Event startDate is required')
    .isDate(),

  body('endDate')
    .exists().withMessage('event endDate is required')
    .isDate(),

];

const inviteUser = [
  body('email')
    .exists(),
  body('eventId')
    .exists(),
  body('invite')
    .exists(),
];

const updateEvent = [
  body('eventId')
    .exists().withMessage('event id is required'),

  body('eventName')
    .exists().withMessage('Name is required')
    .isString()
    .withMessage('Name should be string'),

  body('startDate')
    .exists().withMessage('Event startDate is required')
    .isDate(),

  body('endDate')
    .exists().withMessage('event endDate is required')
    .isDate(),

];

module.exports = {
  createEvent,
  inviteUser,
  updateEvent,
};
