# ==========================================================
# SOAL PENJUMLAHAN 4 : 2 banana + 2 banana =
# ==========================================================

import cairo
from banana_cairo import draw_banana

# ==========================================================
# Fungsi simbol (+ dan =)
# ==========================================================
def draw_symbol(ctx, text, x, y):
    ctx.save()

    ctx.set_source_rgb(0, 0, 0)
    ctx.select_font_face(
        "Arial",
        cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_BOLD
    )
    ctx.set_font_size(180)

    (tx, ty, w, h, dx, dy) = ctx.text_extents(text)
    ctx.move_to(x - w/2, y + h/2)

    ctx.text_path(text)
    ctx.set_line_width(8)
    ctx.stroke_preserve()

    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    ctx.restore()


# ==========================================================
# Barisan buah banana yang center
# ==========================================================
def draw_row(ctx, fn, count, cx, y):
    spacing = 260
    total = (count - 1) * spacing
    start = cx - total / 2

    for i in range(count):
        fn(ctx, start + i * spacing, y, 0.33)


# ==========================================================
# Generator file PNG soal
# ==========================================================
def make():
    width, height = 1600, 700

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # background transparent
    ctx.set_source_rgba(0,0,0,0)
    ctx.paint()

    y = 350

    # 2 banana
    draw_row(ctx, draw_banana, 2, 350, y)

    # +
    draw_symbol(ctx, "+", 700, y)

    # 2 banana
    draw_row(ctx, draw_banana, 2, 1050, y)

    # =
    draw_symbol(ctx, "=", 1400, y)

    surface.write_to_png("assets/soalPenjumlahan4.png")
<<<<<<< HEAD
    print("✔ Saved soalPenjumlahan4.png")


# ==========================================================
# Eksekusi
# ==========================================================
=======
>>>>>>> f3a6dc9fe6435d2492eb0ebae7a079d9926325cb
make()
