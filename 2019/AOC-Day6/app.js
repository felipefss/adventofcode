const _ = require('lodash');
const fs = require('fs');
const readline = require('readline');
const allObjs = [];
const spaceObjs = {};

function recursiveOrganize() {
    let i = 0;
    while(allObjs.length > 0) {
        const [k, v] = allObjs.shift();
        console.log(i++)
    }
}

const rl = readline.createInterface({
    input: fs.createReadStream('./input.txt')
});

rl.on('line', (input) => {
    const entry = input.split(')');

    if (!allObjs.hasOwnProperty(entry[0])) {
        allObjs[entry[0]] = {};
    }

    if (entry[0] == 'COM') {
        spaceObjs['COM'] = { [entry[1]]: {} };
    } else {
        allObjs.push({ [entry[0]]: [entry[1]] });
    }
});

rl.on('close', () => {
    recursiveOrganize();
})
