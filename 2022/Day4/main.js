const { convertFileToArray } = require('../readFile');

const FILE = 'input.txt'

convertFileToArray(FILE).then(res => {
  let fullyContained = 0;
  let overlap = 0;

  res.forEach(elves => {
    // Part 1
    const [elf1, elf2] = elves.split(',').map(str => str.split('-').map(Number));

    if (
      (elf1[0] >= elf2[0] && elf1[1] <= elf2[1]) ||
      (elf2[0] >= elf1[0] && elf2[1] <= elf1[1])
    ) {
      fullyContained++;
    }

    // Part 2
    if (
      (elf1[0] >= elf2[0] && elf1[0] <= elf2[1]) ||
      (elf1[1] >= elf2[0] && elf1[1] <= elf2[1]) ||
      (elf2[0] >= elf1[0] && elf2[0] <= elf1[1]) ||
      (elf2[1] >= elf1[0] && elf2[1] <= elf1[1])
    ) {
      overlap++;
    }
  });
  console.log(fullyContained)
  console.log(overlap)

});