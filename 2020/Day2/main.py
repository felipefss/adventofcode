import re

# Part 1
passwords = []

with open('input.txt', 'r') as file:
    line = file.readline()

    while line:
        line.replace('\\n', '')
        [pol, pwd] = line.split(':')
        passwords.append([pwd.strip(), pol.strip()])
        line = file.readline()


def isPassValid_1(pwd, policy):
    rgx = re.search(r'(\d+-\d+) (\w)', policy)
    letter = rgx.group(2)
    occurrences = rgx.group(1)
    [min_o, max_o] = map(lambda n: int(n), occurrences.split('-'))

    count = pwd.count(letter)
    return min_o <= count <= max_o


def isPassValid_2(pwd, policy):
    rgx = re.search(r'(\d+-\d+) (\w)', policy)
    letter = rgx.group(2)
    constraints = rgx.group(1)
    pos = map(lambda n: int(n) - 1, constraints.split('-'))

    count = 0
    for i in pos:
        if pwd[i] == letter:
            count += 1

    return count == 1


if __name__ == "__main__":
    valid_passwords1 = 0
    valid_passwords2 = 0

    for [pwd, policy] in passwords:
        if isPassValid_1(pwd, policy):
            valid_passwords1 += 1
        if isPassValid_2(pwd, policy):
            valid_passwords2 += 1

    print('Number of valid passwords - part1', valid_passwords1)
    print('Number of valid passwords - part2', valid_passwords2)
