from enum import StrEnum


# See https://www.color-hex.com/color-palette/82283.
class Color(StrEnum):
    WHITE = "#806202"
    BLACK = "black"
    PURPLE = "#800080"
    RED = "#d80707"
    GREEN = "#186420"
    PINK = "#fa2dec"
    BIRTHDAY = "#1457c4"  # blue
    WEDDING = PINK
    DEATH = BLACK
    GENERIC = BLACK
    DEFAULT = BLACK
    DEBUG = "red"
    BORDER = "#dddddd"
