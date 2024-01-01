/* eslint-disable linebreak-style */
module.exports = class jwtUtil {
  constructor(token) {
    this.token = token;
  }

  showPrice() {
    console.log(`Price of ${this.token}`);
  }
};
// module.exports = jwtUtil;
