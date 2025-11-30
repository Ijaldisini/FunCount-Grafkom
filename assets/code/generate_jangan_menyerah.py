import cairo
import math

WIDTH, HEIGHT = 900, 320

def create_jangan_menyerah():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    r = 40
    ctx.new_sub_path()
    ctx.arc(125, 125, r, math.pi, math.pi * 1.5)
    ctx.arc(WIDTH - 115, 125, r, math.pi * 1.5, 0)
    ctx.arc(WIDTH - 115, 205, r, 0, math.pi * 0.5)
    ctx.arc(125, 205, r, math.pi * 0.5, math.pi)
    ctx.close_path()
    ctx.set_source_rgba(0, 0, 0, 0.3)
    ctx.fill()

    ctx.new_sub_path()
    ctx.arc(120, 120, r, math.pi, math.pi * 1.5)
    ctx.arc(WIDTH - 120, 120, r, math.pi * 1.5, 0)
    ctx.arc(WIDTH - 120, 200, r, 0, math.pi * 0.5)
    ctx.arc(120, 200, r, math.pi * 0.5, math.pi)
    ctx.close_path()

    grad = cairo.LinearGradient(0, 80, 0, 240)
    grad.add_color_stop_rgb(0, 1.0, 0.75, 0.3)   
    grad.add_color_stop_rgb(0.5, 1.0, 0.55, 0.1) 
    grad.add_color_stop_rgb(1, 0.95, 0.45, 0.0)  
    ctx.set_source(grad)
    ctx.fill_preserve()

    ctx.set_line_width(8)
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    ctx.new_sub_path()
    ctx.arc(120, 120, r, math.pi, math.pi * 1.5)
    ctx.arc(WIDTH - 120, 120, r, math.pi * 1.5, 0)
    ctx.arc(WIDTH - 120, 200, r, 0, math.pi * 0.5)
    ctx.arc(120, 200, r, math.pi * 0.5, math.pi)
    ctx.close_path()
    ctx.set_line_width(3)
    ctx.set_source_rgba(1, 1, 1, 0.5)
    ctx.stroke()

    def draw_star(x, y, size, rotation=0):
        ctx.save()
        ctx.translate(x, y)
        ctx.rotate(rotation)
        ctx.move_to(0, -size)
        for i in range(5):
            ctx.rotate(math.pi * 2 / 5)
            ctx.line_to(0, -size)
            ctx.rotate(math.pi / 5)
            ctx.line_to(0, -size * 0.4)
            ctx.rotate(math.pi / 5)
        ctx.close_path()
        ctx.fill()
        ctx.restore()

    ctx.set_source_rgba(1, 1, 1, 0.8)
    draw_star(180, 100, 8, math.pi / 4)
    draw_star(WIDTH - 180, 100, 8, 0)
    draw_star(150, 220, 6, math.pi / 6)
    draw_star(WIDTH - 150, 220, 6, -math.pi / 6)

    face_center_x = WIDTH / 2
    face_center_y = 115
    
    ctx.set_source_rgba(0, 0, 0, 0.2)
    ctx.arc(face_center_x + 2, face_center_y + 2, 35, 0, 2 * math.pi)
    ctx.fill()
    
    ctx.set_source_rgb(1, 1, 1)
    ctx.arc(face_center_x, face_center_y, 35, 0, 2 * math.pi)
    ctx.fill()
    
    ctx.set_source_rgb(0.2, 0.2, 0.2)
    ctx.arc(face_center_x - 12, face_center_y - 8, 3.5, 0, 2 * math.pi)
    ctx.fill()
    ctx.arc(face_center_x - 12, face_center_y + 2, 2, 0, 2 * math.pi)
    ctx.fill()
    ctx.move_to(face_center_x - 12, face_center_y - 4)
    ctx.line_to(face_center_x - 12, face_center_y + 5)
    ctx.set_line_width(2)
    ctx.stroke()
    
    ctx.arc(face_center_x + 12, face_center_y - 8, 3.5, 0, 2 * math.pi)
    ctx.fill()
    ctx.arc(face_center_x + 12, face_center_y + 2, 2, 0, 2 * math.pi)
    ctx.fill()
    ctx.move_to(face_center_x + 12, face_center_y - 4)
    ctx.line_to(face_center_x + 12, face_center_y + 5)
    ctx.set_line_width(2)
    ctx.stroke()
    
    ctx.set_line_width(3)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.arc(face_center_x, face_center_y + 20, 15, 0.3, math.pi - 0.3)
    ctx.stroke()
    
    ctx.set_line_width(2.5)
    ctx.move_to(face_center_x - 20, face_center_y - 15)
    ctx.line_to(face_center_x - 8, face_center_y - 18)
    ctx.stroke()
    ctx.move_to(face_center_x + 8, face_center_y - 18)
    ctx.line_to(face_center_x + 20, face_center_y - 15)
    ctx.stroke()

    ctx.set_font_size(46)
    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    text = "SEMANGAT! COBA LAGI YA!"
    xb, yb, tw, th, xa, ya = ctx.text_extents(text)
    text_x = (WIDTH - tw) / 2
    text_y = 218
    
    ctx.set_source_rgba(0, 0, 0, 0.3)
    ctx.move_to(text_x + 2, text_y + 2)
    ctx.show_text(text)
    
    ctx.set_source_rgb(1, 1, 1)
    ctx.move_to(text_x, text_y)
    ctx.show_text(text)

    ctx.set_source_rgba(1, 1, 1, 0.6)
    ctx.arc(WIDTH / 2 - 100, 160, 3, 0, 2 * math.pi)
    ctx.fill()
    ctx.arc(WIDTH / 2 + 120, 165, 2.5, 0, 2 * math.pi)
    ctx.fill()

    surface.write_to_png("jangan_menyerah.png")
    print("✔ jangan_menyerah.png berhasil dibuat dengan wajah sedih custom!")

create_jangan_menyerah()