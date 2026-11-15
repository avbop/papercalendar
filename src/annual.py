from colors import Color
from events import anniversary, event
from icons import Icon


def pope_election(start: int, current: int) -> event:
    """
    >>> pope_election(2025, 2026).title
    '1st anniversary of the election of the Supreme Pontiff'
    """
    a = anniversary(
        "{} anniversary of the election of the Supreme Pontiff",
        Color.GENERIC,
        Icon.GENERIC,
        start,
        current,
    )
    if a is not None:
        return a
    else:
        return event("Election of the Supreme Pontiff", Color.GENERIC, Icon.GENERIC)


def pope_inauguration(start: int, current: int) -> event:
    """
    >>> pope_inauguration(2025, 2026).title
    '1st anniversary of the inauguration of the ministry of the Supreme Pontiff'
    """
    a = anniversary(
        "{} anniversary of the inauguration of the ministry of the Supreme Pontiff",
        Color.GENERIC,
        Icon.GENERIC,
        start,
        current,
    )
    if a is not None:
        return a
    else:
        return event(
            "Inauguration of the ministry of the Supreme Pontiff",
            Color.GENERIC,
            Icon.GENERIC,
        )
