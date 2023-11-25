with open("input.txt") as file:
    parsed_lines: list[list[int]] = []

    for line in file:
        parsed_lines.append([int(x) for x in line.strip().split("x")])


# Part 1
def part1():
    total = 0

    for [l, w, h] in parsed_lines:
        area1 = l * w
        area2 = w * h
        area3 = h * l
        smallest = min(area1, area2, area3)

        total += (2 * area1 + 2 * area2 + 2 * area3) + smallest

    print(total)


# part1()


# Part 2
def part2():
    total = 0

    for dimensions in parsed_lines:
        dimensions.sort()
        [a, b, c] = dimensions
        total += (2 * a + 2 * b) + (a * b * c)

    print(total)


part2()
