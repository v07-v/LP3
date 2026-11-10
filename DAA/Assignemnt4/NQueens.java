public class NQueens {

    static int boardSize; // Size of the chessboard

    // Function to print the solution matrix
    static void printSolution(int[][] board) {
        for (int rowIndex = 0; rowIndex < boardSize; rowIndex++) {
            for (int columnIndex = 0; columnIndex < boardSize; columnIndex++) {
                System.out.print(board[rowIndex][columnIndex] + " ");
            }
            System.out.println();
        }
    }

    // Function to check if a queen can be placed at board[row][col]
    static boolean isSafe(int[][] board, int row, int col) {

        // Check this column on the upper side
        for (int rowIndex = 0; rowIndex < row; rowIndex++) {
            if (board[rowIndex][col] == 1) {
                return false;
            }
        }

        // Check upper diagonal on the left side
        for (int rowIndex = row, columnIndex = col;
             rowIndex >= 0 && columnIndex >= 0; rowIndex--, columnIndex--) {
            if (board[rowIndex][columnIndex] == 1) {
                return false;
            }
        }

        // Check upper diagonal on the right side
        for (int rowIndex = row, columnIndex = col;
             rowIndex >= 0 && columnIndex < boardSize; rowIndex--, columnIndex++) {
            if (board[rowIndex][columnIndex] == 1) {
                return false;
            }
        }

        return true;
    }

    // Recursive function to solve the N-Queens problem
    static boolean solveNQueens(int[][] board, int row) {

        // Base case: If all queens are placed
        if (row >= boardSize) {
            return true;
        }

        // Try placing a queen in each column of the current row
        for (int columnIndex = 0; columnIndex < boardSize; columnIndex++) {
            if (isSafe(board, row, columnIndex)) {

                board[row][columnIndex] = 1; // Place the queen

                // Recur to place the remaining queens
                if (solveNQueens(board, row + 1)) {
                    return true;
                }

                // Backtrack: Remove the queen
                board[row][columnIndex] = 0;
            }
        }

        return false; // No solution found
    }

    public static void main(String[] args) {

        boardSize = 8; // Size of the chessboard
        int[][] board = new int[boardSize][boardSize];

        // Place the first queen at position (0, 0)
        board[0][0] = 1;

        // Solve the problem for the remaining queens
        if (solveNQueens(board, 1)) {
            printSolution(board);
        } else {
            System.out.println("No solution exists.");
        }
    }
}