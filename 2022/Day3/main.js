const { convertFileToArray } = require('../readFile');

const FILE = 'input.txt'

// Part 1
convertFileToArray(FILE).then(res => {
  let prioritiesSum = 0;

  res.forEach(items => {
    const half = items.length / 2;
    const first = Array.from(items.slice(0, half));
    const second = items.slice(half);

    const dups = [];
    first.forEach(item => {
      if (second.includes(item) && !dups.includes(item)) {
        dups.push(item);
      }
    });

    // a charCode - 96
    // A charCode - 38
    let charCode = 96;
    if (dups[0].search(/[A-Z]/) !== -1) {
      charCode = 38;
    }

    prioritiesSum += dups[0].charCodeAt() - charCode;
  });

  console.log(prioritiesSum);

  // Part 2
  prioritiesSum = 0;
  for (let i = 0; i < res.length; i += 3) {
    const [elf1, elf2, elf3] = res.slice(i, i + 3);

    const dups = [];
    Array.from(elf1).forEach(item => {
      if (elf2.includes(item) && elf3.includes(item) && !dups.includes(item)) {
        dups.push(item);
      }
    });

    let charCode = 96;
    if (dups[0].search(/[A-Z]/) !== -1) {
      charCode = 38;
    }

    prioritiesSum += dups[0].charCodeAt() - charCode;
  }
  console.log(prioritiesSum)

});