from constants import *
from collections import defaultdict
from datetime import timedelta, date
from colors import Color
from icons import Icon
from util import *


class week_event:
    def __init__(self, title: str, color: Color):
        self.title = title
        self.color = color


class week:
    def __init__(
        self,
        id: date,
        e: week_event,
    ):
        self.id: date = _make_sun(id)
        self.title: str = e.title
        self.color: Color = e.color

    def filename(self):
        return self.id.strftime("%Y-%m-%d")

    def __str__(self):
        d = self.id.strftime("%Y-%m-%d")
        return f"Week of {d} ({self.title})"


class event:
    def __init__(self, title: str, color: Color, icon: Icon):
        self.title: str = title
        self.color: Color = color
        self.icon: Icon = icon

    def __str__(self) -> str:
        return self.title


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
            d = _make_sun(d)
            self._weeks[d] = week(d, e)

    def get_week(self, id: date) -> week:
        id = _make_sun(id)
        return self._weeks.get(id, week(id, week_event("", Color.DEFAULT)))

    def get_day(self, id: date) -> day:
        return self._days.get(id, day(id))


def _make_sun(d: date) -> date:
    """Return the nearest Sunday that is <= d.

    >>> _make_sun(date(2026, 11, 12))
    datetime.date(2026, 11, 8)
    """
    while d.weekday() != Weekday.SUNDAY:
        d -= timedelta(days=1)
    return d
