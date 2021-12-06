const readData = require('../utils/readData');

function commonBits(data) {
    const commonBits = [];

    data.forEach(bin => {
        Array.from(bin, (b, i) => {
            if (!commonBits[i]) {
                commonBits[i] = 0;
            }

            commonBits[i] += b == '1' ? 1 : -1;
        })
    });

    return commonBits;
};

module.exports = commonBits;

readData('input.txt', (data) => {
    const bits = commonBits(data);

    const gamma = bits.map(sum => sum > 0 ? 1 : 0).join('');
    const epsilon = bits.map(sum => sum < 0 ? 1 : 0).join('');

    // console.log(parseInt(gamma, 2) * parseInt(epsilon, 2));
});