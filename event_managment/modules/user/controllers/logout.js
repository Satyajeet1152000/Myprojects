const db = require('../../../models');
const {
  genResponse, StatusCodes,
} = require('../../../utils');

const logout = async (req, res) => {
  try {
    const { email } = req.body;
    await db.user.update({ token: null }, { where: { email } });

    return res.send(genResponse(StatusCodes.OK, 'logged out successfully.'));
  } catch (err) { return res.send(genResponse(StatusCodes.INTERNAL_SERVER_ERROR)); }
};

module.exports = logout;
