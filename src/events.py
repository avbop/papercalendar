from classes import event
from colors import Color
from icons import Icon
from enum import Enum
import re


class Event(Enum):
    MOTHER_OF_GOD = event("Mary, the Mother of God (s)", Color.WHITE, Icon.NO)
    GREGORY_BASIL = event(
        "Ss. Basil the Great and Gregory Nazianzen (m)", Color.WHITE, Icon.NO
    )
    EPIPHANY = event("Epiphany of the Lord (s)", Color.WHITE, Icon.NO)
    HOLY_FAMILY = event("Holy Family (f)", Color.WHITE, Icon.NO)
    HOLY_INNOCENTS = event("Holy Innocents (f)", Color.RED, Icon.NO)
    C_OCT_5 = event("Fifth Day in the Octave", Color.WHITE, Icon.NO)
    C_OCT_6 = event("Sixth Day in the Octave", Color.WHITE, Icon.NO)
    C_OCT_7 = event("Seventh Day in the Octave", Color.WHITE, Icon.NO)
    THOMAS_BECKET = event("St. Thomas Becket (om)", Color.RED, Icon.NO)
    SYLVESTER = event("St. Sylvester I (om)", Color.WHITE, Icon.NO)

    OP_C_OCT = event("Octave (II)", Color.WHITE, Icon.OP)
    OP_C_OCT_SUN = event("Sunday in the Octave (II)", Color.WHITE, Icon.OP)
    OP_C_OCT_8 = event("Octave Day of the Nativity (I)", Color.WHITE, Icon.OP)
    OP_JOHN_EVANGELIST = event("St. John (I)", Color.WHITE, Icon.OP)
    OP_HOLY_INNOCENTS = event("Holy Innocents (II)", Color.RED, Icon.OP)
    OP_THOMAS_BECKET = event("St. Thomas Becket (III)", Color.RED, Icon.OP)
    OP_SYLVESTER = event("St. Sylvester I (III)", Color.WHITE, Icon.OP)
    OP_BVM = event("Our Lady on Saturday (IV)", Color.WHITE, Icon.OP)
    OP_HOLY_NAME = event("Most Holy Name of Jesus (II)", Color.WHITE, Icon.OP)


def op_mem(base: Event, mems: list[Event]) -> event:
    """Combine events on the OP calendar such that other feasts are listed as memorials.
    >>> op_mem(Event.OP_C_OCT_SUN, [Event.OP_JOHN_EVANGELIST]).title
    'Sunday in the Octave (II)\\nmem. St. John'
    """
    ending = re.compile(r"\s+\(I+V?\)$")
    title = base.value.title
    for m in mems:
        mtitle = re.sub(ending, "", m.value.title)
        title += f"\nmem. {mtitle}"
    return event(title, base.value.color, base.value.icon)
