const {
    createReadStream
} = require('fs');
const readline = require('readline');

module.exports = function (file, callback) {
    const rl = readline.createInterface({
        input: createReadStream(file)
    });

    const data = [];

    rl.on('line', (line) => {
        data.push(line);
    });

    rl.on('close', () => {
        callback(data);
    });
};