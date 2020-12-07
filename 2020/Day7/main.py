import re


def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def get_bag_info(bag):
    info = re.search(r'(\d+)? ?(\w+ \w+)', bag)
    quantity = int(info[1]) if info[1] != None else None
    color = info[2]

    return quantity, color


def build_rules(data):
    rules = {}

    for d in data:
        [outer, inner] = map(lambda b: b.strip(), d.split('contain'))
        inner_bags = [re.sub(r' bags?.?', '', x) for x in inner.split(', ')]

        bag_color = re.sub(r' bags?', '', outer)
        bag = {}
        for ib in inner_bags:
            info = re.findall(r'(\d+)? ?(\w+ \w+)', ib)
            quantity = int(info[0][0]) if info[0][0] != '' else 0
            color = info[0][1]
            if quantity:
                bag[color] = quantity
        rules[bag_color] = bag

    return rules


def part1(bags, my_bag, rules):
    output = False

    for b in bags:
        if b == my_bag:
            return True
        else:
            output = part1(rules[b], my_bag, rules)
            if output:
                return True

    return output


if __name__ == "__main__":
    data = get_input('input.txt')
    rules = build_rules(data)

    # Part 1
    part1_count = 0
    for r, bags in rules.items():
        if r != 'shiny gold':
            part1_count += 1 if part1(bags, 'shiny gold', rules) else 0
    print(part1_count)
