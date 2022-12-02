const fs = require('node:fs');
const readline = require('node:readline');

const fileInput = 'input.txt';

async function processLineByLine() {
  const fileStream = fs.createReadStream(fileInput);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });
  // Note: we use the crlfDelay option to recognize all instances of CR LF
  // ('\r\n') in input.txt as a single line break.

  const elfs = [];
  let sum = 0;

  for await (const line of rl) {
    // Each line in input.txt will be successively available here as `line`.
    if (line === '') {
      elfs.push(sum)
      sum = 0;
    } else {
      sum += Number(line);
    }
  }

  // Part 1
  // console.log(Math.max(...elfs));

  // Part 2
  elfs.sort((a, b) => b - a);
  const totalTop3 = elfs[0] + elfs[1] + elfs[2];
  console.log(totalTop3)
  const totalTop3_2 = elfs.slice(0, 3).reduce((sum, current) => sum + current, 0)
  console.log(totalTop3_2)
}

processLineByLine();