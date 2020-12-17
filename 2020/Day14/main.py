import re
from functools import reduce
from itertools import product


def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def set_bit(value, position):
    return value | (1 << position)


def unset_bit(value, position):
    return value & ~(1 << position)


def part1(data):
    memory = {}
    mask = ''

    for line in data:
        [cmd, value] = line.split(' = ')

        if cmd == 'mask':
            mask = value
        else:
            add_parse = re.search(r'(?:mem\[)(\d+)(?:\])', cmd)
            address = add_parse.group(1)
            val = int(value)
            limit = len(mask) - 1

            for i in range(limit, -1, -1):
                position = limit - i
                if mask[i] == '0':
                    val = unset_bit(val, position)
                elif mask[i] == '1':
                    val = set_bit(val, position)

            memory[address] = val

    return reduce(lambda acc, curr : acc + memory[curr], memory, 0)


def part2(data):
    memory = {}
    mask = ''

    for line in data:
        [cmd, value] = line.split(' = ')

        if cmd == 'mask':
            mask = value
        else:
            add_parse = re.search(r'(?:mem\[)(\d+)(?:\])', cmd)
            address = int(add_parse.group(1))
            val = int(value)
            limit = len(mask) - 1
            floats_pos = []

            for i in range(limit, -1, -1):
                position = limit - i
                if mask[i] == '1':
                    address = set_bit(address, position)
                elif mask[i] == 'X':
                    address = unset_bit(address, position)
                    floats_pos.append(position)

            # Floating bits
            # f_address = []
            bit_fn = [unset_bit, set_bit]
            for b in list(product([0, 1], repeat=len(floats_pos))):
                f_address = address
                for i in range(len(b)):
                    bit = b[i]
                    f_address = bit_fn[bit](f_address, floats_pos[i])
                memory[f_address] = val

    return reduce(lambda acc, curr : acc + memory[curr], memory, 0)



if __name__ == "__main__":
    data = get_input('input.txt')

    # Part 1
    print(part1(data))

    # Part 2
    print(part2(data))