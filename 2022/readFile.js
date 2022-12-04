const fs = require('node:fs');
const readline = require('node:readline');

async function convertFileToArray(fileInput) {
  const fileStream = fs.createReadStream(fileInput);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });
  // Note: we use the crlfDelay option to recognize all instances of CR LF
  // ('\r\n') in input.txt as a single line break.

  const result = []

  for await (const line of rl) {
    // Each line in input.txt will be successively available here as `line`.
    result.push(line);
  }

  return result;
}

module.exports = {
  convertFileToArray
};