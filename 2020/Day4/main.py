import re

lines = []

with open('input.txt', 'r') as file:
    line = file.readline()

    while line:
        lines.append(line.replace('\n', ''))
        line = file.readline()


def organize_passports():
    docs = []
    pp = dict()
    size = len(lines)

    for l in range(size):
        if lines[l] != '':
            info = lines[l].split(' ')
            for i in info:
                [k, v] = i.split(':')
                pp[k] = v
        if lines[l] == '' or l == size - 1:
            docs.append(pp)
            pp = dict()
    return docs


def part1(docs):
    count = 0
    for d in docs:
        if all(k in d for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
            count += 1
    return count


def part2_validation(doc):
    if int(doc['byr']) < 1920 or int(doc['byr']) > 2002:
        return False
    if int(doc['iyr']) < 2010 or int(doc['iyr']) > 2020:
        return False
    if int(doc['eyr']) < 2020 or int(doc['eyr']) > 2030:
        return False
    if 'cm' not in doc['hgt'] and 'in' not in doc['hgt']:
        return False
    if 'cm' in doc['hgt'] and (int(doc['hgt'].replace('cm', '')) < 150 or int(doc['hgt'].replace('cm', '')) > 193):
        return False
    if 'in' in doc['hgt'] and (int(doc['hgt'].replace('in', '')) < 59 or int(doc['hgt'].replace('in', '')) > 76):
        return False
    if not re.match(r"#([0-9]|[A-f]){6}", doc['hcl']):
        return False
    if not any(x in doc['ecl'] for x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False
    if len(doc['pid']) != 9:
        return False

    return True


def part2(docs):
    count = 0
    for d in docs:
        if all(k in d for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
            if part2_validation(d):
                count += 1

    return count


if __name__ == "__main__":
    # Part 1
    passports = organize_passports()
    print(part1(passports))

    # Part 2
    print(part2(passports))
