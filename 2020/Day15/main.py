import math


def get_number(data, limit: int) -> int:
    past = data.copy()
    i = len(past)

    while i < limit:
        last = past[i - 1]
        try:
            spoken_i = list(reversed(past[:-1])).index(last)
            pos = i - 1 - spoken_i
            age = i - pos

            past.append(age)
        except ValueError:
            past.append(0)
        i += 1

    return past[-1]


if __name__ == "__main__":
    inp = {
        'example1': '0,3,6',
        'example2': '1,3,2',
        'example3': '2,1,3',
        'example4': '1,2,3',
        'example5': '2,3,1',
        'example6': '3,2,1',
        'example7': '3,1,2',
        'input': '11,0,1,10,5,19'
    }

    data = [int(n) for n in inp['input'].split(',')]

    # Part 1
    print(get_number(data, 2020))
