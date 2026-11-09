from weeks import Week
from events import Event, op_mem
from classes import week_event, event

YEAR = 2026

# Only include events that overlap with the week of 2027-01-01.
events: list[tuple[int, int, int, Week | Event | week_event | event]] = [
    (YEAR, 12, 27, Week.C2),
    (YEAR, 12, 27, Event.HOLY_FAMILY),
    (YEAR, 12, 27, op_mem(Event.OP_C_OCT_SUN, [Event.OP_JOHN_EVANGELIST])),
    (YEAR, 12, 28, Event.HOLY_INNOCENTS),
    (YEAR, 12, 28, op_mem(Event.OP_HOLY_INNOCENTS, [Event.OP_C_OCT])),
    (YEAR, 12, 29, Event.C_OCT_5),
    (YEAR, 12, 29, Event.THOMAS_BECKET),
    (YEAR, 12, 29, op_mem(Event.OP_C_OCT, [Event.OP_THOMAS_BECKET])),
    (YEAR, 12, 30, Event.C_OCT_6),
    (YEAR, 12, 30, Event.OP_C_OCT),
    (YEAR, 12, 31, Event.C_OCT_7),
    (YEAR, 12, 31, Event.SYLVESTER),
    (YEAR, 12, 31, op_mem(Event.OP_C_OCT, [Event.OP_SYLVESTER])),
]
