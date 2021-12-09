from os import path
from collections import Counter

absolute_path = path.dirname(path.abspath(__file__))


def solve(data):

    risk_sum = 0
    local_min = 0
    seen = {}
    stack = []
    for row in range(len(data)):
        for position in range(len(data[0])):

            if all(
                row + diff_row < 0
                or row + diff_row >= len(data)
                or position + diff_pos < 0
                or position + diff_pos >= len(data[0])
                or data[row][position] < data[row + diff_row][position + diff_pos]
                for diff_row, diff_pos in ((0, -1), (0, 1), (-1, 0), (1, 0))
            ):
                risk_sum += 1 + data[row][position]

            if (row, position) not in seen and data[row][position] != 9:
                stack.append((row, position))
                while stack:
                    row, position = stack.pop()
                    for diff_row, diff_pos in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                        r_ = row + diff_row
                        c_ = position + diff_pos
                        if 0 <= r_ < len(data) and 0 <= c_ < len(data[0]):
                            if (r_, c_) not in seen and data[r_][c_] != 9:
                                seen[(r_, c_)] = local_min
                                stack.append((r_, c_))
                local_min += 1

    a, b, position = Counter(list(seen.values())).most_common(3)
    part2 = (a[1] * b[1] * position[1])

    print("\n1:")
    print("Risk sum: ", risk_sum)

    print("\n2:")
    print("Largest basins multiplied: ", part2)


with open(absolute_path + "/input.txt", 'r') as file:
    data = [list(map(int, line[:-1])) for line in file.readlines()]


# print(data)

solve(data)
