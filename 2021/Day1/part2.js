const {
    createReadStream
} = require('fs');
const readline = require('readline');
const sum = require('./part1');

const rl = readline.createInterface({
    input: createReadStream('input.txt')
});

const data = [];

rl.on('line', (line) => {
    data.push(Number(line));
});

rl.on('close', () => {
    const sums = [];

    for (let i = 0; i < data.length - 2; i++) {
        sums.push(Number(data[i]) + Number(data[i + 1]) + Number(data[i + 2]));
    }

    console.log(sum(sums));
});