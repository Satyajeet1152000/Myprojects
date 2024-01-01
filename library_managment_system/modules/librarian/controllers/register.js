const registerService = require('../Services/register');

module.exports = register = async(req, res, next) => {
  const user = await registerService();

  try {
    return res.json({
      message: "librarian register router",
      name: user.name,
      email: user.email
    });
  } catch (err) {
    res.json({
      error: err,
      user: 'not able to register.'
    });
  }
};