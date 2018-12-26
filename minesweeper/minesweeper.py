def isvalided(board_array, i, j):
    rows = len(board_array)
    cols = len(board_array[0])
    if 0 <= i < rows and 0 <= j < cols:
        return 1
    return 0


def countadjmines(board_array, i, j):
    count = 0
    count += (isvalided(board_array, i - 1, j - 1) and board_array[i - 1][j - 1] == '*')
    count += (isvalided(board_array, i - 1, j) and board_array[i - 1][j] == '*')
    count += (isvalided(board_array, i - 1, j + 1) and board_array[i - 1][j + 1] == '*')
    count += (isvalided(board_array, i, j - 1) and board_array[i][j - 1] == '*')
    count += (isvalided(board_array, i, j + 1) and board_array[i][j + 1] == '*')
    count += (isvalided(board_array, i + 1, j - 1) and board_array[i + 1][j - 1] == '*')
    count += (isvalided(board_array, i + 1, j) and board_array[i + 1][j] == '*')
    count += (isvalided(board_array, i + 1, j + 1) and board_array[i + 1][j + 1] == '*')

    return count


def board(board_array):
    if not board_array:
        return board_array
    rows = len(board_array)
    cols = len(board_array[0])

    for i_row in range(rows):
        if len(board_array[i_row]) != cols:
            raise ValueError("ERR")
        for i_col in range(cols):
            tmp = board_array[i_row][i_col]
            if tmp not in '* ':
                raise ValueError('ERR')
            if tmp != '*':
                count = countadjmines(board_array, i_row, i_col)
                if count > 0:
                    board_array[i_row] = board_array[i_row][:i_col] + str(count) + board_array[i_row][i_col + 1:]
    return board_array
