import cairo
from apple_cairo import draw_apple
from banana_cairo import draw_banana

# ini buat simbol -, =
def draw_symbol(ctx, text, x, y):
    ctx.save()
    ctx.set_source_rgb(0, 0, 0)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(170)
    (tx, ty, w, h, dx, dy) = ctx.text_extents(text)
    ctx.move_to(x - w/2, y + h/2)
    ctx.text_path(text)
    ctx.set_line_width(7)
    ctx.stroke_preserve()
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill()
    ctx.restore()

# layout multi-row + auto scale
def draw_row(ctx, fn, count, cx, cy):
    spacing_x = 220
    spacing_y = 180

    scale = 0.33 if count <= 3 else \
            0.30 if count == 4 else \
            0.26 if count == 5 else \
            0.24 if count == 6 else \
            0.22

    if count == 5:
        fn(ctx, cx-spacing_x,   cy-spacing_y/3, scale)
        fn(ctx, cx,             cy-spacing_y/2, scale)
        fn(ctx, cx+spacing_x,   cy-spacing_y/3, scale)
        fn(ctx, cx-spacing_x/1.3, cy+spacing_y/3, scale)
        fn(ctx, cx+spacing_x/1.3, cy+spacing_y/3, scale)

    elif count == 10:
        fn(ctx, cx-spacing_x, cy-spacing_y, scale)
        fn(ctx, cx,           cy-spacing_y, scale)
        fn(ctx, cx+spacing_x, cy-spacing_y, scale)

        fn(ctx, cx-spacing_x, cy, scale)
        fn(ctx, cx,           cy, scale)
        fn(ctx, cx+spacing_x, cy, scale)

        fn(ctx, cx-spacing_x, cy+spacing_y, scale)
        fn(ctx, cx,           cy+spacing_y, scale)
        fn(ctx, cx+spacing_x, cy+spacing_y, scale)

        fn(ctx, cx, cy+spacing_y*1.8, scale)

# =====================================================

def make():
    width, height = 1600, 900
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.set_source_rgba(0,0,0,0)
    ctx.paint()

    cy = 350

    draw_row(ctx, draw_banana, 10, 450, cy)
    draw_symbol(ctx, "-", 750, cy)
    draw_row(ctx, draw_banana, 5, 1250, cy)
    draw_symbol(ctx, "=", 1450, cy)

<<<<<<< HEAD
    surface.write_to_png("assets/soalPengurangan10.png")
    print("✔ Saved soalPengurangan10.png")

=======
    surface.write_to_png("assets/soalPenjumlahan10.png")
>>>>>>> f3a6dc9fe6435d2492eb0ebae7a079d9926325cb
make()
