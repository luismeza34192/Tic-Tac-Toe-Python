import random

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def user_move(board):
    while True:
        try:
            move = input("Enter your move (row and column, e.g., 0 1): ")
            r, c = map(int, move.split())
            if (r, c) in get_available_moves(board):
                board[r][c] = "X"
                break
            else:
                print("Invalid move. That space is taken.")
        except:
            print("Invalid input. Please enter two numbers separated by a space.")

def computer_move(board):
    move = random.choice(get_available_moves(board))
    board[move[0]][move[1]] = "O"
    print(f"Computer chose: {move[0]} {move[1]}")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe. You are X, the computer is O. The rows and columns start at 0.")
    print_board(board)

    while True:
        user_move(board)
        print_board(board)
        if check_win(board, "X"):
            print("You win.")
            break
        if check_draw(board):
            print("It's a draw.")
            break

        computer_move(board)
        print_board(board)
        if check_win(board, "O"):
            print("Computer wins.")
            break
        if check_draw(board):
            print("It's a draw.")
            break

if __name__ == "__main__":
    play_game()