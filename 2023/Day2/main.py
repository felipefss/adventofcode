import re
from functools import reduce

with open(
    "/Users/felipe.f.santos/Documents/learning/adventofcode/2023/Day2/input.txt"
) as file:
    games = []

    for line in file:
        [game, cubes] = line.split(":")
        [_, id] = game.split(" ")
        games.append({"id": int(id), "cubes": cubes.replace("\n", "")})


# Part 1
def parse_cubes_colors(game: list):
    cubes = {"red": 0, "green": 0, "blue": 0}
    sets = game["cubes"].split("; ")

    for set in sets:
        matches = re.findall("(\d+) (red|green|blue)", set)
        for val, color in matches:
            amount = int(val)
            if amount > cubes[color]:
                cubes[color] = amount

    return cubes


def part1():
    [red, green, blue] = [12, 13, 14]
    possibilities = []

    for game in games:
        parsed_colors = parse_cubes_colors(game)
        if (
            parsed_colors["red"] <= red
            and parsed_colors["green"] <= green
            and parsed_colors["blue"] <= blue
        ):
            possibilities.append(game["id"])

    print(possibilities)
    sum = reduce(lambda a, b: a + b, possibilities)
    print(sum)


# part1()


# Part 2
def part2():
    sum = 0

    for game in games:
        cubes = parse_cubes_colors(game)
        sum += cubes["red"] * cubes["green"] * cubes["blue"]

    print(sum)


part2()
