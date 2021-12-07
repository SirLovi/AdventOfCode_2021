from os import path
from collections import defaultdict

absolute_path = path.dirname(path.abspath(__file__))


def solve(data):

    dict1, dict2 = defaultdict(int)

    for line in data:
        a, b = line.split('->')
        x1, y1 = map(int, a.split(','))
        x2, y2 = map(int, b.split(','))

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                dict1[x1, i] += 1
                dict2[x1, i] += 1

        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                dict1[i, y1] += 1
                dict2[i, y1] += 1

        else:
            a = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            b = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
            for x, y in zip(a, b):
                dict2[x, y] += 1

        overlaps1 = sum(x > 1 for x in dict1.values())

        overlaps2 = sum(x > 1 for x in dict2.values())

    print("\n1:")
    print("Overlaps: ", overlaps1)

    print("\n2:")
    print("Overlaps: ", overlaps2)


with open(absolute_path + "/input.txt", 'r') as file:
    data = file.readlines()


# print(data)

solve(data)
