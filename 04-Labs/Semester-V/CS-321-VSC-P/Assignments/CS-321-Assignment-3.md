# Assignment 3: Constraint Satisfaction Problems

## Problem Statement / Aim
To model and solve a Constraint Satisfaction Problem (CSP) by implementing an algorithm to solve the classic N-Queens problem using backtracking.

## Theory & Concept
A Constraint Satisfaction Problem (CSP) involves finding a state or assignment of values to variables such that a set of constraints are satisfied. The N-Queens problem is a classic CSP where the goal is to place N queens on an N×N chessboard so that no two queens threaten each other. This means no two queens can share the same row, column, or diagonal. The problem is generally solved using backtracking, where we place a queen in each row one by one, and if we reach a state where placing a queen is not possible, we backtrack to the previous row and try a different position.

## Fully Solved Code
```python
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check this column on upper rows
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row >= n:
        solutions.append(["".join(r) for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = '.' # Backtrack

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

if __name__ == "__main__":
    n = 4
    print(f"Solving {n}-Queens Problem...")
    solutions = solve_n_queens(n)
    
    print(f"Total solutions found: {len(solutions)}\n")
    for idx, sol in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in sol:
            print(" ".join(row))
        print()
```

## Expected Output
```text
Solving 4-Queens Problem...
Total solutions found: 2

Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .
```

[[CS-321-Viva-3|View Viva Questions]]
