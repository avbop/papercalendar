import math
from PIL import ImageFont

# page size
_DPI = 300  # px/in
_PAGE_WIDTH = 11.7  # in
_PAGE_HEIGHT = 8.27  # in
WIDTH = int(_DPI * _PAGE_WIDTH)  # px
HEIGHT = int(_DPI * _PAGE_HEIGHT)  # px
MARGIN = int(0.2 * _DPI)  # in * px/in

# week info formatting
WEEK_FONT = ImageFont.truetype("assets/font/Charter Bold.ttf", 100)
WEEK_INFO_Y = 250

# day info formatting
BORDER_WIDTH = 5
BORDER_OFFSET = int(HEIGHT * 0.05)
TEXT_MARGIN = 40
DAY_FONT = ImageFont.truetype("assets/font/Charter Regular.ttf", 60)
EVENT_FONT = ImageFont.truetype("assets/font/Charter Regular.ttf", 40)

# spacing
X_ORIGIN_TOP = MARGIN
Y_ORIGIN_TOP = MARGIN
X_ORIGIN_BOTTOM = WIDTH - MARGIN
Y_ORIGIN_BOTTOM = HEIGHT // 2
DX = (WIDTH - X_ORIGIN_TOP - MARGIN) // 4
DY = (HEIGHT // 2) - MARGIN - 2 * BORDER_OFFSET

ICON_WIDTH = 50
ICON_HEIGHT = ICON_WIDTH
ICON_TEXT_MARGIN = ICON_HEIGHT // 3
ICON_DIR = "assets/icon/"
