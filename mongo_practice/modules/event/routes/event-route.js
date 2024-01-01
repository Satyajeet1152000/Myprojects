const router = require('express').Router();
const auth = require('../../../middleware/auth');

const validationError = require('../../../middleware/validation-error');
const eventValidation = require('../../../validation/event-validation');
const {
  createEvent, inviteUser, list, updateEvent, eventDetail,
} = require('../controllers');

router.post('/createEvent', eventValidation.createEvent, validationError, auth, createEvent);
router.get('/list', auth, list);
router.post('/inviteUser', eventValidation.inviteUser, validationError, inviteUser);
// router.patch('/updateEvent', eventValidation.updateEvent, validationError, auth, updateEvent);
// router.get('/eventDetail', auth, eventDetail);

module.exports = router;
