with open("input.txt") as file:
    parsed_lines = ""

    for line in file:
        parsed_lines = parsed_lines + line.strip()

# Part 1
floor = 0
# for dir in parsed_lines:
#     if dir == "(":
#         floor += 1
#     if dir == ")":
# floor -= 1

# print(floor)

# Part 2
for i in range(len(parsed_lines)):
    if parsed_lines[i] == "(":
        floor += 1
    if parsed_lines[i] == ")":
        floor -= 1

    if floor == -1:
        print(i + 1)
        break
