import cairo
from apple_cairo import draw_apple
from banana_cairo import draw_banana

# ini buat simbol -, =
def draw_symbol(ctx, text, x, y):
    ctx.save()
    ctx.set_source_rgb(0,0,0)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(170)
    (tx,ty,w,h,dx,dy)=ctx.text_extents(text)
    ctx.move_to(x - w/2, y + h/2)
    ctx.text_path(text)
    ctx.set_line_width(7)
    ctx.stroke_preserve()
    ctx.set_source_rgb(1,1,1)
    ctx.fill()
    ctx.restore()

# layout multi-row + auto scale
def draw_row(ctx, fn, count, cx, cy):
    spacing_x = 220
    spacing_y = 180

    if count <= 3:
        scale = 0.33
    elif count == 4:
        scale = 0.30
    elif count == 5:
        scale = 0.26
    elif count == 6:
        scale = 0.24
    else:
        scale = 0.23  # untuk 7 buah

    if count == 4:  # 2×2
        fn(ctx,cx-spacing_x/2, cy-spacing_y/4, scale)
        fn(ctx,cx+spacing_x/2, cy-spacing_y/4, scale)
        fn(ctx,cx-spacing_x/2, cy+spacing_y/4, scale)
        fn(ctx,cx+spacing_x/2, cy+spacing_y/4, scale)

    elif count == 7:  # 3–3–1 layout
        # baris 1
        fn(ctx,cx-spacing_x, cy-spacing_y/2, scale)
        fn(ctx,cx,            cy-spacing_y/2, scale)
        fn(ctx,cx+spacing_x,  cy-spacing_y/2, scale)
        # baris 2
        fn(ctx,cx-spacing_x, cy, scale)
        fn(ctx,cx,           cy, scale)
        fn(ctx,cx+spacing_x, cy, scale)
        # baris 3
        fn(ctx,cx, cy+spacing_y/2, scale)

# =====================================================

def make():
    width, height = 1600, 700
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.set_source_rgba(0,0,0,0)
    ctx.paint()

    cy = 350

    draw_row(ctx, draw_apple, 7, 450, cy)
    draw_symbol(ctx, "-", 800, cy)
    draw_row(ctx, draw_banana, 4, 1150, cy)
    draw_symbol(ctx, "=", 1400, cy)

    surface.write_to_png("assets/soalPengurangan7.png")
    print("✔ Saved soalPengurangan7.png")

make()
