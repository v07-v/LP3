def is_safe(board, row, column, size):
    for other_row in range(size):
        if board[other_row][column] == 1:
            return False

    for other_row in range(size):
        for other_column in range(size):
            if (
                board[other_row][other_column] == 1
                and abs(other_row - row) == abs(other_column - column)
            ):
                return False

    return True


def solve_n_queens(board, row, size):
    if row == size:
        return True

    if 1 in board[row]:
        return solve_n_queens(board, row + 1, size)

    for column in range(size):
        if is_safe(board, row, column, size):
            board[row][column] = 1

            if solve_n_queens(board, row + 1, size):
                return True

            board[row][column] = 0

    return False


def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))


def main():
    size = int(input("Enter the value of n: "))
    first_row, first_column = map(
        int,
        input(
            "Enter the first queen position (row and column, starting from 1): "
        ).split(),
    )

    first_row -= 1
    first_column -= 1

    if size < 1 or not (0 <= first_row < size and 0 <= first_column < size):
        print("Invalid board size or queen position.")
        return

    board = [[0 for _ in range(size)] for _ in range(size)]
    board[first_row][first_column] = 1

    if solve_n_queens(board, 0, size):
        print("\nN-Queens solution:")
        print_solution(board)
    else:
        print("No solution exists for the given first queen position.")


if __name__ == "__main__":
    main()


# Sample input:
# 8
# 1 1
