from enum import Enum
import re
from colors import Color
from icons import Icon


class event:
    def __init__(self, title: str, color: Color, icon: Icon):
        self.title: str = title
        self.color: Color = color
        self.icon: Icon = icon

    def __str__(self) -> str:
        return self.title


def mem(base: event, *mems: event) -> event:
    """Combine events on the OP calendar such that other feasts are listed as memorials.
    >>> import lit_op
    >>> mem(lit_op.CO_SUN, lit_op.JOHN).title
    'Sunday in the Octave (II)\\nmem. St. John'
    >>> mem(lit_op.CO_SUN, lit_op.EMERENTIANA).title
    'Sunday in the Octave (II)\\nmem. St. Emerentiana'
    """
    ending = re.compile(r"\s+\([IVm]+\)$")
    title = base.title
    for m in mems:
        mtitle = re.sub(ending, "", m.title)
        title += f"\nmem. {mtitle}"
    return event(title, base.color, base.icon)


def comm(e: event) -> event:
    """Convert a memorial or optional memorial into an Advent or Lent commemoration.
    >>> import lit_no
    >>> comm(lit_no.PATRICK).color == Color.PURPLE
    True
    >>> comm(lit_no.PATRICK).title
    'St. Patrick (c)'
    """
    title = e.title.replace("(m)", "(c)")
    title = title.replace("(om)", "(c)")
    return event(title, Color.PURPLE, e.icon)


def anniversary(
    title: str, color: Color, icon: Icon, first_year: int, current_year: int
) -> event | None:
    dy = current_year - first_year
    if dy < 1:
        return None
    txt = ordinal_text(dy)
    return event(title.format(txt), color, icon)


def ordinal_text(i: int) -> str:
    """Return the English ordinal numeral and abbreviation.
    >>> ordinal_text(1)
    '1st'
    >>> ordinal_text(2)
    '2nd'
    >>> ordinal_text(3)
    '3rd'
    >>> ordinal_text(4)
    '4th'
    >>> ordinal_text(5)
    '5th'
    >>> ordinal_text(31)
    '31st'
    >>> ordinal_text(32)
    '32nd'
    >>> ordinal_text(33)
    '33rd'
    >>> ordinal_text(34)
    '34th'
    >>> ordinal_text(1023)
    '1023rd'
    >>> ordinal_text(1013)
    '1013th'
    """
    txt = f"{i}th"
    digits = i % 100
    if digits > 10 and digits < 20:
        txt = f"{i}th"
    else:
        digits = i % 10
        if digits == 1:
            txt = f"{i}st"
        elif digits == 2:
            txt = f"{i}nd"
        elif digits == 3:
            txt = f"{i}rd"
    return txt
