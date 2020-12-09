def get_input(fname):
    data = []
    with open(fname, 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def find_sum(nums, result):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == result:
                return True
    return False


def part1(data, preamble):
    for i in range(preamble, len(data)):
        start = i - preamble
        if not find_sum(data[start:i], data[i]):
            return data[i]
    return 0


def part2(data, wrong_number):
    min_i = max_i = total = 0
    # max_i = 0
    # total = 0

    while total != wrong_number and max_i < len(data):
        if total > wrong_number:
            total = 0
            min_i += 1
        else:
            max_i += 1
        total = sum(data[min_i:max_i])

    sub_list = data[min_i:max_i]
    sub_list.sort()

    return sub_list[0] + sub_list[-1]


if __name__ == "__main__":
    data = [int(n) for n in get_input('input.txt')]

    # Part 1
    wrong_number = part1(data, 25)
    print(wrong_number)

    # Part 2
    print(part2(data, wrong_number))
