const router = require("express").Router();

const UserController = require("../controllers/user.controller");
const { userDataValidation } = require("../validations/user.validation");

router.post("/", userDataValidation, UserController.addUser);

module.exports = router;
