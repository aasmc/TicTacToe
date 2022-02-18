class Cell:
    def __init__(self, col_num, row_num, occupied=False, symbol=" "):
        self.col_num = col_num,
        self.row_num = row_num,
        self.occupied = occupied
        self.symbol = symbol

    def __str__(self):
        return self.symbol


def create_cell(symbol, col_num, row_num):
    occupied = symbol == "X" or symbol == "O"
    cell_symbol = symbol if symbol != "_" else " "
    return Cell(col_num=col_num, row_num=row_num, occupied=occupied, symbol=cell_symbol)
