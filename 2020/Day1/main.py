# Part 1

with open('input.txt', 'r') as file:
    lines = file.readlines()

years = [int(l.replace('\\n', '')) for l in lines]
years.sort()

def get_2_that_sum(year_list):
    size = len(year_list)

    for i in range(size - 1):
        for j in range(size - 1, 1, -1):
            if year_list[i] + year_list[j] == 2020:
                return year_list[i] * year_list[j]

# print(getMult(years))
# Part 2
def get_3_that_sum(year_list):
    size = len(year_list)
    half = int(size / 2)

    for i in range(size):
        for j in range(i + 1):
            for k in range (j + 1):
                if year_list[i] + year_list[j] + year_list[k] == 2020:
                    return year_list[i] * year_list[j] * year_list[k]

print(get_3_that_sum(years))