import argparse
from datetime import timedelta, date
from functools import partial
import multiprocessing
import os
from PIL import Image, ImageDraw, ImageOps, ImageColor, ImageText
import data
from cal import calendar, week_key, week
from colors import Color
from constants import *


def setup_output(args):
    exists = os.path.exists(args.outdir)
    isdir = os.path.isdir(args.outdir)
    if exists and not isdir:
        print(f"Error: '{args.outdir}' exists but is not a directory.")
        exit(1)
    if not exists:
        os.makedirs(args.outdir)
        if args.debug:
            pid = os.getpid()
            print(f"{pid}: Made '{args.outdir}/'.")


def generate_week(wk, cal, args):
    out = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(out)

    # Draw boxes for days.
    x = X_ORIGIN_TOP
    y = Y_ORIGIN_TOP + BORDER_OFFSET
    # upper right corner
    for i in range(5):
        if i not in [0, 4]:
            draw.line([x, y, x, y + DY], fill=Color.BORDER, width=BORDER_WIDTH)
        if args.debug:
            draw.line([x, y - BORDER_OFFSET, x, HEIGHT // 2], fill=Color.DEBUG, width=1)
        x += DX
    # lower left corner
    x = X_ORIGIN_BOTTOM
    y = Y_ORIGIN_BOTTOM + BORDER_OFFSET
    for i in range(5):
        if i not in [0, 4]:
            draw.line([x, y, x, y + DY], fill=Color.BORDER, width=BORDER_WIDTH)
        if args.debug:
            draw.line(
                [x, y - BORDER_OFFSET, x, HEIGHT - MARGIN], fill=Color.DEBUG, width=1
            )
        x -= DX

    # Draw each day.
    x = X_ORIGIN_TOP
    y = Y_ORIGIN_TOP
    for i in range(4):
        day = cal.get_day(wk.id + timedelta(days=i))
        draw_day(day, x, y, out, args)
        x += DX
    x = X_ORIGIN_BOTTOM
    y = Y_ORIGIN_BOTTOM
    for i in range(7, 3, -1):
        x -= DX
        if i == 7:  # TODO: refactor into separate function.
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
            draw_day(day, x, y, out, args)

    if args.debug:
        draw.line([WIDTH // 2, 0, WIDTH // 2, HEIGHT], fill=Color.RED)
        draw.line([0, HEIGHT // 2, WIDTH, HEIGHT // 2], fill=Color.RED)

    if args.preview:
        out.show()
    else:
        filename = os.path.join(args.outdir, wk.filename())
        out.save(filename)
        if args.debug:
            pid = os.getpid()
            print(f"{pid}: Wrote '{filename}'.")


def draw_day(d, x_base, y_base, img, args):
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
        y, right = draw_text_with_icon(e.title, e.icon, e.color, x, y, img, args)


# TODO: automatically wrap text.
def draw_text_with_icon(text, icon, color, x, y, img, args):
    draw = ImageDraw.Draw(img)
    icon = Image.open(ICON_DIR + icon)
    icon = ImageOps.pad(icon, (ICON_WIDTH, ICON_HEIGHT))
    if args.color_icons:
        icon = color_image(icon, color)
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


# TODO: convert stuff from constants into args with default values.
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate a printable calendar, one page per week."
    )
    p.add_argument("-s", "--start", type=date.fromisoformat, help="The starting date.")
    p.add_argument("-e", "--end", type=date.fromisoformat, help="The ending date.")
    p.add_argument(
        "-o", "--outdir", type=str, help="The directory to write to.", default="out"
    )
    p.add_argument(
        "-c",
        "--color-icons",
        help="Display icons in the same color as the accompanying text.",
        action="store_true",
    )
    p.add_argument(
        "-d", "--debug", help="Print debug information.", action="store_true"
    )
    p.add_argument(
        "-p", "--preview", help="Preview first generated image.", action="store_true"
    )
    args = p.parse_args()
    if args.start is None:
        args.start = date.today()
    if args.end is None:
        args.end = args.start
    args.start = week_key(args.start)
    return args


def main():
    args = parse_args()
    if not args.preview:
        setup_output(args)

    # Load the calendar data here to avoid multiprocessing issues.
    cal = calendar()
    years: set[int] = set()
    d: date = args.start
    while d <= args.end + timedelta(days=7):
        if d.year not in years:
            data.add_events(cal, d.year)
            years.add(d.year)
            if args.debug:
                pid = os.getpid()
                print(f"{pid}: Loaded data for {d.year}.")
        d += timedelta(days=1)

    if args.preview:
        if args.debug:
            pid = os.getpid()
            print(f"{pid}: Previewing week {args.start}.")
        generate_week(cal.get_week(args.start), cal, args)
    else:
        weeks: list[week] = []
        d: date = args.start
        while d <= args.end:
            weeks.append(cal.get_week(d))
            d += timedelta(days=7)
        with multiprocessing.Pool() as pool:
            pool.map(partial(generate_week, cal=cal, args=args), weeks)
    if args.debug:
        pid = os.getpid()
        print(f"{pid}: Done.")


if __name__ == "__main__":
    main()
