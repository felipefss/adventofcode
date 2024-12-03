import sys
import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

from util.io import readfile

INPUT_FILE = "input.txt"


def part1():
    id_input: list[str] = readfile(INPUT_FILE)
    left = []
    right = []

    for pair in id_input:
        [a, b] = pair.replace("   ", ",").split(",")
        left.append(int(a))
        right.append(int(b))

    left.sort()
    right.sort()

    total = 0

    for i in range(len(left)):
        total += abs(left[i] - right[i])

    print(total)


def part2():
    pass


part1()
