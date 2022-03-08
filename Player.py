from InputHandler import handle_coordinates
from InputHandler import handle_int_coordinates
from Level import Level
import random
from enum import Enum
from StateChecker import check_game_state
from State import State


def get_minimax_coordinates(board, symbol, is_maximizing):
    best_score = -1000 if is_maximizing else 1000
    coords = []
    new_symbol = "O" if is_maximizing else "X"
    for i in range(0, 3):
        for j in range(0, 3):
            cell = board.rows[i].cells[j]
            if not cell.occupied:
                cell.symbol = symbol
                cell.occupied = True
                score = minimax(board, not is_maximizing, new_symbol)
                cell.symbol = " "
                cell.occupied = False
                if is_maximizing and score > best_score:
                    best_score = score
                    coords = [i + 1, j + 1]
                elif not is_maximizing and score < best_score:
                    best_score = score
                    coords = [i + 1, j + 1]
    return coords


def minimax(board, is_maximizing, symbol):
    state = check_game_state(board)
    if state == State.X_WINS:
        return 1
    elif state == State.O_WINS:
        return -1
    elif state == State.DRAW:
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(0, 3):
            for j in range(0, 3):
                cell = board.rows[i].cells[j]
                if not cell.occupied:
                    cell.symbol = symbol
                    cell.occupied = True
                    score = minimax(board, False, "O")
                    cell.symbol = " "
                    cell.occupied = False
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = 1000
        for i in range(0, 3):
            for j in range(0, 3):
                cell = board.rows[i].cells[j]
                if not cell.occupied:
                    cell.symbol = symbol
                    cell.occupied = True
                    score = minimax(board, True, "X")
                    cell.symbol = " "
                    cell.occupied = False
                    best_score = min(best_score, score)
        return best_score


class UserType(Enum):
    USER = 1
    COMP = 2


def get_win_coordinates(board, symbol):
    return board.get_win_coordinates(symbol)


def update_board(board, coordinates, symbol):
    board.update_cell(row_num=coordinates[0] - 1, col_num=coordinates[1] - 1, symbol=symbol)


def get_random_coordinates(board):
    coordinates = []
    while not coordinates:
        row_num = random.randint(1, 3)
        col_num = random.randint(1, 3)
        coordinates = handle_int_coordinates(row_num=row_num, col_num=col_num, board=board)
    return coordinates


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
        coordinates = get_random_coordinates(board)
        update_board(board, coordinates, self.symbol)

    def make_medium_move(self, board):
        coordinates = get_win_coordinates(board, self.symbol)
        if coordinates:
            update_board(board, coordinates, self.symbol)
        else:
            enemy_symbol = "O" if self.symbol == "X" else "X"
            coordinates = get_win_coordinates(board, enemy_symbol)
            if coordinates:
                update_board(board, coordinates, self.symbol)
            else:
                coordinates = get_random_coordinates(board)
                update_board(board, coordinates, self.symbol)

    def make_hard_move(self, board):
        if board.is_empty():
            coordinates = get_random_coordinates(board)
            update_board(board, coordinates, self.symbol)
        else:
            coordinates = get_minimax_coordinates(board, self.symbol, self.symbol == "X")
            update_board(board, coordinates, self.symbol)




