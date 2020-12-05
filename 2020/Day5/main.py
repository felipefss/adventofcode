import math

seats = []

with open('input.txt', 'r') as file:
    line = file.readline()

    while line:
        seats.append(line.replace('\n', ''))
        line = file.readline()


def decode_seat(chars, top: int) -> int:
    min_range = 0
    max_range = top

    for r in chars:
        combi = max_range + min_range
        if r == 'F' or r == 'L':
            max_range = int(math.floor(combi / 2))
        elif r == 'B' or r == 'R':
            min_range = int(math.ceil(combi / 2))
    return max_range


def get_seat_id(seat_code):
    rows = seat_code[:7]
    cols = seat_code[-3:]
    row = decode_seat(rows, 127)
    col = decode_seat(cols, 7)

    return row * 8 + col


def part1():
    max_id = 0

    for s in seats:
        seat_id = get_seat_id(s)

        if seat_id > max_id:
            max_id = seat_id

    return max_id


def part2():
    seat_ids = []

    for s in seats:
        seat_ids.append(get_seat_id(s))

    seat_ids.sort()

    for i in range(1, len(seat_ids)):
        if seat_ids[i] - seat_ids[i - 1] == 2:
            return seat_ids[i] - 1

    return 0


if __name__ == "__main__":
    # Part 1
    print(part1())

    # Part 2
    print(part2())
