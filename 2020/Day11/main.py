def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def check_adjacent(seats: list, x: int, y: int) -> int:
    occupied = 0
    rows = len(seats)
    cols = len(seats[0])

    for i in range(-1, 2):
        row = x + i
        if 0 <= row < rows:
            for j in range(-1, 2):
                col = y + j

                if row == x and col == y:
                    continue

                if 0 <= col < cols:
                    if seats[row][col] == '#':
                        occupied += 1

    return occupied


def part1(data):
    seats = [[col for col in row] for row in data]
    rows = len(seats)
    cols = len(seats[0])
    occupied = 0
    changes = 0

    while True:
        next_seats = [[y for y in seats[x]] for x in range(rows)]

        for i in range(rows):
            for j in range(cols):
                adjacent = check_adjacent(seats, i, j)
                state = seats[i][j]

                if state == 'L' and adjacent == 0:
                    next_seats[i][j] = '#'
                    occupied += 1
                    changes += 1
                elif state == '#' and adjacent >= 4:
                    next_seats[i][j] = 'L'
                    occupied -= 1
                    changes += 1

        seats = next_seats
        if changes > 0:
            changes = 0
        else:
            break

    return occupied


if __name__ == "__main__":
    data = get_input('input.txt')
    print(part1(data))
