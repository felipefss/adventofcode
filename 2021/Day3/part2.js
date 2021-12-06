const readData = require('../utils/readData');
const commonBits = require('./part1');

readData('input.txt', (data) => {
    let i = 0;
    let diag = [...data];

    // oxygen generator rating
    while (diag.length > 1) {
        const bits = commonBits(diag).map(sum => Number(sum >= 0));

        diag = diag.filter(b => Number(b[i]) == bits[i]);
        i++;
    }

    const oxygenGen = parseInt(diag[0], 2);

    // Reset diagnostic array
    diag = [...data];
    i = 0;

    // CO2 scrubber rating
    while (diag.length > 1) {
        const bits = commonBits(diag).map(sum => Number(sum < 0));

        diag = diag.filter(b => Number(b[i]) == bits[i]);
        i++;
    }

    const co2Scrubber = parseInt(diag[0], 2);

    console.log(oxygenGen * co2Scrubber);
});