const loginService = require('../Services/login');

module.exports = login = async (req, res) => {
  const user = await loginService(req.body.email, req.body.password);  
  // const user = await loginService('satyajeet@gmail.com','2324xcdc');  

  try {    
    return res.json({
      message: "librarian login router",
      name: user.name,
      email: user.email,
      token: user.token
    });
  } catch (err) {
    res.json({
      error: err,
      user: 'not found'
    });
  }
};