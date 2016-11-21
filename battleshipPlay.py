""" 1-Player Battleship board game """
""" Random position; 5x5 grid; 10 guesses """
""" Index coordinates starts at zero """

## 5 x 5 Grid
board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print(print_board(board))

## Battleship Position
import random

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print("row: ", ship_row)
print("col: ", ship_col)

## Player guesses and check; 4 trials
for turn in range(4):
    print("Turn", turn + 1)

    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if turn == 3:
            print("Game Over")
        elif guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            board[guess_row][guess_col] = "X"
            print("You missed my battleship!")
            print_board(board)



""" Improvements:
1. Multiple battleships
2. Different size battleships
3. 2 player game
4. more features; rematches, statistics...
"""