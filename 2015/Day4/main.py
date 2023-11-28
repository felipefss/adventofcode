import hashlib

input = "iwrupvqb"
# input = "abcdef"
# 609043


def find_hash(number_of_zeros: int, start=-1):
    i = start
    h = ""

    while not h.startswith("0" * number_of_zeros):
        i += 1
        hash_input = input + str(i)
        h = hashlib.md5(hash_input.encode("utf-8")).hexdigest()

    print(i)


# Part 1
# find_hash(5)

# Part 2
find_hash(6, 346386)
# 9958218
