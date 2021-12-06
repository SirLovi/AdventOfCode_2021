from os import path
from collections import Counter

absolute_path = path.dirname(path.abspath(__file__))

cat = ''.join


def transpose(matrix):
    return list(zip(*matrix))


def solve1(data):
    gamma = ""
    epsilon = ""

    one_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zero_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, len(data)):
        for j in range(0, len(data[0])):

            if(data[i][j] == '1'):
                one_counter[j] += 1
            elif(data[i][j] == '0'):
                zero_counter[j] += 1

    for i in range(0, len(one_counter)):
        if(one_counter[i] > zero_counter[i]):
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    print("\n1:")
    print("Ones: ", one_counter)
    print("Zeros: ", zero_counter)
    print("Gamma: ", int(gamma, 2))
    print("Epsilon: ", int(epsilon, 2))
    print("Multiplied: ", int(gamma, 2)*int(epsilon, 2))


def most_common(col):
    (first, x), (second, y) = Counter(col).most_common(2)
    if x == y:
        first = '1'
        second = '0'
    return first, second


def bin2int(s): return int(cat(s), 2)


def get_stuff(data, is_least_common):
    rows = data.copy()
    for i in range(len(rows[0])):
        t = transpose(rows)
        wanted = most_common(t[i])[is_least_common]
        rows = [line for line in rows if line[i] == wanted]
        if len(rows) == 1:
            return bin2int(rows)


def part_1(data):
    l = [most_common(col) for col in transpose(data)]
    l = transpose(l)
    return bin2int(l[0]) * bin2int(l[1])


def part_2(data):
    t = transpose(data)
    g = get_stuff(data, False)
    e = get_stuff(data, True)
    return g * e


def solve2(data):
    gamma = ""
    epsilon = ""

    one_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    zero_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    most_common = []
    least_common = []

    for i in range(0, len(data)):
        for j in range(0, len(data[0])):

            if(data[i][j] == '1'):
                one_counter[j] += 1
            elif(data[i][j] == '0'):
                zero_counter[j] += 1

    for i in range(0, len(one_counter)):
        if(one_counter[i] > zero_counter[i]):
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'

    print("\n1:")
    print("Ones: ", one_counter)
    print("Zeros: ", zero_counter)
    print("Gamma: ", int(gamma, 2))
    print("Epsilon: ", int(epsilon, 2))
    print("Multiplied: ", int(gamma, 2)*int(epsilon, 2))


lines = ""
n_bits = 0

with open(absolute_path + "/3_input.txt", 'r') as txtfile:
    data = [str(val) for curr_line in txtfile.readlines()
            for val in curr_line.split()]


print(part_1(data))
print(part_2(data))

# print(data)

# solve1(data)

# solve2(data)
