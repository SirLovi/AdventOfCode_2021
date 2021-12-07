from os import path

absolute_path = path.dirname(path.abspath(__file__))


def solve1(data):
    increased = 0
    decreased = 0

    for i in range(0, len(data)):
        if(i == 3):
            continue
        if (data[i] > data[i-1]):
            increased += 1
        elif(data[i] < data[i-1]):
            decreased += 1

    print("\n1:")
    print("Increased: ", increased)
    print("Decreased: ", decreased)


def solve2(data):
    increased = 0
    decreased = 0

    for i in range(0, len(data)):
        if(i == 0):
            continue
        if (data[i]+data[i-1]+data[i-2] > data[i-1]+data[i-2]+data[i-3]):
            increased += 1
        elif(data[i]+data[i-1]+data[i-2] < data[i-1]+data[i-2]+data[i-3]):
            decreased += 1

    print("\n2:")
    print("Increased: ", increased)
    print("Decreased: ", decreased)


with open(absolute_path + "/input.txt", 'r') as txtfile:
    data = [int(num) for curr_line in txtfile.readlines()
            for num in curr_line.split()]

solve1(data)

solve2(data)
