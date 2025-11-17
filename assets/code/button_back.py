import cairo

WIDTH, HEIGHT = 300, 200

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

button_x = 20
button_y = 20
button_width = 260
button_height = 160
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

ctx.set_source_rgb(1, 1, 1)
ctx.new_path()
ctx.move_to(160, 60)   # kanan atas segitiga
ctx.line_to(100, 100)  # tengah kiri segitiga
ctx.line_to(160, 140)  # kanan bawah segitiga
ctx.close_path()
ctx.fill()

surface.write_to_png("assets/button_back.png")
