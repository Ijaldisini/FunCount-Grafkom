import cairo
import math

WIDTH, HEIGHT = 900, 320

def create_jangan_menyerah():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    # Bubble shape (rounded rectangle)
    r = 40
    ctx.new_sub_path()
    ctx.arc(120, 120, r, math.pi, math.pi * 1.5)
    ctx.arc(WIDTH - 120, 120, r, math.pi * 1.5, 0)
    ctx.arc(WIDTH - 120, 200, r, 0, math.pi * 0.5)
    ctx.arc(120, 200, r, math.pi * 0.5, math.pi)
    ctx.close_path()

    # Orange gradient
    grad = cairo.LinearGradient(0, 80, 0, 240)
    grad.add_color_stop_rgb(0, 1.0, 0.65, 0.2)   # light orange
    grad.add_color_stop_rgb(1, 1.0, 0.45, 0.0)   # deep orange
    ctx.set_source(grad)
    ctx.fill_preserve()

    # White border
    ctx.set_line_width(10)
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    # Sad emoji
    ctx.select_font_face("Comic Sans MS", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(55)
    ctx.set_source_rgb(1, 1, 1)
    emoji = "ಥ﹏ಥ"
    xb, yb, tw, th, xa, ya = ctx.text_extents(emoji)
    ctx.move_to((WIDTH - tw) / 2, 130)
    ctx.show_text(emoji)

    # MAIN TEXT
    ctx.set_font_size(44)
    text = "SEMANGAT! COBA LAGI YA!"
    xb, yb, tw, th, xa, ya = ctx.text_extents(text)
    ctx.move_to((WIDTH - tw) / 2, 220)
    ctx.show_text(text)

    surface.write_to_png("jangan_menyerah.png")
    print("✔ jangan_menyerah.png berhasil dibuat!")

create_jangan_menyerah()
