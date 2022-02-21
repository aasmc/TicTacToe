from GameBoard import create_empty_board
from State import print_state
from State import State
from StateChecker import check_game_state
from Player import Player
from Level import Level


def play_game():
    board = create_empty_board()
    print(board)
    user_player = Player(symbol="X", is_user=True)
    comp_player = Player(symbol="O", is_user=False)
    is_user_turn = True
    while True:
        if is_user_turn:
            user_player.make_user_move(board)
        else:
            comp_player.make_computer_move(Level.EASY, board)
        is_user_turn = not is_user_turn
        print(board)
        state = check_game_state(board)
        if state == State.O_WINS or state == State.X_WINS:
            break
    print_state(state)
