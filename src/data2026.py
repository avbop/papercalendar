from weeks import week_event
from events import event, mem
import lit_no_w, lit_no, lit_op, annual

YEAR = 2026

# Only include events that overlap with the week of 2027-01-01.
events: list[tuple[int, int, int, week_event | event]] = [
    (YEAR, 12, 27, lit_no_w.C2),
    (YEAR, 12, 27, lit_no.HOLY_FAMILY),
    (YEAR, 12, 27, mem(lit_op.CO_SUN, lit_op.JOHN)),
    (YEAR, 12, 28, lit_no.HOLY_INNOCENTS),
    (YEAR, 12, 28, mem(lit_op.HOLY_INNOCENTS, lit_op.CO)),
    (YEAR, 12, 29, lit_no.CO),
    (YEAR, 12, 29, lit_no.THOMAS_BECKET),
    (YEAR, 12, 29, mem(lit_op.CO, lit_op.THOMAS_BECKET)),
    (YEAR, 12, 30, lit_no.CO),
    (YEAR, 12, 30, lit_op.CO),
    (YEAR, 12, 31, lit_no.CO),
    (YEAR, 12, 31, lit_no.SYLVESTER),
    (YEAR, 12, 31, mem(lit_op.CO, lit_op.SYLVESTER)),
    (YEAR, 5, 8, annual.pope_election(2025, YEAR)),
    (YEAR, 5, 18, annual.pope_inauguration(2025, YEAR)),
]
