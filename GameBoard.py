from BoardRow import create_row
from Cell import Cell
from BoardRow import create_empty_row


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

    def get_win_coordinates(self, symbol):
        for row in self.rows:
            coords = row.get_winner_cell_coordinates(symbol)
            if coords:
                return coords
        coords = self.get_main_diagonal_win_coordinates(symbol)
        if coords:
            return coords
        coords = self.get_secondary_diagonal_win_coordinates(symbol)
        if coords:
            return coords
        for i in range(0, 3):
            coords = self.get_col_win_coordinates(i, symbol)
            if coords:
                return coords
        return []

    def get_col_win_coordinates(self, col_num, symbol):
        count = 0
        coords = []
        for row in self.rows:
            cell = row.cells[col_num]
            if cell.symbol == symbol:
                count += 1
        if count == 2:
            for row in self.rows:
                cell = row.cells[col_num]
                if cell.symbol == " ":
                    coords.append(cell.row_num[0] + 1)
                    coords.append(cell.col_num[0] + 1)
                    return coords
        return []

    def get_main_diagonal_win_coordinates(self, symbol):
        coords = []
        count = 0
        for i in range(0, 3):
            cell = self.rows[i].cells[i]
            if cell.symbol == symbol:
                count += 1
        if count == 2:
            for i in range(0, 3):
                cell = self.rows[i].cells[i]
                if cell.symbol == " ":
                    coords.append(cell.row_num[0] + 1)
                    coords.append(cell.col_num[0] + 1)
                    return coords
        return coords

    def get_secondary_diagonal_win_coordinates(self, symbol):
        count = 0
        row_idx = 0
        for i in range(2, -1, -1):
            cell = self.rows[row_idx].cells[i]
            row_idx += 1
            if cell.symbol == symbol:
                count += 1
        row_idx = 0
        coords = []
        if count == 2:
            for i in range(2, -1, -1):
                cell = self.rows[row_idx].cells[i]
                row_idx += 1
                if cell.symbol == " ":
                    coords.append(cell.row_num[0] + 1)
                    coords.append(cell.col_num[0] + 1)
                    return coords
        return coords


def create_board(input_str):
    rows = []
    for i in range(0, 3):
        start = i * 3
        end = start + 3
        row = create_row(row_num=i, input_str=input_str[start:end])
        rows.append(row)
    return GameBoard(rows)


def create_empty_board():
    rows = [create_empty_row(i) for i in range(0, 3)]
    return GameBoard(rows)
