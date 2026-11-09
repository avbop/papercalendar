from weeks import Week
from events import Event
from classes import week_event, event

YEAR = 2027

# TODO: finish adding events
events: list[tuple[int, int, int, Week | Event | week_event | event]] = [
    (YEAR, 1, 1, Event.MOTHER_OF_GOD),
    (YEAR, 1, 1, Event.OP_C_OCT_SUN),
    (YEAR, 1, 2, Event.GREGORY_BASIL),
    (YEAR, 1, 2, Event.OP_BVM),
    (YEAR, 1, 3, Week.C3),
    (YEAR, 1, 6, Event.EPIPHANY),
    (YEAR, 1, 10, Week.OT1),
    (YEAR, 1, 17, Week.OT2),
    (YEAR, 1, 24, Week.OT3),
]
