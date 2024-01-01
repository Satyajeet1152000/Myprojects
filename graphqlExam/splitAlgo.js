/* eslint-disable no-param-reassign */
/* eslint-disable no-console */
const groupExpense = 210;
const totalGroupMembers = 7;
// const contributions = [100, 110, 0, 0, 0, 0, 0];

const contributionsData = [
  { userId: 'user1', amount: '100' },
  { userId: 'user2', amount: '110' },
  { userId: 'user3', amount: '0' },
  { userId: 'user4', amount: '0' },
  { userId: 'user5', amount: '0' },
  { userId: 'user6', amount: '0' },
  { userId: 'user7', amount: '0' },
];

let contributions = [];
contributions = contributionsData.map((contribution) => parseFloat(contribution.amount));

const avgPay = groupExpense / totalGroupMembers;

// find maxPayer
function getMaxPayer(arr) {
  let maxInd = 0;
  for (let i = 1; i < totalGroupMembers; i += 1) {
    if (arr[i] > arr[maxInd]) maxInd = i;
  }
  return maxInd;
}

// find minPayer
function getMinPayer(arr) {
  let minInd = 0;
  for (let i = 1; i < totalGroupMembers; i += 1) {
    if (arr[i] < arr[minInd]) minInd = i;
  }
  return minInd;
}

function splitPayment(arr) {
  for (let i = 0; i < totalGroupMembers; i += 1) {
    const maxPayer = getMaxPayer(arr);
    const minPayer = getMinPayer(arr);

    if (maxPayer === 0 && minPayer === 0) { break; }

    const maxCanPay = arr[maxPayer] - avgPay;
    const maxCanTake = arr[minPayer] - avgPay;

    const transactionAmount = Math.min(Math.abs(maxCanPay), Math.abs(maxCanTake));

    arr[maxPayer] -= transactionAmount;
    arr[minPayer] += transactionAmount;

    console.log(`   paid ${minPayer} -> ${maxPayer}  == ${transactionAmount}`);
  }
}

// check paymets have to equal to group expense
function totalContributions(arr) {
  let sum = 0;
  for (let i = 0; i < totalGroupMembers; i += 1) {
    if (arr[i] < 0) { return 0; }
    sum += arr[i];
  }
  return sum;
}

if (totalContributions(contributions) === groupExpense) {
  console.log(`maximum payment= ${contributions[getMaxPayer(contributions)]}`);
  console.log(`amount have to pay by each user is => ${avgPay}`);
  console.log('----------------------------------------');
  splitPayment(contributions);
} else {
  console.log(contributions);
  console.log('invalid contributions');
}
