def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def part1(data):
    depart_at = int(data[0])
    bus_ids = [int(b) for b in data[1].split(',') if b != 'x']
    i = depart_at
    available = []

    while len(available) == 0:
        available = list(filter(lambda b: i % b == 0, bus_ids))
        i += 1

    return (i - 1 - depart_at) * available[0]


def part2(data):
    bus_ids = [int(b) if b != 'x' else b for b in data[1].split(',')]
    size = len(bus_ids)
    current = bus_ids[0]

    


if __name__ == "__main__":
    data = get_input('example.txt')

    # Part 1
    print(part1(data))

    # Part 2
    print(part2(data))
