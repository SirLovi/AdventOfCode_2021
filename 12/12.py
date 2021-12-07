from os import path

absolute_path = path.dirname(path.abspath(__file__))


def solve(data):

    med = data[len(data) // 2]
    fuel_used1 = sum(abs(n - med) for n in data)

    mean = sum(data) // len(data)
    fuel_used2 = sum(abs(n - mean) * (abs(n - mean) + 1) // 2 for n in data)

    print("\n1:")
    print("Fuel used: ", fuel_used1)

    print("\n2:")
    print("Fuel used: ", fuel_used2)


with open(absolute_path + "/input.txt", 'r') as file:
    data = list(sorted(int(n) for n in file.read().split(",")))


# print(data)

solve(data)
