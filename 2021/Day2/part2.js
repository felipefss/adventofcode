const readData = require('../utils/readData');

readData('input.txt', (data) => {
    let horizontal = 0;
    let depth = 0;
    let aim = 0;

    data.map(dir => dir.split(' ')).forEach(dir => {
        switch (dir[0]) {
            case 'forward':
                horizontal += Number(dir[1]);
                depth += aim * Number(dir[1]);
                break;
            case 'up':
                aim -= Number(dir[1]);
                break;
            case 'down':
                aim += Number(dir[1]);
                break;
        }
    });

    console.log(horizontal * depth);
});