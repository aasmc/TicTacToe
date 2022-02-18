from BoardRow import create_row
from Cell import Cell


class GameBoard:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self):
        border = str("-" * 9)
        res = f"{border}\n"
        for row in self.rows:
            res = f"{res}{row}\n"
        res = f"{res}{border}"
        return res

    def get_cell_at_position(self, row_num, col_num):
        return self.rows[row_num].cells[col_num]

    def get_next_player(self):
        count_x = 0
        count_o = 0
        for row in self.rows:
            for cell in row.cells:
                if cell.symbol == "X":
                    count_x += 1
                elif cell.symbol == "O":
                    count_o += 1
        if count_x <= count_o:
            return "X"
        else:
            return "O"

    def update_cell(self, row_num, col_num, symbol):
        row = self.rows[row_num]
        row.update_cell(Cell(col_num=col_num, row_num=row_num, occupied=True, symbol=symbol))


def create_board(input_str):
    rows = []
    for i in range(0, 3):
        start = i * 3
        end = start + 3
        row = create_row(row_num=i, input_str=input_str[start:end])
        rows.append(row)
    return GameBoard(rows)























