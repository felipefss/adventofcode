const { convertFileToArray } = require('../readFile');

convertFileToArray('input.txt').then(res => {
  const stacks = [];

  for (let line of res) {
    if (!line.includes('[')) {
      break;
    }
    let stackNum = 0;
    const numOfStacks = line.match(/(.{3}).?/g).length;

    for (let i = 0; i < line.length; i += 4) {
      const index = stackNum % numOfStacks;
      const crate = line.slice(i, i + 3);

      if (!stacks[index]) {
        stacks[index] = [];
      }

      const parsedCrate = crate.match(/\w/);
      if (parsedCrate) {
        stacks[index].push(parsedCrate[0]);
      }
      stackNum++;
    }
  }

  const instructions = res.slice(res.indexOf('') + 1);

  for (let i of instructions) {
    try {
      const [_, move, from, to] = i.match(/move (\d+) from (\d) to (\d)/);

      for (let moves = 0; moves < move; moves++) {
        stacks[to - 1].unshift(stacks[from - 1].shift())
      }
    } catch (e) {
      console.log(i)
      console.log(stacks)
      throw e;
    }
  }

  console.log(stacks)
  const result = stacks.reduce((acc, stack) => acc + stack[0], '');
  console.log(result)
});