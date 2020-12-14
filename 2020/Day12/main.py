import math


def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def calc_coord(action: str, value: int) -> tuple:
    if action == 'N':
        return (0, value)
    elif action == 'S':
        return (0, value * -1)
    elif action == 'E':
        return (value, 0)
    elif action == 'W':
        return (value * -1, 0)


def convert_angle(angle: int) -> int:
    return int(angle / 90)


def part1(instructions):
    coord = [0, 0]
    action_list = ('E', 'S', 'W', 'N')
    last = 'E'

    for i in instructions:
        action = i[0]
        action_ind = action_list.index(last)
        value = int(i[1:])
        x = y = 0

        if action == 'L':
            new_index = (action_ind - convert_angle(value)) % 4
            last = action_list[new_index]
            continue
        if action == 'R':
            # (action_index + angle_calc) % 4
            new_index = (action_ind + convert_angle(value)) % 4
            last = action_list[new_index]
            continue

        if action == 'F':
            (x, y) = calc_coord(last, value)
        else:
            (x, y) = calc_coord(action, value)

        coord[0] += x
        coord[1] += y

    return int(math.fabs(coord[0]) + math.fabs(coord[1]))


def rotate_waypoint(wp: list, units: int) -> list:
    [x, y] = wp

    if units == 0:
        return [x, y]
    elif units == 1 or units == -3:
        return [y, -x]
    elif units == 2 or units == -2:
        return [-x, -y]
    elif units == 3 or units == -1:
        return [-y, x]


def part2(instructions):
    coord = [0, 0]
    waypoint = [10, 1]      # E10, N4

    for i in instructions:
        action = i[0]
        value = int(i[1:])
        rotate = int(value / 90) % 4
        x = y = 0

        if action == 'L':
            waypoint = rotate_waypoint(waypoint, -rotate)
            continue

        if action == 'R':
            waypoint = rotate_waypoint(waypoint, rotate)
            continue

        if action == 'F':
            x += value * waypoint[0]
            y += value * waypoint[1]
        else:
            (wx, wy) = calc_coord(action, value)
            waypoint[0] += wx
            waypoint[1] += wy

        coord[0] += x
        coord[1] += y

    return int(math.fabs(coord[0]) + math.fabs(coord[1]))


if __name__ == "__main__":
    data = get_input('input.txt')

    # Part 1
    print(part1(data))

    # Part 2
    print(part2(data))
