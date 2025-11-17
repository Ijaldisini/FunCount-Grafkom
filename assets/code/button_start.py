import cairo

WIDTH, HEIGHT = 400, 200

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

button_x = 50
button_y = 50
button_width = 300
button_height = 100
radius = 40

def rounded_rect(ctx, x, y, w, h, r):
    ctx.new_path()
    ctx.arc(x + w - r, y + r, r, -90 * (3.1416/180), 0)
    ctx.arc(x + w - r, y + h - r, r, 0, 90 * (3.1416/180))
    ctx.arc(x + r, y + h - r, r, 90 * (3.1416/180), 180 * (3.1416/180))
    ctx.arc(x + r, y + r, r, 180 * (3.1416/180), 270 * (3.1416/180))
    ctx.close_path()

rounded_rect(ctx, button_x, button_y, button_width, button_height, radius)

ctx.set_source_rgb(0.29, 0.69, 0.31)
ctx.fill_preserve()

ctx.set_line_width(10)
ctx.set_source_rgb(0.18, 0.49, 0.20)
ctx.stroke()

ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(60)

text = "START"
(x, y, w, h, dx, dy) = ctx.text_extents(text)

text_x = button_x + (button_width - w) / 2 - x
text_y = button_y + (button_height + h) / 2

ctx.set_source_rgb(1, 1, 1)
ctx.move_to(text_x, text_y)
ctx.show_text(text)

surface.write_to_png("assets/button_start.png")