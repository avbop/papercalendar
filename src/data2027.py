from weeks import Week
from events import Event

YEAR = 2027

events: list[tuple[int, int, int, Week | Event]] = [
    (YEAR, 1, 3, Week.C2),
    (YEAR, 1, 10, Week.OT1),
    (YEAR, 1, 17, Week.OT2),
    (YEAR, 1, 24, Week.OT3),
    (YEAR, 1, 6, Event.EPIPHANY),
    (YEAR, 1, 1, Event.MOTHER_OF_GOD),
    (YEAR, 1, 2, Event.GREGORY_BASIL),
]
