def handle_coordinates(coordinates_str, board):
    coordinates = coordinates_str.split()
    try:
        row_num = int(coordinates[0])
        col_num = int(coordinates[1])
        if row_num < 1 or row_num > 3 or col_num < 1 or col_num > 3:
            print("Coordinates should be from 1 to 3!")
            return []
        cell = board.get_cell_at_position(row_num=row_num - 1, col_num= col_num - 1)
        if cell.occupied:
            print("This cell is occupied! Choose another one!")
            return []
        return [row_num, col_num]
    except ValueError:
        print("You should enter numbers!")
        return []
    except IndexError:
        print("You should enter numbers!")
        return []

