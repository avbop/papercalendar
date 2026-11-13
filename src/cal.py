from constants import *
from collections import defaultdict
from datetime import timedelta, date
from colors import Color
from icons import Icon
from util import *
from events import event
from weeks import week_event


class week:
    def __init__(
        self,
        id: date,
        e: week_event,
    ):
        self.id: date = week_key(id)
        self.title: str = e.title
        self.color: Color = e.color

    def filename(self):
        d = self.id.strftime("%Y-%m-%d")
        return f"{d}.jpg"

    def __str__(self):
        d = self.id.strftime("%Y-%m-%d")
        return f"Week of {d} ({self.title})"


class day:
    def __init__(self, id: date):
        self.id: date = id
        self.events: list[event] = []

    def __str__(self):
        return self.id.strftime("%Y-%m-%d")


class calendar:
    def __init__(self):
        self._weeks: dict[date, week] = dict()
        self._days: dict[date, day] = dict()

    def add_event(self, d: date, e: event | week_event):
        if isinstance(e, event):
            if d not in self._days:
                self._days[d] = day(d)
            self._days[d].events.append(e)
        else:
            d = week_key(d)
            self._weeks[d] = week(d, e)

    def get_week(self, id: date) -> week:
        id = week_key(id)
        return self._weeks.get(id, week(id, week_event("", Color.DEFAULT)))

    def get_day(self, id: date) -> day:
        return self._days.get(id, day(id))


def week_key(d: date) -> date:
    """Return the nearest Sunday that is <= d.

    >>> week_key(date(2026, 11, 12))
    datetime.date(2026, 11, 8)
    """
    while d.weekday() != Weekday.SUNDAY:
        d -= timedelta(days=1)
    return d
