import cairo

WIDTH, HEIGHT = 300, 200

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Background transparan
ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

# Button layout
button_x = 20
button_y = 20
button_width = 260
button_height = 160
radius = 40

# Rounded rectangle function
def rounded_rect(ctx, x, y, w, h, r):
    ctx.new_path()
    ctx.arc(x + w - r, y + r, r, -90*(3.14/180), 0)
    ctx.arc(x + w - r, y + h - r, r, 0, 90*(3.14/180))
    ctx.arc(x + r, y + h - r, r, 90*(3.14/180), 180*(3.14/180))
    ctx.arc(x + r, y + r, r, 180*(3.14/180), 270*(3.14/180))
    ctx.close_path()

# Draw button shape
rounded_rect(ctx, button_x, button_y, button_width, button_height, radius)

# Fill (hijau muda)
ctx.set_source_rgb(0.29, 0.69, 0.31)
ctx.fill_preserve()

# Outline (hijau tua)
ctx.set_line_width(10)
ctx.set_source_rgb(0.18, 0.49, 0.20)
ctx.stroke()

# ==============================
# Draw Text "KEMBALI"
# ==============================

ctx.set_source_rgb(1, 1, 1)  # putih
ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(42)

text = "KEMBALI"
ext = ctx.text_extents(text)

text_x = (WIDTH - ext.width) / 2 - ext.x_bearing
text_y = (HEIGHT - ext.height) / 2 - ext.y_bearing

ctx.move_to(text_x, text_y)
ctx.show_text(text)

# Save file
surface.write_to_png("assets/button_kembali.png")