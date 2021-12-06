from os import path

absolute_path = path.dirname(path.abspath(__file__))


"""def solve(data):

    data_last_period = data
    data_now = data

    for day in range(0, 256):
        for fish in range(len(data_last_period)):
            if data_last_period[fish][0] == 0:
                data_now.append([8, 8])
                data_now[fish] = [6, 6]
            else:
                data_now[fish] = [
                    data_last_period[fish][0]-1, data_last_period[fish][1]]
            data_last_period = data_now

    # print(data_now)

    print("\n1:")
    print("Number o'fish: ", len(data_now))"""


def solve(data):

    for day in range(0, 256):
        fish = [data[i + 1] for i in range(8)] + [0]
        fish[6] += data[0]
        fish[8] += data[0]
        data = fish
        if day == 79:
            print("\n1:")
            print("Number o'fish: ", sum(data))

    print("\n2:")
    print("Number o'fish: ", sum(data))


data = [0] * 9

with open(absolute_path + "/6_input.txt", 'r') as file:
    for n in file.read().split(","):
        data[int(n)] += 1


# print(data)

solve(data)
