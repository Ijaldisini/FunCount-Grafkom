import cairo
from apple_cairo import draw_apple
from banana_cairo import draw_banana

# Fungsi untuk menggambar simbol (+ dan =)
def draw_symbol(ctx, text, x, y):
    ctx.save()

    # Outline hitam
    ctx.set_source_rgb(0, 0, 0)

    # Font simbol
    ctx.select_font_face(
        "Arial",
        cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_BOLD
    )
    ctx.set_font_size(180)

    # Hitung posisi supaya center
    (tx, ty, w, h, dx, dy) = ctx.text_extents(text)
    ctx.move_to(x - w / 2, y + h / 2)

    # Outline
    ctx.text_path(text)
    ctx.set_line_width(8)
    ctx.stroke_preserve()

    # Isi putih
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    ctx.restore()

# Fungsi menggambar barisan buah jenis apa saja
def draw_row(ctx, fruit_fn, count, center_x, y):
    spacing = 250  # jarak antar buah
    total = (count - 1) * spacing
    start = center_x - total / 2

    for i in range(count):
        fruit_fn(ctx, start + i * spacing, y, 0.35)

# Fungsi utama untuk membuat soal dalam bentuk PN
def make():
    width, height = 1500, 700

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # background transparan
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    y = 350  # posisi vertikal utama

    # 2 apple
    draw_row(ctx, draw_apple, 2, 350, y)

    # +
    draw_symbol(ctx, "+", 700, y)

    # 1 banana  
    draw_row(ctx, draw_banana, 1, 1050, y)

    # =
    draw_symbol(ctx, "=", 1350, y)

    surface.write_to_png("assets/soalPenjumlahan2.png")
    print("✔ Saved soalPenjumlahan2.png")

make()
