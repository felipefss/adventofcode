import re

with open(
    "/Users/felipe.f.santos/Documents/learning/adventofcode/2023/Day1/input.txt"
) as file:
    lines = []

    for line in file:
        lines.append(line.replace("\n", ""))


# Part 1
def part1():
    sum = 0

    for line in lines:
        vals = [x for x in re.findall("\d", line)]
        sum += int(vals[0] + vals[-1])

    print(sum)


# part1()


def parse_spelled_number(num: str):
    nums_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    return num if num.isdecimal() else nums_map[num]


def find_numbers_in_line(line: str):
    found_nums = []
    nums = "01234567789"
    spelled_nums = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for n in nums:
        ind = 0
        while True:
            ind = line.find(n, ind)
            if ind == -1:
                break
            found_nums.append({"val": n, "pos": ind})
            ind += 1

    for n in spelled_nums:
        ind = 0
        while True:
            ind = line.find(n, ind)
            if ind == -1:
                break
            found_nums.append({"val": parse_spelled_number(n), "pos": ind})
            ind += 1

    return found_nums


# Part 2
def part2():
    sum = 0

    for line in lines:
        vals = find_numbers_in_line(line)
        vals.sort(key=lambda v: v["pos"])

        sum += int(vals[0]["val"] + vals[-1]["val"])

    print(sum)


part2()
