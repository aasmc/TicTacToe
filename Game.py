from GameBoard import create_empty_board
from State import State
from StateChecker import check_game_state
from Player import Player
from Player import UserType
from Level import Level
from Level import from_string
from State import print_state


def handle_command(command_str):
    commands = command_str.split()
    if commands[0] == "exit":
        return []
    elif len(commands) < 3:
        raise ValueError("Bad parameters!")
    if commands[1] == "user":
        comp_level = from_string(commands[2])
        return Player("X", UserType.USER, Level.UNDEFINED), Player("O", UserType.COMP, comp_level)
    elif commands[2] == "user":
        comp_level = from_string(commands[1])
        return Player("X", UserType.COMP, comp_level), Player("O", UserType.USER, Level.UNDEFINED)
    else:
        comp_level_one = from_string(commands[1])
        comp_level_two = from_string(commands[2])
        return Player("X", UserType.COMP, comp_level_one), Player("O", UserType.COMP, comp_level_two)


def play_game():
    while True:
        try:
            players = handle_command(input("Input command: "))
            if not players:
                break
            board = create_empty_board()
            print(board)
            first_player_move = True
            first_player = players[0]
            second_player = players[1]
            while True:
                if first_player_move:
                    first_player.make_move(board)
                else:
                    second_player.make_move(board)
                first_player_move = not first_player_move
                print(board)
                state = check_game_state(board)
                if state == State.O_WINS or state == State.X_WINS or state == State.DRAW:
                    break
            print_state(state)
        except ValueError as e:
            print(e)
