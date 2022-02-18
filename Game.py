from GameBoard import create_board
from State import print_state
from StateChecker import check_game_state
from InputHandler import  handle_coordinates


def play_game():
    board_string = input("Enter the cells: ")
    board = create_board(board_string)
    print(board)
    coordinates = []
    while not coordinates:
        coord_str = input("Enter the coordinates: ")
        coordinates = handle_coordinates(coord_str, board)
    symbol = board.get_next_player()
    board.update_cell(row_num=coordinates[0] - 1, col_num=coordinates[1] - 1, symbol=symbol)
    print(board)
    state = check_game_state(board)
    print_state(state)