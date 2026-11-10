from datetime import date
import cal
from events import event, Event
from weeks import week_event, Week
import sys
lazy import data2026
lazy import data2027
lazy import data2028


def add_events(c: cal.calendar, year: int):
    es: list[tuple[date, event | week_event]] = []
    pending: list[
        tuple[
            int,
            int,
            int,
            Week | Event | event | week_event,
        ]
    ] = []
    if year == 2026:
        pending = data2026.events
    elif year == 2027:
        pending = data2027.events
    elif year == 2028:
        pending = data2028.events
    for e in pending:
        d = date(e[0], e[1], e[2])
        if isinstance(e[3], (Week, Event)):
            es.append((d, e[3].value))
        else:
            es.append((d, e[3]))
    try:
        from local_config import customize_events

        customize_events(es, year)
    except:
        print("Warning: unable to load local_config.py.", file=sys.stderr)
    for e in es:
        c.add_event(e[0], e[1])
