from classes import week_event
from colors import Color
from enum import Enum


class Week(Enum):
    C1 = week_event("First Week of Christmas", Color.WHITE)
    C2 = week_event("Second Week of Christmas", Color.WHITE)
    OT1 = week_event("First Week of Ordinary Time", Color.GREEN)
    OT2 = week_event("Second Week of Ordinary Time", Color.GREEN)
    OT3 = week_event("Third Week of Ordinary Time", Color.GREEN)
