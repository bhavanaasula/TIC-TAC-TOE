import numpy as np

board = np.array([" ", " ", " ", 
                  " ", " ", " ", 
                  " ", " " , " "])

def display_board():
    print("\n---- TIC TAC TOE ----")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("----+----+----")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("----+----+----")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(symbol):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for w in win_conditions:
        if board[w[0]] == board[w[1]] == board[w[2]] == symbol:
            return True
    return False

def is_draw():
    return " " not in board

while True:
    display_board()
    pos = int(input("\nEnter position (1-9): ")) - 1

    if pos < 0 or pos > 8:
        print("Invalid position!")
        continue

    if board[pos] != " ":
        print("Position already taken!")
        continue

    # Player move
    board[pos] = "X"

    if check_winner("X"):
        display_board()
        print("Player X Wins!")
        break

    if is_draw():
        display_board()
        print("It's a Draw!")
        break

    # Computer move
    print("Computer playing...")
    empty_spots = np.where(board == " ")[0]
    comp_pos = np.random.choice(empty_spots)
    board[comp_pos] = "O"

    if check_winner("O"):
        display_board()
        print("Computer O Wins!")
        break

    if is_draw():
        display_board()
        print("It's a Draw!")
        break
