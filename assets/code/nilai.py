import cairo
import os

os.makedirs("assets", exist_ok=True)

# Daftar warna untuk tiap nilai
colors = {
    100: (1.0, 0.84, 0.0),   # Gold
    90:  (0.2, 0.8, 0.2),    # Lime Green
    80:  (0.2, 0.5, 1.0),    # Blue
    70:  (1.0, 0.9, 0.2),    # Yellow
    60:  (1.0, 0.6, 0.0),    # Orange
    50:  (1.0, 0.2, 0.2),    # Red
    40:  (0.6, 0.2, 0.9),    # Purple
    30:  (0.0, 0.7, 0.7),    # Teal
    20:  (1.0, 0.4, 0.7),    # Pink
    10:  (0.6, 0.6, 0.6)     # Gray
}

WIDTH, HEIGHT = 400, 400
RADIUS = 150

for value in range(10, 110, 10):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Background transparan
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    # Ambil warna badge
    r, g, b = colors[value]

    # Gambar lingkaran berwarna
    ctx.arc(WIDTH/2, HEIGHT/2, RADIUS, 0, 3.14*2)
    ctx.set_source_rgb(r, g, b)
    ctx.fill_preserve()

    # Outline lingkaran
    ctx.set_line_width(10)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

    # Tampilkan nilai angka di tengah
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(130)

    text = str(value)
    (x, y, w, h, dx, dy) = ctx.text_extents(text)
    text_x = WIDTH/2 - (w/2 + x)
    text_y = HEIGHT/2 + (h/2)

    # Outline angka
    ctx.move_to(text_x, text_y)
    ctx.text_path(text)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(8)
    ctx.stroke_preserve()

    # Isi angka
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()

    # Simpan file
    filename = f"assets/nilai{value}.png"
    surface.write_to_png(filename)
<<<<<<< HEAD

    print(f"Saved: {filename}")
=======
>>>>>>> f3a6dc9fe6435d2492eb0ebae7a079d9926325cb
