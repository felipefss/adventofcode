const fs = require('fs');
const readline = require('readline');
const spaceObjs = {};

function addEntry(entry, source) {
    const [k, v] = entry;

    if (Object.keys(source).length == 0) {
        source[k] = { [v]: {} };
    } else if (source[k]) {
        source[k][v] = {};
    } else if (source[v]) {
        source[k] = { [v]: JSON.parse(JSON.stringify(source[v])) };
    }

    for (let [key, val] of Object.entries(source)) {

    }
}

const rl = readline.createInterface({
    input: fs.createReadStream('./input.txt')
});

rl.on('line', (input) => {
    const entry = input.split(')');
    const obj = {
        [entry[0]]: entry[1]
    };
});

rl.on('close', () => {
    console.log('finish')
})

const o = {
    d: { i: {}, e: {} }
};
o.c = { d: JSON.parse(JSON.stringify(o.d)) }
delete o.d
o.c.d.e.f = {}
console.log(o.c.d)
