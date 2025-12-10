import cairo
import math

WIDTH, HEIGHT = 900, 320

def draw_sparkle(ctx, x, y, size, color):
    ctx.save()
    ctx.set_source_rgba(*color)
    ctx.set_line_width(2)
    ctx.move_to(x, y - size)
    ctx.line_to(x, y + size)
    ctx.move_to(x - size, y)
    ctx.line_to(x + size, y)
    ctx.stroke()
    ctx.restore()

def create_congratulations():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    # Transparent background
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    # Gradient banner
    gradient = cairo.LinearGradient(0, 60, 0, 260)
    gradient.add_color_stop_rgb(0, 0.25, 0.55, 1.0)  # blue
    gradient.add_color_stop_rgb(1, 0.15, 0.45, 0.9)  # darker blue

    ctx.rectangle(80, 60, WIDTH - 160, 200)
    ctx.set_source(gradient)
    ctx.fill()

    # Gold border
    ctx.set_line_width(10)
    ctx.set_source_rgb(1.0, 0.8, 0.0)
    ctx.rectangle(80, 60, WIDTH - 160, 200)
    ctx.stroke()

    # Ribbon left
    ctx.set_source_rgb(1.0, 0.85, 0.0)
    ctx.move_to(80, 160)
    ctx.line_to(40, 130)
    ctx.line_to(40, 190)
    ctx.close_path()
    ctx.fill()

    # Ribbon right
    ctx.move_to(WIDTH - 80, 160)
    ctx.line_to(WIDTH - 40, 130)
    ctx.line_to(WIDTH - 40, 190)
    ctx.close_path()
    ctx.fill()

    # Title text
    ctx.select_font_face("Comic Sans MS", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(48)
    ctx.set_source_rgb(1.0, 0.95, 0.0)

    text = "HEBAT! KAMU BENAR SEMUA!"
    xb, yb, tw, th, xa, ya = ctx.text_extents(text)
    ctx.move_to((WIDTH - tw) / 2, (HEIGHT / 2) + (th / 2))
    ctx.show_text(text)

    # Add many sparkles
    spark_color = (1.0, 1.0, 1.0, 0.95)
    sparkle_points = [
        (150, 80), (250, 70), (350, 95), (450, 60), (600, 90), (700, 75),
        (200, 250), (300, 230), (400, 260), (550, 240), (650, 255)
    ]

    for (x, y) in sparkle_points:
        draw_sparkle(ctx, x, y, 12, spark_color)

    surface.write_to_png("congratulations.png")
    print("✔ congratulations.png berhasil dibuat!")

create_congratulations()
