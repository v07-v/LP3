# Assignment 4: N-Queens

## Important code

- `isSafe()` checks the column and both upper diagonals before placing a queen.
- `solveNQueens()` places one queen per row and backtracks when a partial board cannot lead to a solution.

## Concept used: Backtracking

- Backtracking solves a problem by making one choice at a time. Here, the program places
  one queen in each row and checks whether the board is still valid.
- If a placement blocks all possible positions for a later queen, the program removes
  the last queen and tries another column. This step is called backtracking.
- The method avoids checking every complete board because invalid partial boards are
  rejected early. It is useful for problems where choices depend on earlier choices.

## Complexity of the program

- For an `N x N` board, the worst-case time is approximately `O(N * N!)`.
  The factorial part comes from trying many queen arrangements, and `isSafe()`
  can scan up to `N` positions for each trial.
- The board uses `O(N^2)` space. The recursive calls add `O(N)` stack space,
  so the board is the main memory requirement.

## Complexity of the concept

- Backtracking often has exponential or factorial worst-case time because it may
  try many combinations. For N-Queens, a common bound is `O(N!)`.
- Its space is usually based on the stored solution and recursion depth. Here that
  means `O(N^2)` for the board and `O(N)` for the recursion stack.
