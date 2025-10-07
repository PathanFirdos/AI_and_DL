import math

# --- Tic Tac Toe using Minimax ---

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check winner
def check_winner(board):
    # rows, cols, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":  # AI win
        return 1
    elif winner == "O":  # Human win
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# AI chooses best move
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# --- Play Game ---
board = [[" " for _ in range(3)] for _ in range(3)]

print("Tic Tac Toe! You are O, AI is X")
while True:
    print_board(board)

    if check_winner(board) or is_full(board):
        break

    # Human move
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))
    if board[row][col] == " ":
        board[row][col] = "O"
    else:
        print("Invalid move!")
        continue

    if check_winner(board) or is_full(board):
        break

    # AI move
    move = best_move(board)
    if move:
        board[move[0]][move[1]] = "X"

winner = check_winner(board)
print_board(board)
if winner:
    print("Winner is:", winner)
else:
    print("It's a draw!")
