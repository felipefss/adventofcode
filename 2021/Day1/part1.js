const fs = require('fs');

module.exports = (arr) => {
    return arr.reduce((sum, n, i, arr) => Number(n) > Number(arr[i - 1]) ? sum + 1 : sum, 0);
};

fs.readFile('input.txt', (err, data) => {
    if (err) {
        throw err;
    }

    const measurements = data.toString().split('\n')
    //console.log(measurements);
});