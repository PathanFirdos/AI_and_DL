# --- N-Queens Problem using Backtracking (All Solutions) ---

# Function to print the chessboard
def print_solution(board, N):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

# Check if a queen can be placed at board[row][col]
def is_safe(board, row, col, N):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve the problem
def solve(board, row, N, solutions):
    if row == N:  # All queens are placed
        print_solution(board, N)
        solutions.append([row[:] for row in board])  # store a copy
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place queen
            solve(board, row + 1, N, solutions)  # Recur for next row
            board[row][col] = 0  # Backtrack

# Driver code
if __name__ == "__main__":
    N = int(input("Enter number of queens (e.g., 4, 8): "))
    board = [[0] * N for _ in range(N)]
    solutions = []
    
    solve(board, 0, N, solutions)

    if not solutions:
        print("No solution exists")
    else:
        print(f"Total solutions found: {len(solutions)}")

