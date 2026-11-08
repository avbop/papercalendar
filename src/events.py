from classes import event
from colors import Color
from icons import Icon
from enum import Enum


class Event(Enum):
    MOTHER_OF_GOD = event("Mary, the Mother of God (s)", Color.WHITE, Icon.NO)
    GREGORY_BASIL = event(
        "Saints Basil the Great and Gregory Nazianzen (m)", Color.WHITE, Icon.NO
    )
    EPIPHANY = event("Epiphany of the Lord (s)", Color.WHITE, Icon.NO)
