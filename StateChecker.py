from State import State


def check_game_state(board):
    states = [
        check_rows_for_winner(board),
        check_cols_for_winner(board),
        check_main_diagonal_for_winner(board),
        check_secondary_diagonal_for_winner(board)
    ]
    if any([state == State.O_WINS for state in states]):
        return State.O_WINS
    if any(state == State.X_WINS for state in states):
        return State.X_WINS
    if check_for_draw(board):
        return State.DRAW
    return State.NOT_FINISHED


def check_rows_for_winner(board):
    for row in board.rows:
        state = check_row_for_winner(row)
        if state == State.O_WINS or state == State.X_WINS:
            return state
    return State.UNDEFINED


def check_row_for_winner(row):
    return get_state_for_cells(row.cells)


def get_state_for_cells(cells):
    cell_symbols = [cell.symbol for cell in cells]
    x_win = all(symbol == "X" for symbol in cell_symbols)
    o_win = all(symbol == "O" for symbol in cell_symbols)
    if x_win:
        return State.X_WINS
    elif o_win:
        return State.O_WINS
    else:
        return State.UNDEFINED


def check_cols_for_winner(board):
    for i in range(0, 3):
        state = check_col_for_winner(board, i)
        if state == State.X_WINS or state == State.O_WINS:
            return state
    return State.UNDEFINED


def check_col_for_winner(board, col):
    col_cells = [row.cells[col] for row in board.rows]
    return get_state_for_cells(col_cells)


def check_main_diagonal_for_winner(board):
    main_diagonal_cells = [board.rows[i].cells[i] for i in range(0, 3)]
    return get_state_for_cells(main_diagonal_cells)


def check_secondary_diagonal_for_winner(board):
    secondary_diagonal_cells = []
    row_idx = 0
    for i in range(2, -1, -1):
        cell = board.rows[row_idx].cells[i]
        secondary_diagonal_cells.append(cell)
        row_idx += 1
    return get_state_for_cells(secondary_diagonal_cells)


def check_for_draw(board):
    return all([row.all_cells_occupied() for row in board.rows])
