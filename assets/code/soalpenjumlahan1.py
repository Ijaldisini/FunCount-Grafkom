import cairo
from apple_cairo import draw_apple

# Fungsi untuk menggambar simbol seperti + dan =
def draw_symbol(ctx, text, x, y):
    ctx.save()

    # Warna outline hitam
    ctx.set_source_rgb(0, 0, 0)

    # Font yang dipakai
    ctx.select_font_face(
        "Arial",
        cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_BOLD
    )
    ctx.set_font_size(180)  # Ukuran huruf

    # Hitung ukuran simbol supaya bisa diposisikan center
    (tx, ty, w, h, dx, dy) = ctx.text_extents(text)
    ctx.move_to(x - w / 2, y + h / 2)

    # Outline simbol
    ctx.text_path(text)
    ctx.set_line_width(8)
    ctx.stroke_preserve()

    # Isi simbol putih
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    ctx.restore()


# Gambar barisan buah apple, diposisikan center
def draw_row_apple(ctx, count, center_x, y):
    spacing = 250  # Jarak antar buah
    total = (count - 1) * spacing  # Total lebar row
    start = center_x - total / 2   # Titik mulai (centered)

    # Gambar apple sebanyak `count`
    for i in range(count):
        draw_apple(ctx, start + i * spacing, y, 0.35)

# membuat PNG
def make():
    width, height = 1500, 700  # ukuran canvas

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Background transparan
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    # Posisi Y buah & simbol
    y = 350

    # 1 apple
    draw_row_apple(ctx, 1, 350, y)

    # +
    draw_symbol(ctx, "+", 700, y)

    # 1 apple
    draw_row_apple(ctx, 1, 1050, y)

    # =
    draw_symbol(ctx, "=", 1350, y)

    # Simpan hasil
    surface.write_to_png("assets/soalPenjumlahan1.png")
<<<<<<< HEAD
    print("✔ Saved soalPenjumlahan1.png")
=======
>>>>>>> f3a6dc9fe6435d2492eb0ebae7a079d9926325cb
make()
