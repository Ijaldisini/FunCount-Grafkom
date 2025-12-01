import math
import cairo

WIDTH, HEIGHT = 320, 340

def draw_bear_happy(ctx, x=0, y=0, scale=1.0):
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(scale, scale)

    def circle(cx, cy, r, color):
        ctx.arc(cx, cy, r, 0, 2 * math.pi)
        if len(color) == 4:
            ctx.set_source_rgba(*color)
        else:
            ctx.set_source_rgb(*color)
        ctx.fill()

    def rounded_rect(cx, cy, w, h, r, fill_color, stroke_color=None, stroke_w=2):
        ctx.new_sub_path()
        ctx.arc(cx + w - r, cy + r, r, -math.pi/2, 0)
        ctx.arc(cx + w - r, cy + h - r, r, 0, math.pi/2)
        ctx.arc(cx + r, cy + h - r, r, math.pi/2, math.pi)
        ctx.arc(cx + r, cy + r, r, math.pi, 3*math.pi/2)
        ctx.close_path()

        if len(fill_color) == 4:
            ctx.set_source_rgba(*fill_color)
        else:
            ctx.set_source_rgb(*fill_color)
        ctx.fill_preserve()

        if stroke_color:
            if len(stroke_color) == 4:
                ctx.set_source_rgba(*stroke_color)
            else:
                ctx.set_source_rgb(*stroke_color)
            ctx.set_line_width(stroke_w)
            ctx.stroke()
        else:
            ctx.new_path()

    # --- shadow ---
    ctx.save()
    ctx.translate(110, 280)
    ctx.scale(1.8, 0.5)
    circle(0, 0, 35, (0, 0, 0, 0.25))
    ctx.restore()

    # --- body ---
    body_x, body_y = 90, 160
    rounded_rect(body_x, body_y, 110, 110, 30,
                 fill_color=(0.83, 0.68, 0.48),
                 stroke_color=(0.55, 0.38, 0.26),
                 stroke_w=4)

    rounded_rect(body_x+25, body_y+25, 60, 60, 25,
                 fill_color=(1.0, 0.95, 0.85),
                 stroke_color=(0.65, 0.45, 0.32),
                 stroke_w=3)

    # legs
    for dx in [body_x+25, body_x+65]:
        rounded_rect(dx, body_y+95, 35, 35, 12,
                     fill_color=(0.75, 0.55, 0.39),
                     stroke_color=(0.5, 0.32, 0.2),
                     stroke_w=3)

    # arms
    for dx in [body_x-20, body_x+110]:
        rounded_rect(dx, body_y+25, 30, 60, 15,
                     fill_color=(0.8, 0.63, 0.45),
                     stroke_color=(0.5, 0.35, 0.22),
                     stroke_w=3)

    # --- Head ---
    head_cx, head_cy, head_r = 145, 105, 70
    circle(head_cx, head_cy, head_r, (0.83, 0.68, 0.48))

    ctx.arc(head_cx, head_cy, head_r, 0, 2*math.pi)
    ctx.set_source_rgb(0.5, 0.35, 0.25)
    ctx.set_line_width(4)
    ctx.stroke()

    # ears
    for sx in [-1, 1]:
        ex = head_cx + sx*45
        ey = head_cy - 55
        circle(ex, ey, 28, (0.83, 0.68, 0.48))
        circle(ex, ey, 16, (1.0, 0.9, 0.8))

    # HAPPY eyes (setengah lingkaran)
    eye_y = head_cy + 5
    ctx.set_line_width(5)
    ctx.set_source_rgb(0.2, 0.2, 0.2)

    for sx in [-1, 1]:
        ex = head_cx + sx*25
        ctx.arc(ex, eye_y, 10, math.pi*1.1, math.pi*1.9)
        ctx.stroke()

    # nose
    circle(head_cx, head_cy + 10, 12, (0.25, 0.18, 0.12))

    # HAPPY mouth (lebar melengkung)
    ctx.set_source_rgb(0.25, 0.18, 0.12)
    ctx.set_line_width(4)
    ctx.arc(head_cx, head_cy + 35, 25, 0, math.pi)
    ctx.stroke()

    # cheeks (lebih pink)
    for sx in [-1, 1]:
        circle(head_cx + sx*40, head_cy + 25, 12, (1.0, 0.6, 0.7))

    ctx.restore()


# SAVE PNG
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

draw_bear_happy(ctx, 20, 20, 1.0)
surface.write_to_png("assets/maskot_happy.png")
print("maskot_happy.png berhasil dibuat!")
