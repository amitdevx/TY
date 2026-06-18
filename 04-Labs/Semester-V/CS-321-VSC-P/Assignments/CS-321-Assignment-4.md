# Assignment 4: Game Playing Algorithms

## Problem Statement / Aim
To implement adversarial game playing algorithms, specifically using the Minimax algorithm, to determine optimal moves in a zero-sum game like Tic-Tac-Toe.

## Theory & Concept
In artificial intelligence, game playing often involves adversarial search, where two or more players have conflicting goals. The Minimax algorithm is a decision-making algorithm used for minimizing the possible loss for a worst-case scenario. It is widely used in two-player turn-based games such as Tic-Tac-Toe, Chess, and Checkers.
The algorithm evaluates the game tree recursively. One player (Maximizer) tries to maximize their score, while the other player (Minimizer) tries to minimize the score. It assumes that the opponent is playing optimally. A common optimization to standard Minimax is Alpha-Beta pruning, which eliminates branches of the game tree that don't need to be explored.

## Fully Solved Code
```python
import math

# Evaluate the board to see if there's a winner
def evaluate(board):
    # Checking rows for victory
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == 'X': return 10
            elif board[row][0] == 'O': return -10
            
    # Checking columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == 'X': return 10
            elif board[0][col] == 'O': return -10

    # Checking diagonals for victory
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X': return 10
        elif board[0][0] == 'O': return -10
        
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == 'X': return 10
        elif board[0][2] == 'O': return -10
        
    return 0

# Check if there are moves remaining
def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

# The Minimax function
def minimax(board, depth, is_max):
    score = evaluate(board)
    
    # Maximizer has won
    if score == 10: return score - depth
    
    # Minimizer has won
    if score == -10: return score + depth
    
    # Tie
    if not is_moves_left(board): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = '_'
        return best

# Find the best move for the Maximizer
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = '_'
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
                    
    return best_move

if __name__ == "__main__":
    # Current state of the board
    board = [
        ['X', 'O', 'X'],
        ['O', 'O', 'X'],
        ['_', '_', '_']
    ]
    
    print("Current Board:")
    for row in board:
        print(" ".join(row))
        
    best_move = find_best_move(board)
    print(f"\nThe optimal move for 'X' is at row {best_move[0]} and column {best_move[1]}")
```

## Expected Output
```text
Current Board:
X O X
O O X
_ _ _

The optimal move for 'X' is at row 2 and column 2
```

[[CS-321-Viva-4|View Viva Questions]]
