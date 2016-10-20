from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship! You have 10 turns")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board) + 1
ship_col = random_col(board) + 1

for turn in range(10):
    turn_number = turn + 1
    print('Turn %s' % turn_number)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if guess_row not in range(6) or guess_col not in range(6):
            print("Oops, that's not even in the ocean.")
            print()
        elif(board[guess_row - 1][guess_col - 1] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            print()
            board[guess_row - 1][guess_col - 1] = "X"
    print_board(board)
    if turn == 9:
        print('Game Over.')