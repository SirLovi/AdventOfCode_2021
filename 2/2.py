from os import path

absolute_path = path.dirname(path.abspath(__file__))


def solve1(data):
    currpos = 0
    currdepth = 0

    for i in range(0, len(data)):
        if(data[i] == "forward"):
            currpos += int(data[i+1])
        elif(data[i] == "down"):
            currdepth += int(data[i+1])
        elif(data[i] == "up"):
            currdepth -= int(data[i+1])

    print("\n1:")
    print("Final Position: ", currpos)
    print("Final Depth: ", currdepth)
    print("Multiplyied: ", currdepth*currpos)


def solve2(data):
    currpos = 0
    currdepth = 0
    aim = 0

    for i in range(0, len(data)):
        if(data[i] == "forward"):
            currpos += int(data[i+1])
            currdepth += aim * int(data[i+1])
        elif(data[i] == "down"):
            aim += int(data[i+1])
        elif(data[i] == "up"):
            aim -= int(data[i+1])

    print("\n1:")
    print("Final Position: ", currpos)
    print("Final Depth: ", currdepth)
    print("Multiplyied: ", currdepth*currpos)


with open(absolute_path + "/2_input.txt", 'r') as txtfile:
    input_list = txtfile.readlines()
    data = [str(val) for curr_line in input_list for val in curr_line.split()]

print(data)

solve1(data)

solve2(data)
