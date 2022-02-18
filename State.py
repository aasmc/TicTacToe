from enum import Enum


class State(Enum):
    NOT_FINISHED = 1
    DRAW = 2
    X_WINS = 3
    O_WINS = 4
    UNDEFINED = 5


def print_state(state):
    if state == State.DRAW:
        print("Draw")
    elif state == State.O_WINS:
        print("O wins")
    elif state == State.X_WINS:
        print("X wins")
    elif state == State.NOT_FINISHED:
        print("Game not finished")
    else:
        raise ValueError("Incorrect game state")
