# n_queens_csp.py

def is_safe(queens, row, col):
    """Check if a queen can be placed at (row, col)."""
    for r, c in enumerate(queens):
        # Same column or same diagonal
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_n_queens(n, row=0, queens=[]):
    """Backtracking CSP solver for N-Queens."""
    if row == n:
        return [queens]  # Found one solution

    solutions = []
    for col in range(n):
        if is_safe(queens, row, col):
            solutions.extend(solve_n_queens(n, row + 1, queens + [col]))
    return solutions

def print_solution(sol):
    """Pretty-print a board."""
    n = len(sol)
    for row in sol:
        print(" ".join("Q" if c == row else "." for c in range(n)))
    print()

if __name__ == "__main__":
    N = 8  # You can change this for other sizes
    sols = solve_n_queens(N)
    print(f"Found {len(sols)} solutions for {N}-Queens.\n")
    # Show first 3 solutions
    for s in sols[:3]:
        print_solution(s)
