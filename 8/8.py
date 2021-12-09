from os import path
from itertools import permutations

absolute_path = path.dirname(path.abspath(__file__))


def solve(data):

    d = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9, }

    appearance = 0
    summed = 0
    for line in data:
        a, b = line.split(" | ")
        a = a.split()
        b = b.split()
        appearance += sum(len(code) in {2, 3, 4, 7} for code in b)
        for permutation in permutations("abcdefg"):
            to = str.maketrans("abcdefg", "".join(permutation))
            a_ = ["".join(sorted(code.translate(to))) for code in a]
            b_ = ["".join(sorted(code.translate(to))) for code in b]
            if all(code in d for code in a_):
                summed += int("".join(str(d[code]) for code in b_))
                break

    print("\n1:")
    print("Digits appeared x times: ", appearance)

    print("\n2:")
    print("Values added up: ", summed)


with open(absolute_path + "/input.txt", 'r') as file:
    data = file.readlines()


# print(data)

solve(data)
