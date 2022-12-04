const { convertFileToArray } = require('../readFile');

// 0 = lose
// 1 = draw
// 2 = win

const inputMapping = {
  X: {
    oponent: ['B', 'A', 'C'],
    value: 1
  },
  Y: {
    oponent: ['C', 'B', 'A'],
    value: 2
  },
  Z: {
    oponent: ['A', 'C', 'B'],
    value: 3
  }
};

const pointsMap = [0, 3, 6];

function calculateOutcome(me, oponent) {
  const current = inputMapping[me];
  const pointsIndex = current.oponent.indexOf(oponent);

  return current.value + pointsMap[pointsIndex];
}

const inputArray = convertFileToArray('input.txt');

// Part 1
let total = 0;

inputArray.then(res => {
  res.forEach((item) => {
    const [oponent, me] = item.split(' ');

    total += calculateOutcome(me, oponent);
  });

  console.log(total)
}).catch(error => console.error(error))

// Part 2
// X = lose
// Y = draw
// Z = win
const inputMapping2 = ['A', 'B', 'C'];
total = 0;
inputArray.then(res => {
  const total2 = res.reduce((sum, pair) => {
    const [oponent, action] = pair.split(' ');
    const indexOponent = inputMapping2.indexOf(oponent);
    const outcomeValue = inputMapping[action].value - 2;
    let points = pointsMap[outcomeValue + 1];

    const me = inputMapping2.at(indexOponent + outcomeValue);
    const myIndex = outcomeValue + indexOponent === 3 ? 0 : inputMapping2.indexOf(me);

    points += myIndex + 1;

    // console.log(oponent, action, me, indexOponent, outcomeValue, myIndex, points)
    return sum + points;
  }, 0);
  console.log(total2)
}).catch(error => console.error);