from os import path

absolute_path = path.dirname(path.abspath(__file__))


def solve(drawn_numbers, boards):

    score1 = 0
    score2 = 0

    tested_boards = set()

    for number in drawn_numbers:
        for board_index, board in enumerate(boards):
            if board_index in tested_boards:
                continue

            for i, j in ((i, j) for i in range(5) for j in range(5)):
                if board[i][j][0] == number:
                    board[i][j][1] = True
                    break
            else:
                continue

            row = all(board[x][j][1] for x in range(5))
            col = all(board[i][y][1] for y in range(5))
            if row or col:
                sum_ = sum(x for row in board for x, seen in row if not seen)

                if score1 == 0:
                    score1 = sum_ * number

                score2 = sum_ * number
                tested_boards.add(board_index)

    print("\n1:")
    print("Final score: ", score1)

    print("\n2:")
    print("Final score: ", score2)


with open(absolute_path + "/input.txt", 'r') as file:
    drawn_numbers = [int(n) for n in file.readline().split(",")]
    file.readline()
    boards = []
    board = []
    for line in file:
        if line.strip():
            board.append([[int(n), False] for n in line.split()])
        else:
            boards.append(board)
            board = []


# print(drawn_numbers)
# print(board)
# print(boards)

solve(drawn_numbers, boards)
