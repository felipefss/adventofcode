import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from util.io import readfile

INPUT_FILE = "example.txt"


def part1(left: list[int], right: list[int]):
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    total = 0

    for i in range(len(sorted_left)):
        total += abs(sorted_left[i] - sorted_right[i])

    print(total)


def part2(left: list[int], right: list[int]):
    score = 0

    for num in left:
        appearances = right.count(num)
        if appearances > 0:
            score += num * appearances

    print(score)


if __name__ == "__main__":
    ids_input: list[str] = readfile(INPUT_FILE)

    left = []
    right = []

    for pair in ids_input:
        [a, b] = pair.replace("   ", ",").split(",")
        left.append(int(a))
        right.append(int(b))

    # part1(left, right)
    part2(left, right)
