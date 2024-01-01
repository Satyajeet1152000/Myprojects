const { getReasonPhrase } = require('http-status-codes');

module.exports = (resStatusCode, resMessage, result) => {
  const resResult = result || [];
  const status = `${resStatusCode}, ${getReasonPhrase(resStatusCode)}`;
  return {
    status,
    message: resMessage,
    result: resResult,
  };
};
