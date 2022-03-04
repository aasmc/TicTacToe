from InputHandler import handle_coordinates
from InputHandler import handle_int_coordinates
from Level import Level
import random
from enum import Enum


class UserType(Enum):
    USER = 1
    COMP = 2


class Player:

    def __init__(self, symbol, user_type, level):
        self.symbol = symbol
        self.user_type = user_type
        self.level = level

    def make_move(self, board):
        if self.user_type == UserType.USER:
            self.make_user_move(board)
        else:
            self.make_computer_move(board)

    def make_user_move(self, board):
        coordinates = []
        while not coordinates:
            coord_str = input("Enter the coordinates: ")
            coordinates = handle_coordinates(coord_str, board)
        board.update_cell(row_num=coordinates[0] - 1, col_num=coordinates[1] - 1, symbol=self.symbol)

    def make_computer_move(self, board):
        move_str = 'Making move level'
        if self.level == Level.EASY:
            move_str = f'{move_str} "easy"'
            self.make_easy_move(board)
        elif self.level == Level.MEDIUM:
            move_str = f'{move_str} "medium"'
            self.make_medium_move(board)
        elif self.level == Level.HARD:
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
