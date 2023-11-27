with open("input.txt") as file:
    parsed_lines = ""

    for line in file:
        parsed_lines = parsed_lines + line.strip()


# Part 1
def part1():
    points = {(0, 0)}
    current_x = 0
    current_y = 0

    for dir in parsed_lines:
        match dir:
            case "^":
                current_y += 1
            case "v":
                current_y -= 1
            case ">":
                current_x += 1
            case "<":
                current_x -= 1

        points.add((current_x, current_y))

    print(len(points))


# part1()


def change_turns(current="santa"):
    return "santa" if current == "robot" else "robot"


def part2():
    points = {"santa": [(0, 0)], "robot": [(0, 0)]}
    current_turn = "santa"

    for dir in parsed_lines:
        (current_x, current_y) = points[current_turn][-1]

        match dir:
            case "^":
                current_y += 1
            case "v":
                current_y -= 1
            case ">":
                current_x += 1
            case "<":
                current_x -= 1

        points[current_turn].append((current_x, current_y))
        current_turn = change_turns(current_turn)

    unique_houses = set(points["santa"]).union(points["robot"])

    print(len(unique_houses))


part2()
