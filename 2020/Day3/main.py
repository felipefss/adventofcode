tobo_map = []

with open('./input.txt', 'r') as file:
    line = file.readline()
    while line:
        tobo_map.append(line.replace('\n', ''))
        line = file.readline()


def trees_on_slope(right, down):
    row_i = down
    col = 0
    trees = 0

    while row_i < len(tobo_map):
        row = tobo_map[row_i]
        col += right

        if col >= len(row):
            col = col - len(row)

        if row[col] == '#':
            trees += 1
        row_i += down

    return trees


if __name__ == "__main__":
    #Part 1
    print(trees_on_slope(3, 1))

    #Part 2
    mult = 1
    for [r, d] in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        mult *= trees_on_slope(r, d)
    print(mult)