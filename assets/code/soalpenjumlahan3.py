# ==========================================================
# SOAL PENJUMLAHAN 3 : 1 banana + 2 apple =
# ==========================================================

import cairo
from apple_cairo import draw_apple
from banana_cairo import draw_banana

# ==========================================================
# Gambar simbol (+ dan =) dengan outline hitam tebal
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
    ctx.move_to(x - w / 2, y + h / 2)

    ctx.text_path(text)
    ctx.set_line_width(8)
    ctx.stroke_preserve()

    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    ctx.restore()


# ==========================================================
# Gambar barisan buah center
# ==========================================================
def draw_row(ctx, fn, count, center_x, y):
    spacing = 250
    total = (count - 1) * spacing
    start = center_x - total / 2

    for i in range(count):
        fn(ctx, start + i * spacing, y, 0.35)


# ==========================================================
# Buat file PNG soal penjumlahan
# ==========================================================
def make():
    width, height = 1500, 700

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # background transparan
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    y = 350

    # 1 banana
    draw_row(ctx, draw_banana, 1, 350, y)

    # +
    draw_symbol(ctx, "+", 700, y)

    # 2 apple
    draw_row(ctx, draw_apple, 2, 1050, y)

    # =
    draw_symbol(ctx, "=", 1350, y)

    surface.write_to_png("assets/soalPenjumlahan3.png")
    print("✔ Saved soalPenjumlahan3.png")


# ==========================================================
# Eksekusi
# ==========================================================
make()
