def get_input():
    data = []
    with open('input.txt', 'r') as file:
        line = file.readline()

        while line:
            data.append(line.replace('\n', ''))
            line = file.readline()
    return data


def part1(questions):
    count_sum = 0
    size = len(questions)
    answers = set()

    for i in range(size):
        if questions[i] != '':
            person = [a for a in questions[i]]
            answers.update(set(person))
        if questions[i] == '' or i == size - 1:
            count_sum += len(answers)
            answers.clear()
    return count_sum


def part2(questions):
    count_sum = 0
    size = len(questions)
    answers = []

    for i in range(size):
        if questions[i] != '':
            person = [a for a in questions[i]]
            answers.append(set(person))
        if questions[i] == '' or i == size - 1:
            inter = set.intersection(*answers)
            count_sum += len(inter)
            answers.clear()
    return count_sum


if __name__=="__main__":
    # Part 1
    data = get_input()
    # print(part1(data))

    # Part 2
    print(part2(data))
