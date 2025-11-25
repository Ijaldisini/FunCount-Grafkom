import cairo
from apple_cairo import draw_apple
from banana_cairo import draw_banana


# tanda - dan =
def draw_symbol(ctx, text, x, y):
    ctx.save()
    ctx.set_source_rgb(0,0,0)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(160)
    (tx,ty,w,h,dx,dy)=ctx.text_extents(text)
    ctx.move_to(x - w/2, y + h/2)
    ctx.text_path(text)
    ctx.set_line_width(7)
    ctx.stroke_preserve()
    ctx.set_source_rgb(1,1,1)
    ctx.fill()
    ctx.restore()


# GRID 3 kolom (untuk kiri)
def draw_row_left(ctx, fn, count, cx, cy):

    if count <= 6:
        scale = 0.30
    elif count <= 9:
        scale = 0.26
    else:
        scale = 0.23

    spacing_x = 160
    spacing_y = 150

    rows = (count + 2) // 3
    top_offset = cy - (rows - 1) * spacing_y / 2

    idx = 0
    for r in range(rows):
        y = top_offset + r * spacing_y
        for c in (-1, 0, 1):
            if idx >= count:
                break
            x = cx + c * spacing_x
            fn(ctx, x, y, scale)
            idx += 1


# GRID 2 kolom (untuk kanan)
def draw_row_right(ctx, fn, count, cx, cy):

    if count <= 4:
        scale = 0.33
    elif count <= 6:
        scale = 0.28
    else:
        scale = 0.25

    spacing_x = 150
    spacing_y = 150

    rows = (count + 1) // 2
    top_offset = cy - (rows - 1) * spacing_y / 2

    idx = 0
    for r in range(rows):
        y = top_offset + r * spacing_y
        x = cx - spacing_x/2
        fn(ctx, x, y, scale)
        idx += 1
        if idx >= count:
            break
        x = cx + spacing_x/2
        fn(ctx, x, y, scale)
        idx += 1


# =============================================================

def make():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1600, 900)
    ctx = cairo.Context(surface)

    ctx.set_source_rgba(0,0,0,0)
    ctx.paint()

    cy = 420

    draw_row_left(ctx, draw_banana, 10, 380, cy)
    draw_symbol(ctx, "-", 750, cy)
    draw_row_right(ctx, draw_banana, 5, 1080, cy)
    draw_symbol(ctx, "=", 1350, cy)

    surface.write_to_png("assets/soalPengurangan10.png")
<<<<<<< HEAD
    print("✔ Saved soalPengurangan10.png")

=======
>>>>>>> f3a6dc9fe6435d2492eb0ebae7a079d9926325cb
make()
