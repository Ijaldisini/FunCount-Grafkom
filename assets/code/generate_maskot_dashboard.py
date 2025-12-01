import math
import cairo

WIDTH, HEIGHT = 360, 360

def draw_bear_dashboard(ctx, x=0, y=0, scale=1.0):
    ctx.save()
    ctx.translate(x, y)
    ctx.scale(scale, scale)

    # ---------------------------
    # Helper: circle (RGB/RGBA)
    # ---------------------------
    def circle(cx, cy, r, color):
        ctx.arc(cx, cy, r, 0, 2 * math.pi)
        if len(color) == 4:
            ctx.set_source_rgba(*color)
        else:
            ctx.set_source_rgb(*color)
        ctx.fill()

    # ---------------------------
    # Helper: rounded rect
    # ---------------------------
    def rounded_rect(cx, cy, w, h, r, fill_color, stroke_color=None, stroke_w=2):
        ctx.new_sub_path()
        ctx.arc(cx + w - r, cy + r,     r, -math.pi/2, 0)
        ctx.arc(cx + w - r, cy + h - r, r, 0, math.pi/2)
        ctx.arc(cx + r,     cy + h - r, r, math.pi/2, math.pi)
        ctx.arc(cx + r,     cy + r,     r, math.pi, 3*math.pi/2)
        ctx.close_path()

        # fill
        if len(fill_color) == 4:
            ctx.set_source_rgba(*fill_color)
        else:
            ctx.set_source_rgb(*fill_color)
        ctx.fill_preserve()

        # stroke
        if stroke_color:
            if len(stroke_color) == 4:
                ctx.set_source_rgba(*stroke_color)
            else:
                ctx.set_source_rgb(*stroke_color)
            ctx.set_line_width(stroke_w)
            ctx.stroke()
        else:
            ctx.new_path()

    # ---------------------------
    # Shadow
    # ---------------------------
    ctx.save()
    ctx.translate(150, 300)
    ctx.scale(2, 0.5)
    circle(0, 0, 40, (0, 0, 0, 0.2))
    ctx.restore()

    # ---------------------------
    # BODY
    # ---------------------------
    body_x, body_y = 110, 170
    rounded_rect(body_x, body_y, 110, 120, 35,
                 fill_color=(0.83, 0.68, 0.48),
                 stroke_color=(0.55, 0.38, 0.26),
                 stroke_w=4)

    # Belly
    rounded_rect(body_x+25, body_y+30, 60, 70, 25,
                 fill_color=(1.0, 0.95, 0.85),
                 stroke_color=(0.65, 0.45, 0.32),
                 stroke_w=3)

    # Feet
    for dx in [body_x + 25, body_x + 65]:
        rounded_rect(dx, body_y + 95, 35, 30, 12,
                     fill_color=(0.75, 0.55, 0.39),
                     stroke_color=(0.5, 0.32, 0.2),
                     stroke_w=3)

    # ---------------------------
    # ARMS (Right waving, left normal)
    # ---------------------------
    # left arm
    rounded_rect(body_x - 20, body_y + 20, 30, 60, 15,
                 fill_color=(0.8, 0.63, 0.45),
                 stroke_color=(0.5, 0.35, 0.22),
                 stroke_w=3)

    # right arm (raised & waving)
    ctx.save()
    ctx.translate(body_x + 120, body_y + 10)
    ctx.rotate(-0.6)  # rotate up
    rounded_rect(0, 0, 30, 70, 15,
                 fill_color=(0.8, 0.63, 0.45),
                 stroke_color=(0.5, 0.35, 0.22),
                 stroke_w=3)
    ctx.restore()

    # ---------------------------
    # HEAD
    # ---------------------------
    head_cx = 165
    head_cy = 115
    head_r = 70

    circle(head_cx, head_cy, head_r, (0.83, 0.68, 0.48))

    # Head outline
    ctx.arc(head_cx, head_cy, head_r, 0, 2*math.pi)
    ctx.set_source_rgb(0.5, 0.35, 0.25)
    ctx.set_line_width(4)
    ctx.stroke()

    # Ears
    for sx in [-1, 1]:
        ex = head_cx + sx * 45
        ey = head_cy - 55
        circle(ex, ey, 28, (0.83, 0.68, 0.48))
        circle(ex, ey, 18, (1.0, 0.9, 0.85))

    # Eyes (open friendly)
    eye_y = head_cy - 10
    for sx in [-1, 1]:
        ex = head_cx + sx * 25
        circle(ex, eye_y, 11, (0.2, 0.2, 0.25))
        circle(ex - 3, eye_y - 3, 3, (1, 1, 1))

    # Nose
    circle(head_cx, head_cy + 10, 12, (0.25, 0.18, 0.12))

    # Happy mouth
    ctx.set_source_rgb(0.25, 0.18, 0.12)
    ctx.set_line_width(4)
    ctx.arc(head_cx, head_cy + 38, 25, 0, math.pi)
    ctx.stroke()

    # Cheeks
    for sx in [-1, 1]:
        circle(head_cx + sx * 40, head_cy + 25, 12, (1.0, 0.6, 0.7))

    ctx.restore()


# SAVE PNG -----------------------------
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgba(0, 0, 0, 0)
ctx.paint()

draw_bear_dashboard(ctx, 20, 10, 1.0)
surface.write_to_png("assets/maskot_dashboard.png")

print("maskot_dashboard.png BERHASIL dibuat!")
