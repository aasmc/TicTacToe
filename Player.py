from InputHandler import handle_coordinates
from InputHandler import handle_int_coordinates
from Level import Level
import random


class Player:

    def __init__(self, symbol, is_user):
        self.symbol = symbol
        self.is_user = is_user

    def make_user_move(self, board):
        coordinates = []
        while not coordinates:
            coord_str = input("Enter the coordinates: ")
            coordinates = handle_coordinates(coord_str, board)
        board.update_cell(row_num=coordinates[0] - 1, col_num=coordinates[1] - 1, symbol=self.symbol)

    def make_computer_move(self, level, board):
        move_str = 'Making move level'
        if level == Level.EASY:
            move_str = f'{move_str} "easy"'
            self.make_easy_move(board)
        elif level == Level.MEDIUM:
            move_str = f'{move_str} "medium"'
            self.make_medium_move(board)
        elif level == Level.HARD:
            move_str = f'{move_str} "hard"'
            self.make_hard_move(board)
        print(move_str)

    def make_easy_move(self, board):
        coordinates = []
        while not coordinates:
            row_num = random.randint(1, 3)
            col_num = random.randint(1, 3)
            coordinates = handle_int_coordinates(row_num=row_num, col_num=col_num, board=board)
        board.update_cell(row_num=coordinates[0] - 1, col_num=coordinates[1] - 1, symbol=self.symbol)

    def make_medium_move(self, board):
        pass

    def make_hard_move(self, board):
        pass
