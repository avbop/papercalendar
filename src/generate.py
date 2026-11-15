import argparse
import multiprocessing
import os
import sys
from datetime import date, timedelta
from functools import partial

from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps, ImageText

import data
from cal import calendar, week, week_key
from colors import Color


def setup_output(args):
    exists = os.path.exists(args.outdir)
    isdir = os.path.isdir(args.outdir)
    if exists and not isdir:
        print(f"Error: '{args.outdir}' exists but is not a directory.")
        sys.exit(1)
    if not exists:
        os.makedirs(args.outdir)
        if args.debug:
            pid = os.getpid()
            print(f"{pid}: Made '{args.outdir}/'.")


def generate_week(wk, cal, args):
    out = Image.new("RGB", (args.width, args.height), "white")
    draw = ImageDraw.Draw(out)

    # Draw boxes for days.
    x = args.x_origin_top
    y = args.y_origin_top + args.border_offset
    # upper right corner
    for i in range(5):
        if i not in [0, 4]:
            draw.line(
                [x, y, x, y + args.dy], fill=Color.BORDER, width=args.border_width
            )
        if args.debug:
            draw.line(
                [x, y - args.border_offset, x, args.height // 2],
                fill=Color.DEBUG,
                width=1,
            )
        x += args.dx
    # lower left corner
    x = args.x_origin_bottom
    y = args.y_origin_bottom + args.border_offset
    for i in range(5):
        if i not in [0, 4]:
            draw.line(
                [x, y, x, y + args.dy], fill=Color.BORDER, width=args.border_width
            )
        if args.debug:
            draw.line(
                [x, y - args.border_offset, x, args.height - args.margin],
                fill=Color.DEBUG,
                width=1,
            )
        x -= args.dx

    # Draw each day.
    x = args.x_origin_top
    y = args.y_origin_top
    for i in range(4):
        day = cal.get_day(wk.id + timedelta(days=i))
        draw_day(day, x, y, out, args)
        x += args.dx
    x = args.x_origin_bottom
    y = args.y_origin_bottom
    for i in range(7, 3, -1):
        x -= args.dx
        if i == 7:  # TODO: refactor into separate function.
            mid_x = x + args.dx // 2
            start = wk.id
            end = wk.id + timedelta(days=6)
            txt = wk.title
            dtxt = ImageText.Text(txt, font=args.event_font)
            draw.text((mid_x, y), dtxt, fill=wk.color, anchor="ma")
            _left, _top, _right, bottom = dtxt.get_bbox((mid_x, y), anchor="ma")
            dy = bottom + args.icon_text_margin
            if start.month == end.month:
                txt = f"{start.day} – {end.day} {end.strftime('%B')}"
            else:
                txt = f"{start.day} {start.strftime('%B')} – {end.day} {end.strftime('%B')}"
            dtxt = ImageText.Text(txt, font=args.event_font)
            draw.text((mid_x, dy), dtxt, fill=Color.DEFAULT, anchor="ma")
        else:
            day = cal.get_day(wk.id + timedelta(days=i))
            draw_day(day, x, y, out, args)

    if args.debug:
        draw.line([args.width // 2, 0, args.width // 2, args.height], fill=Color.RED)
        draw.line([0, args.height // 2, args.width, args.height // 2], fill=Color.RED)

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
    mid_x = x_base + args.dx // 2
    x = x_base + args.text_margin
    y = y_base + args.text_margin
    num = ImageText.Text(str(d.id.day), font=args.day_font)
    dow = ImageText.Text(d.id.strftime("%A"), font=args.day_font)
    draw.text((x, y), num, fill=Color.DEFAULT, anchor="la")
    draw.text((mid_x, y), dow, fill=Color.DEFAULT, anchor="ma")
    _left, _top, _right, bottom = num.get_bbox((x, y), anchor="la")
    y = bottom + args.text_margin
    for e in d.events:
        y, _right = draw_text_with_icon(e.title, e.icon, e.color, x, y, img, args)


# TODO: automatically wrap text.
def draw_text_with_icon(text, icon, color, x, y, img, args):
    draw = ImageDraw.Draw(img)
    icon = Image.open(os.path.join(args.assets, icon))
    icon = ImageOps.pad(icon, (args.icon_width, args.icon_height))
    if args.color_icons:
        icon = color_image(icon, color)
    img.paste(icon, (x, y))
    x += args.icon_width + args.icon_text_margin
    t = ImageText.Text(text, font=args.event_font)
    draw.text((x, y), t, fill=color, anchor="la")
    _left, _top, right, bottom = t.get_bbox((x, y), anchor="la")
    return int(max(bottom, y + args.icon_height) + args.icon_text_margin), right


def color_image(img, color):
    img = img.convert("RGB")
    c = ImageColor.getrgb(color)
    pixels = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pixels[x, y] != (255, 255, 255):
                pixels[x, y] = c
    return img


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Generate a printable calendar, one page per week."
    )
    p.add_argument(
        "-s",
        "--start",
        type=date.fromisoformat,
        help="The starting date. Default: today.",
    )
    p.add_argument(
        "-e", "--end", type=date.fromisoformat, help="The ending date. Default: START."
    )
    p.add_argument(
        "-o",
        "--outdir",
        type=str,
        help="The directory to write to. Default: out.",
        default="out",
    )
    p.add_argument(
        "-a",
        "--assets",
        type=str,
        help="The directory containing the icon and font files. Default: assets.",
        default="assets",
    )
    p.add_argument(
        "--color-icons",
        help="Display icons in the same color as the accompanying text. Default: false.",
        action="store_true",
    )
    p.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="The DPI (pixels per inch) of the output file. Default: 300.",
    )
    p.add_argument(
        "--page-width",
        type=float,
        default=11.7,
        help="The width (inches) of the output file. Default: 11.7.",
    )
    p.add_argument(
        "--page-height",
        type=float,
        default=8.27,
        help="The height (inches) of the output file. Default: 8.27.",
    )
    p.add_argument(
        "--page-margin",
        type=float,
        default=0.2,
        help="The margin (inches) of the output file. Default: 0.2.",
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
    args.width = int(args.dpi * args.page_width)
    args.height = int(args.dpi * args.page_height)
    args.margin = int(args.dpi * args.page_margin)
    args.border_offset = int(args.height * 0.05)
    args.x_origin_top = args.margin
    args.y_origin_top = args.margin
    args.x_origin_bottom = args.width - args.margin
    args.y_origin_bottom = args.height // 2
    args.dx = (args.width - args.x_origin_top - args.margin) // 4
    args.dy = (args.height // 2) - args.margin - 2 * args.border_offset
    args.week_font = ImageFont.truetype(os.path.join(args.assets, "bold.ttf"), 100)
    args.day_font = ImageFont.truetype(os.path.join(args.assets, "regular.ttf"), 60)
    args.event_font = ImageFont.truetype(os.path.join(args.assets, "regular.ttf"), 40)
    args.icon_width = 50
    args.icon_height = args.icon_width
    args.icon_text_margin = args.icon_width // 3
    args.border_width = 5
    args.text_margin = 40
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
