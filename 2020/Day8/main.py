import re

def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def parse_inst(instruction):
    parsed = instruction.split(' ')
    return parsed[0], int(parsed[1])


def part1(data):
    acc = 0
    instructions = {}
    i = 0

    while i < len(data):
        oper, arg = parse_inst(data[i])

        # Save current instruction index
        # to return acc value before it's run a second time
        if i not in instructions:
            instructions[i] = True
        else:
            return acc

        if oper == 'nop':
            pass
        elif oper == 'acc':
            acc += arg
        elif oper == 'jmp':
            i += arg
            continue

        i += 1


def run_error_program(data):
    acc = 0
    instructions = []
    i = 0

    while i < len(data):
        oper, arg = parse_inst(data[i])

        # Save current instruction index
        # to return acc value before it's run a second time
        if i not in instructions:
            instructions.append(i)
        else:
            return instructions, True

        if oper == 'nop':
            pass
        elif oper == 'acc':
            acc += arg
        elif oper == 'jmp':
            i += arg
            continue

        i += 1

    return acc, False


def part2(data):
    inst_list = data.copy()
    ret_val, error = run_error_program(inst_list)
    i = len(ret_val)
    subs = {
        'jmp': 'nop',
        'nop': 'jmp'
    }

    while i >= 0 and error:
        i -= 1
        err_ind = ret_val[i]
        instruction = inst_list[err_ind]

        rgx = re.search(r'(\w{3})', instruction)
        if rgx and rgx[1] in subs:
            inst_list[err_ind] = instruction.replace(rgx[1], subs[rgx[1]])
            ret_val, error = run_error_program(inst_list)
            inst_list = data.copy()

    return ret_val

if __name__ == "__main__":
    data = get_input('input.txt')

    # Part 1
    print(part1(data))

    # Part 2
    print(part2(data))