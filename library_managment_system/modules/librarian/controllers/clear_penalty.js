module.exports = clear_penalty = (req, res, next) => {
  try {
    return res.json({
      message: "librarian clear_penalty router"
    });
  } catch (err) {
    console.log("controller catch part");
  }
};