from classes import calendar
from weeks import Week
from events import Event
from datetime import date
from classes import event, week_event
import sys
lazy import data2026
lazy import data2027


def add_events(c: calendar, years: list[int]):
    events: list[tuple[date, event | week_event]] = []
    pending: list[tuple[int, int, int, Week | Event | event | week_event]] = []
    for y in years:
        if y == 2026:
            pending = data2026.events
        elif y == 2027:
            pending = data2027.events
        for e in pending:
            d = date(e[0], e[1], e[2])
            if isinstance(e[3], (Week, Event)):
                events.append((d, e[3].value))
            else:
                events.append((d, e[3]))
    try:
        from local_config import customize_events

        customize_events(events, years)
    except:
        print("Warning: unable to load local_config.py.", file=sys.stderr)
    for e in events:
        c.add_event(e[0], e[1])
