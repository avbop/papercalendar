import data
from constants import *
from classes import calendar
from datetime import timedelta, date
from PIL import Image, ImageDraw, ImageOps, ImageColor, ImageText
import os
import multiprocessing
from colors import Color

TESTING = True
PREVIEW = True
PREVIEW_DATE = date(2027, 1, 9)


def _clean_rm(path):
    if os.path.exists(path) and not os.path.isdir(path):
        os.remove(path)
        return 1
    return 0


def setup_output(cal):
    exists = os.path.exists(OUT_DIR)
    isdir = os.path.isdir(OUT_DIR)
    if exists and not isdir:
        print(f"Error: {OUT_DIR} exists but is not a directory.")
        exit(1)
    if not exists:
        print(f"Making {OUT_DIR}/.")
        os.makedirs(OUT_DIR)


def generate_week(wk, cal):
    out = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(out)

    # Draw boxes for days.
    x = X_ORIGIN_TOP
    y = Y_ORIGIN_TOP + BORDER_OFFSET
    # upper right corner
    for i in range(5):
        if i not in [0, 4]:
            draw.line([x, y, x, y + DY], fill=BORDER_COLOUR, width=BORDER_WIDTH)
        if TESTING:
            draw.line([x, y - BORDER_OFFSET, x, HEIGHT // 2], fill="red", width=1)
        x += DX
    # lower left corner
    x = X_ORIGIN_BOTTOM
    y = Y_ORIGIN_BOTTOM + BORDER_OFFSET
    for i in range(5):
        if i not in [0, 4]:
            draw.line([x, y, x, y + DY], fill=BORDER_COLOUR, width=BORDER_WIDTH)
        if TESTING:
            draw.line([x, y - BORDER_OFFSET, x, HEIGHT - MARGIN], fill="red", width=1)
        x -= DX

    # Draw each day.
    x = X_ORIGIN_TOP
    y = Y_ORIGIN_TOP
    for i in range(4):
        day = cal.get_day(wk.id + timedelta(days=i))
        draw_day(day, x, y, out)
        x += DX
    x = X_ORIGIN_BOTTOM
    y = Y_ORIGIN_BOTTOM
    for i in range(7, 3, -1):
        x -= DX
        if i == 7:
            mid_x = x + DX // 2
            start = wk.id
            end = wk.id + timedelta(days=6)
            txt = wk.title
            dtxt = ImageText.Text(txt, font=EVENT_FONT)
            draw.text((mid_x, y), dtxt, fill=wk.color, anchor="ma")
            left, top, right, bottom = dtxt.get_bbox((mid_x, y), anchor="ma")
            dy = bottom + ICON_TEXT_MARGIN
            if start.month == end.month:
                txt = f"{start.day} – {end.day} {end.strftime("%B")}"
            else:
                txt = f"{start.day} {start.strftime("%B")} – {end.day} {end.strftime("%B")}"
            dtxt = ImageText.Text(txt, font=EVENT_FONT)
            draw.text((mid_x, dy), dtxt, fill=Color.DEFAULT, anchor="ma")
        else:
            day = cal.get_day(wk.id + timedelta(days=i))
            draw_day(day, x, y, out)

    # Output.
    if TESTING:
        # Debug info.
        draw.line([WIDTH // 2, 0, WIDTH // 2, HEIGHT], fill="red")
        draw.line([0, HEIGHT // 2, WIDTH, HEIGHT // 2], fill="red")
        # Preview.
    if PREVIEW:
        out.show()
    out.save(OUT_FMT.format(wk.filename()))


def draw_day(d, x_base, y_base, img):
    draw = ImageDraw.Draw(img)
    mid_x = x_base + DX // 2
    x = x_base + TEXT_MARGIN
    y = y_base + TEXT_MARGIN
    num = ImageText.Text(str(d.id.day), font=DAY_FONT)
    dow = ImageText.Text(d.id.strftime("%A"), font=DAY_FONT)
    draw.text((x, y), num, fill=Color.DEFAULT, anchor="la")
    draw.text((mid_x, y), dow, fill=Color.DEFAULT, anchor="ma")
    left, top, right, bottom = num.get_bbox((x, y), anchor="la")
    y = bottom + TEXT_MARGIN
    for e in d.events:
        y, right = draw_text_with_icon(e.title, e.icon, e.color, x, y, img)


def draw_text_with_icon(text, icon, color, x, y, img):
    draw = ImageDraw.Draw(img)
    icon = Image.open(ICON_DIR + icon)
    icon = ImageOps.pad(icon, (ICON_WIDTH, ICON_HEIGHT))
    img.paste(icon, (x, y))
    x += ICON_WIDTH + ICON_TEXT_MARGIN
    t = ImageText.Text(text, font=EVENT_FONT)
    draw.text((x, y), t, fill=color, anchor="la")
    left, top, right, bottom = t.get_bbox((x, y), anchor="la")
    return int(max(bottom, y + ICON_HEIGHT) + ICON_TEXT_MARGIN), right


def color_image(img, color):
    img = img.convert("RGB")
    c = ImageColor.getrgb(color)
    pixels = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pixels[x, y] != (255, 255, 255):
                pixels[x, y] = c
    return img


def main():
    cal = calendar()
    data.add_events(cal, [2027])
    if PREVIEW:
        generate_week(cal.get_week(PREVIEW_DATE), cal)
        exit(0)
    setup_output(cal)
    pool = multiprocessing.Pool(os.cpu_count())
    for w in cal.week_keys():
        pool.apply_async(generate_week, (cal.get_week(w), cal))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
