import cairo
from apple_cairo import draw_apple
from banana_cairo import draw_banana

# ini buat simbol -, =
def draw_symbol(ctx, text, x, y):
    ctx.save()
    ctx.set_source_rgb(0,0,0)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(180)
    (tx,ty,w,h,dx,dy)=ctx.text_extents(text)
    ctx.move_to(x - w/2, y + h/2)
    ctx.text_path(text)
    ctx.set_line_width(8)
    ctx.stroke_preserve()
    ctx.set_source_rgb(1,1,1)
    ctx.fill()
    ctx.restore()

# ini layout buah multi-row style A
def draw_row(ctx, fn, count, cx, cy):
    spacing_x = 240
    spacing_y = 200

    if count == 1:
        fn(ctx, cx, cy, 0.33)

    elif count == 2:
        fn(ctx, cx-spacing_x/2, cy, 0.33)
        fn(ctx, cx+spacing_x/2, cy, 0.33)

    elif count == 3:
        fn(ctx, cx - spacing_x/1.7, cy - spacing_y/4, 0.33)
        fn(ctx, cx + spacing_x/1.7, cy - spacing_y/4, 0.33)
        fn(ctx, cx,                 cy + spacing_y/4, 0.33)

    elif count == 4:
        fn(ctx, cx-spacing_x/2, cy-spacing_y/4, 0.33)
        fn(ctx, cx+spacing_x/2, cy-spacing_y/4, 0.33)
        fn(ctx, cx-spacing_x/2, cy+spacing_y/4, 0.33)
        fn(ctx, cx+spacing_x/2, cy+spacing_y/4, 0.33)

    elif count == 5:
        fn(ctx, cx-spacing_x,     cy-spacing_y/3, 0.33)
        fn(ctx, cx,               cy-spacing_y/2, 0.33)
        fn(ctx, cx+spacing_x,     cy-spacing_y/3, 0.33)
        fn(ctx, cx-spacing_x/1.3, cy+spacing_y/3, 0.33)
        fn(ctx, cx+spacing_x/1.3, cy+spacing_y/3, 0.33)

# ===============================================

def make():
    width, height = 1600, 700
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.set_source_rgba(0,0,0,0)
    ctx.paint()

    cy = 350

    # 1 apple
    draw_row(ctx, draw_apple, 1, 350, cy)
    # -
    draw_symbol(ctx, "-", 700, cy)
    # 1 banana
    draw_row(ctx, draw_banana, 1, 1050, cy)
    # =
    draw_symbol(ctx, "=", 1400, cy)

    surface.write_to_png("assets/soalPengurangan1.png")
    print("✔ Saved soalPengurangan1.png")

make()
