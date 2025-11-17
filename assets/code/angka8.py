import cairo

WIDTH, HEIGHT = 300, 300
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

text = "8"

ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(200)

(x, y, w, h, dx, dy) = ctx.text_extents(text)
x_pos = (WIDTH - w) / 2 - x
y_pos = (HEIGHT + h) / 2

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.move_to(x_pos, y_pos)
ctx.text_path(text)
ctx.stroke_preserve()

ctx.set_source_rgb(1, 1, 1)
ctx.fill()

surface.write_to_png("assets/angka_8.png")
    