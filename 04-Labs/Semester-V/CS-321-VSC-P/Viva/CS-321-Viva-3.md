[[CS-321-Assignment-3|Back to Assignment]]

# Viva Questions: Constraint Satisfaction Problems

1. **What defines a Constraint Satisfaction Problem (CSP)?**
   *A CSP is defined by a set of variables, a domain of values for each variable, and a set of constraints that restrict the allowable combinations of values for the variables.*

2. **Why is the N-Queens problem considered a CSP?**
   *Because the variables (queens) must be assigned values (positions on the board) such that specific constraints (no two queens attack each other horizontally, vertically, or diagonally) are satisfied.*

3. **What is Backtracking in the context of CSPs?**
   *Backtracking is a depth-first search approach where we build a solution incrementally, and as soon as we determine that a partial solution cannot be completed to a valid solution, we abandon it (backtrack).*

4. **What is constraint propagation?**
   *It is the process of using the constraints to reduce the domain of possible values for the variables, thereby simplifying the problem before or during the search.*

5. **Mention some real-world applications of CSPs.**
   *Map coloring, scheduling problems, timetabling, and Sudoku puzzle solving are classic real-world applications of CSPs.*
