def handle_coordinates(coordinates_str, board):
    coordinates = coordinates_str.split()
    try:
        row_num = int(coordinates[0])
        col_num = int(coordinates[1])
        return get_coordinates(row_num=row_num, col_num=col_num, board=board, is_user=True)
    except ValueError:
        print("You should enter numbers!")
        return []
    except IndexError:
        print("You should enter numbers!")
        return []


def get_coordinates(row_num, col_num, board, is_user):
    if row_num < 1 or row_num > 3 or col_num < 1 or col_num > 3:
        if is_user:
            print("Coordinates should be from 1 to 3!")
        return []
    cell = board.get_cell_at_position(row_num=row_num - 1, col_num=col_num - 1)
    if cell.occupied:
        if is_user:
            print("This cell is occupied! Choose another one!")
        return []
    return [row_num, col_num]


def handle_int_coordinates(row_num, col_num, board):
    return get_coordinates(row_num=row_num, col_num=col_num, board=board, is_user=False)

