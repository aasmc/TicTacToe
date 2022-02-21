from Cell import create_cell
from Cell import create_empty_cell


class BoardRow:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        cell_str = ""
        for cell in self.cells:
            cell_str = f"{cell_str}{cell} "
        return f"| {cell_str}|"

    def update_cell(self, updated_cell):
        for cell in self.cells:
            if cell.col_num == updated_cell.col_num and cell.row_num == updated_cell.row_num:
                cell.symbol = updated_cell.symbol
                cell.occupied = updated_cell.occupied
                break

    def all_cells_occupied(self):
        return all([cell.occupied for cell in self.cells])


def create_row(row_num, input_str):
    cells = [create_cell(symbol=input_str[i], col_num=i, row_num=row_num) for i in range(0, 3)]
    return BoardRow(cells)


def create_empty_row(row_num):
    cells = [create_empty_cell(col_num=i, row_num=row_num) for i in range(0, 3)]
    return BoardRow(cells)
