from weeks import week_event, Week
from events import event, Event, mem

YEAR = 2028

events: list[tuple[int, int, int, Week | Event | week_event | event]] = [
    (YEAR, 1, 1, Event.MOTHER_OF_GOD),
    (YEAR, 1, 2, Week.C2),
    (YEAR, 1, 2, Event.C_SUN_2),
]
