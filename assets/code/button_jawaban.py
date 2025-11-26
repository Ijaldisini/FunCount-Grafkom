import cairo

# ============================
# CONFIG BUTTON STYLE
# ============================
width = 260          # lebih panjang seperti tombol "PENGURANGAN"
height = 120
radius = 50
font_size = 80

bg_top = (0.25, 0.85, 0.25)   # hijau terang atas
bg_bottom = (0.10, 0.65, 0.10) # hijau gelap bawah
shadow_color = (0, 0, 0, 0.25) # shadow transparan
text_color = (1, 1, 1)        # putih


def draw_round_rect(ctx, x, y, w, h, r):
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -90 * (3.14/180), 0)
    ctx.arc(x + w - r, y + h - r, r, 0, 90 * (3.14/180))
    ctx.arc(x + r, y + h - r, r, 90 * (3.14/180), 180 * (3.14/180))
    ctx.arc(x + r, y + r, r, 180 * (3.14/180), 270 * (3.14/180))
    ctx.close_path()


def generate_button(num):

    filename = f"button_{num}.png"

    # Buat surface
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Background transparan
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    # ============================
    # SHADOW
    # ============================
    ctx.save()
    ctx.translate(5, 6)  # geser sedikit ke kanan & bawah
    draw_round_rect(ctx, 0, 0, width - 10, height - 10, radius)
    ctx.set_source_rgba(*shadow_color)
    ctx.fill()
    ctx.restore()

    # ============================
    # BUTTON GRADIENT
    # ============================
    draw_round_rect(ctx, 0, 0, width - 10, height - 10, radius)

    gradient = cairo.LinearGradient(0, 0, 0, height)
    gradient.add_color_stop_rgb(0, *bg_top)     # atas terang
    gradient.add_color_stop_rgb(1, *bg_bottom)  # bawah gelap

    ctx.set_source(gradient)
    ctx.fill()

    # ============================
    # TEXT
    # ============================
    ctx.set_source_rgb(*text_color)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(font_size)

    text = str(num)
    xb, yb, tw, th, xa, ya = ctx.text_extents(text)
    tx = (width - tw) / 2 - xb
    ty = (height - th) / 2 - yb

    ctx.move_to(tx, ty)
    ctx.show_text(text)

    surface.write_to_png(filename)
    print("Generated:", filename)


# ============================
# GENERATE 1 – 10
# ============================
for i in range(1, 11):
    generate_button(i)
