from enum import Enum


class Level(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    UNDEFINED = 4


def from_string(level_str):
    if level_str == "easy":
        return Level.EASY
    elif level_str == "medium":
        return Level.MEDIUM
    elif level_str == "hard":
        return Level.HARD
    else:
        raise ValueError("Incorrect Level")
