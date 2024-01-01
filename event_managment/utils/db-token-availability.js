const db = require('../models');

module.exports = async (email) => {
  const user = await db.user.findOne({
    where: {
      email,
    },
  });
  if (user) {
    return user.token;
  }
  return false;
};
