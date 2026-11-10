from weeks import Week
from events import Event
from classes import week_event, event

YEAR = 2028

events: list[tuple[int, int, int, Week | Event | week_event | event]] = [
    (YEAR, 1, 1, Event.MOTHER_OF_GOD),
    (YEAR, 1, 2, Week.C2),
    (YEAR, 1, 2, Event.C_SUN_2),
]
