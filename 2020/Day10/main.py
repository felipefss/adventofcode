def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def part1(jolts):
    one_jolts = three_jolts = 0

    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i - 1]
        if 0 < diff < 4:
            if diff == 1:
                one_jolts += 1
            elif diff == 3:
                three_jolts += 1
        else:
            break

    return one_jolts * three_jolts


def is_connected(jolts):
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i - 1]
        if diff < 1 or diff > 3:
            return False

    return True


def part2(data, visited = []):
    arrangements = 0

    # if is_connected(data):
    #     arrangements += 1
    if data[-1] in visited:
        return 0

    for i in range(len(data) - 1, 1, -1):
        if data[i] - data[i-1] < 3:
            temp = [n for n in data[:i] if data[i] - n <= 3]
            size = len(temp)
            if size > 1:
                visited.append(data[i])
                arrangements += size


    return arrangements


if __name__ == "__main__":
    data = get_input('example2.txt')
    jolts = [int(n) for n in data]
    jolts.append(0)
    jolts.sort()
    jolts.append((jolts[-1] + 3))

    # Part 1
    print(part1(jolts))

    # Part 2
    print(part2(jolts))
