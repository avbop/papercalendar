from weeks import week_event
from events import event, mem
import lit_no_w, lit_no, lit_op, annual

YEAR = 2028

events: list[tuple[int, int, int, week_event | event]] = [
    (YEAR, 1, 1, lit_no.MOTHER_OF_GOD),
    (YEAR, 1, 2, lit_no_w.C2),
    (YEAR, 1, 2, lit_no.C_SUN_2),
    (YEAR, 5, 8, annual.pope_election(2025, YEAR)),
    (YEAR, 5, 18, annual.pope_inauguration(2025, YEAR)),
]
