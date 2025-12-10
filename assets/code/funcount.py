import cairo
import math

# =====================================
# CONFIG
# =====================================
WIDTH  = 600
HEIGHT = 180

BG_ALPHA = 0      # transparan

TEXT = "FunCount"
FONT_SIZE = 90

FILL_COLOR    = (1, 1, 1)          # putih
OUTLINE_COLOR = (0.0, 0.55, 0.12)  # hijau tua
SHADOW_COLOR  = (0, 0, 0, 0.25)    # shadow halus


# =====================================
# DRAW
# =====================================
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# background transparan
ctx.set_source_rgba(0, 0, 0, BG_ALPHA)
ctx.paint()

# ----- SHADOW -----
ctx.select_font_face("Arial Rounded MT Bold",
                     cairo.FONT_SLANT_NORMAL,
                     cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(FONT_SIZE)

xbearing, ybearing, text_w, text_h, xa, ya = ctx.text_extents(TEXT)

text_x = (WIDTH - text_w) / 2 - xbearing
text_y = (HEIGHT + text_h) / 2 - ybearing

# shadow offset
ctx.set_source_rgba(*SHADOW_COLOR)
ctx.move_to(text_x + 4, text_y + 4)
ctx.show_text(TEXT)

# ----- OUTLINE -----
ctx.set_line_width(12)
ctx.set_source_rgb(*OUTLINE_COLOR)
ctx.move_to(text_x, text_y)
ctx.text_path(TEXT)
ctx.stroke_preserve()

# ----- FILL -----
ctx.set_source_rgb(*FILL_COLOR)
ctx.fill()

# SAVE
surface.write_to_png("title_funtcount.png")
print("SAVED: title_funtcount.png")
