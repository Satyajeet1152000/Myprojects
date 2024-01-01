/* eslint-disable no-use-before-define */
const userInfo = document.getElementById('userInfo');

const userEmail = prompt('Enter Username or Email.');
const userPass = prompt('Enter password.');

queryFetch(`
  mutation Login($input: LoginInput) {
    login(input: $input) {
      id
      name
      username
      email
      balance
      token
    }
  }
`, {
  input: {
    emailOrUsername: userEmail,
    password: userPass,
  },
}).then((data) => {
  // user.innerText = data.errors;
  const {
    name, username, email, balance, token,
  } = data.data.login;
  userInfo.innerHTML = '';

  userInfo.append(outputGenerator('Name', name));
  userInfo.append(outputGenerator('Username', username));
  userInfo.append(outputGenerator('Email', email));
  userInfo.append(outputGenerator('Balance', balance));
  userInfo.append(outputGenerator('Token', token));
  // console.log(data.data.login);
});

function outputGenerator(fieldname, value) {
  const element = document.createElement('div');
  element.innerHTML = `${fieldname.bold()} : ${value}`;
  return element;
}

function queryFetch(query, variables) {
  return fetch('http://localhost:4000/', {
    method: 'POST',
    headers: { 'Content-type': 'application/json' },
    body: JSON.stringify({
      query,
      variables,
    }),
  }).then((res) => res.json());
}
