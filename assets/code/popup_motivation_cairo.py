import math
import cairo
import os

WIDTH, HEIGHT = 800, 400

ASSETS_DIR = "assets"

def make_surface(filename):
    os.makedirs(ASSETS_DIR, exist_ok=True)
    path = os.path.join(ASSETS_DIR, filename)
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()
    return surface, ctx, path

def rounded_rect(ctx, x, y, w, h, r):
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    ctx.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    ctx.arc(x + r, y + r, r, math.pi, 3 * math.pi / 2)
    ctx.close_path()

def draw_gradient_bg(ctx, x, y, w, h, r, color1, color2):
    """Background gradient ceria"""
    rounded_rect(ctx, x, y, w, h, r)
    ctx.clip_preserve()
    
    gradient = cairo.LinearGradient(x, y, x, y + h)
    gradient.add_color_stop_rgb(0, *color1)
    gradient.add_color_stop_rgb(1, *color2)
    ctx.set_source(gradient)
    ctx.fill()
    ctx.reset_clip()

def draw_text_center(ctx, text, y, size, color=(1, 1, 1), bold=True, alpha=1.0):
    ctx.select_font_face(
        "Sans",
        cairo.FONT_SLANT_NORMAL,
        cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL
    )
    ctx.set_font_size(size)
    ext = ctx.text_extents(text)
    x = (WIDTH - ext.width) / 2 - ext.x_bearing
    baseline = y
    
    if len(color) == 3:
        ctx.set_source_rgba(color[0], color[1], color[2], alpha)
    else:
        ctx.set_source_rgba(*color)
    
    ctx.move_to(x, baseline)
    ctx.show_text(text)

def draw_star(ctx, cx, cy, radius, color, rotation=0):
    """Gambar bintang 5 sudut yang lebih cantik"""
    ctx.save()
    ctx.translate(cx, cy)
    ctx.rotate(rotation)
    
    outer_r = radius
    inner_r = radius * 0.4
    
    ctx.set_source_rgb(*color)
    for i in range(5):
        angle_out = (i * 2 * math.pi / 5) - math.pi / 2
        angle_in = angle_out + math.pi / 5
        
        if i == 0:
            ctx.move_to(outer_r * math.cos(angle_out), outer_r * math.sin(angle_out))
        else:
            ctx.line_to(outer_r * math.cos(angle_out), outer_r * math.sin(angle_out))
        
        ctx.line_to(inner_r * math.cos(angle_in), inner_r * math.sin(angle_in))
    
    ctx.close_path()
    ctx.fill()
    ctx.restore()

def draw_sparkle(ctx, cx, cy, size, color):
    """Gambar kilauan bintang 4 titik"""
    ctx.save()
    ctx.translate(cx, cy)
    ctx.set_source_rgb(*color)
    ctx.set_line_width(size * 0.3)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    
    ctx.move_to(0, -size)
    ctx.line_to(0, size)
    ctx.stroke()
    
    ctx.move_to(-size, 0)
    ctx.line_to(size, 0)
    ctx.stroke()
    
    d = size * 0.7
    ctx.move_to(-d, -d)
    ctx.line_to(d, d)
    ctx.stroke()
    
    ctx.move_to(d, -d)
    ctx.line_to(-d, d)
    ctx.stroke()
    
    ctx.restore()

def draw_confetti(ctx, cx, cy, size, color, angle=0):
    """Gambar confetti persegi panjang"""
    ctx.save()
    ctx.translate(cx, cy)
    ctx.rotate(angle)
    ctx.set_source_rgb(*color)
    ctx.rectangle(-size * 0.4, -size, size * 0.8, size * 2)
    ctx.fill()
    ctx.restore()

def draw_trophy(ctx, cx, cy, size, color):
    """Gambar piala sederhana dan lucu"""
    ctx.set_source_rgb(*color)
    
    cup_w = size * 0.7
    cup_h = size * 0.6
    ctx.move_to(cx - cup_w/2, cy - size/2)
    ctx.line_to(cx - cup_w/3, cy + cup_h/2)
    ctx.line_to(cx + cup_w/3, cy + cup_h/2)
    ctx.line_to(cx + cup_w/2, cy - size/2)
    ctx.close_path()
    ctx.fill()
    
    base_w = size * 0.9
    ctx.rectangle(cx - base_w/2, cy + cup_h/2, base_w, size * 0.15)
    ctx.fill()
    
    handle_r = size * 0.25
    ctx.set_line_width(size * 0.12)
    ctx.arc(cx - cup_w/2 - handle_r/2, cy, handle_r, -math.pi/2, math.pi/2)
    ctx.stroke()
    ctx.arc(cx + cup_w/2 + handle_r/2, cy, handle_r, math.pi/2, 3*math.pi/2)
    ctx.stroke()

def draw_cute_character(ctx, cx, cy, size, color, expression="happy"):
    """Gambar karakter lucu dengan ekspresi berbeda"""
    shadow_offset = size * 0.05
    ctx.set_source_rgba(0, 0, 0, 0.2)
    ctx.arc(cx + shadow_offset, cy + shadow_offset, size, 0, 2 * math.pi)
    ctx.fill()
    
    ctx.save()
    ctx.arc(cx, cy, size, 0, 2 * math.pi)
    ctx.clip()
    
    gradient = cairo.RadialGradient(cx - size * 0.3, cy - size * 0.3, size * 0.2, cx, cy, size)
    r, g, b = color
    gradient.add_color_stop_rgb(0, min(1, r * 1.2), min(1, g * 1.2), min(1, b * 1.2))
    gradient.add_color_stop_rgb(1, r, g, b)
    ctx.set_source(gradient)
    ctx.arc(cx, cy, size, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()
    
    ctx.set_source_rgb(1, 1, 1)
    ctx.set_line_width(size * 0.08)
    ctx.arc(cx, cy, size, 0, 2 * math.pi)
    ctx.stroke()
    
    eye_r = size * 0.15
    eye_dx = size * 0.35
    eye_y = cy - size * 0.25
    
    if expression == "happy":
        ctx.set_source_rgb(0.2, 0.1, 0.05)
        ctx.set_line_width(eye_r * 0.8)
        ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.move_to(cx - eye_dx - eye_r, eye_y)
        ctx.line_to(cx - eye_dx + eye_r, eye_y)
        ctx.stroke()
        ctx.move_to(cx + eye_dx - eye_r, eye_y)
        ctx.line_to(cx + eye_dx + eye_r, eye_y)
        ctx.stroke()
    else:
        ctx.set_source_rgb(0.2, 0.1, 0.05)
        ctx.arc(cx - eye_dx, eye_y, eye_r, 0, 2 * math.pi)
        ctx.fill()
        ctx.arc(cx + eye_dx, eye_y, eye_r, 0, 2 * math.pi)
        ctx.fill()
        
        ctx.set_source_rgb(1, 1, 1)
        highlight_r = eye_r * 0.4
        ctx.arc(cx - eye_dx + eye_r * 0.3, eye_y - eye_r * 0.3, highlight_r, 0, 2 * math.pi)
        ctx.fill()
        ctx.arc(cx + eye_dx + eye_r * 0.3, eye_y - eye_r * 0.3, highlight_r, 0, 2 * math.pi)
        ctx.fill()
    
    ctx.set_source_rgba(1, 0.4, 0.5, 0.4)
    cheek_r = size * 0.25
    ctx.arc(cx - size * 0.6, cy + size * 0.1, cheek_r, 0, 2 * math.pi)
    ctx.fill()
    ctx.arc(cx + size * 0.6, cy + size * 0.1, cheek_r, 0, 2 * math.pi)
    ctx.fill()
    
    ctx.set_source_rgb(0.2, 0.1, 0.05)
    ctx.set_line_width(size * 0.12)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    
    if expression == "excited":
        mouth_r = size * 0.4
        ctx.arc(cx, cy + size * 0.15, mouth_r, math.radians(30), math.radians(150))
    else:
        mouth_r = size * 0.45
        ctx.arc(cx, cy + size * 0.1, mouth_r, math.radians(20), math.radians(160))
    
    ctx.stroke()

def draw_popup(filename, title_text, subtitle_text, 
            bg_color1, bg_color2, accent_color, char_color, 
            char_expression, decorations):
    
    surface, ctx, path = make_surface(filename)

    margin = 45
    box_x = margin
    box_y = margin
    box_w = WIDTH - 2 * margin
    box_h = HEIGHT - 2 * margin
    radius = 50

    shadow_offset = 8
    ctx.set_source_rgba(0, 0, 0, 0.15)
    rounded_rect(ctx, box_x + shadow_offset, box_y + shadow_offset, box_w, box_h, radius)
    ctx.fill()

    draw_gradient_bg(ctx, box_x, box_y, box_w, box_h, radius, bg_color1, bg_color2)

    rounded_rect(ctx, box_x, box_y, box_w, box_h, radius)
    ctx.set_line_width(10)
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

    if decorations == "stars":
        positions = [
            (WIDTH * 0.12, HEIGHT * 0.22, 22, math.radians(15)),
            (WIDTH * 0.88, HEIGHT * 0.22, 22, math.radians(-15)),
            (WIDTH * 0.15, HEIGHT * 0.78, 18, math.radians(30)),
            (WIDTH * 0.85, HEIGHT * 0.78, 18, math.radians(-30)),
        ]
        colors = [(1, 0.85, 0.2), (1, 0.5, 0.6), (0.4, 0.8, 1), (0.6, 1, 0.5)]
        
        for i, (x, y, size, rot) in enumerate(positions):
            draw_star(ctx, x, y, size, colors[i % len(colors)], rot)
        
        sparkles = [
            (WIDTH * 0.25, HEIGHT * 0.35, 8),
            (WIDTH * 0.75, HEIGHT * 0.35, 8),
            (WIDTH * 0.20, HEIGHT * 0.65, 6),
            (WIDTH * 0.80, HEIGHT * 0.65, 6),
        ]
        for x, y, size in sparkles:
            draw_sparkle(ctx, x, y, size, (1, 1, 1))
    
    elif decorations == "confetti":
        import random
        random.seed(42)
        colors = [(1, 0.3, 0.5), (1, 0.7, 0.2), (0.3, 0.7, 1), (0.6, 1, 0.4), (1, 0.5, 0.8)]
        
        for i in range(15):
            x = WIDTH * (0.1 + random.random() * 0.8)
            y = HEIGHT * (0.15 + random.random() * 0.7)
            size = random.randint(8, 15)
            angle = random.random() * math.pi * 2
            color = colors[i % len(colors)]
            draw_confetti(ctx, x, y, size, color, angle)
    
    elif decorations == "trophy":
        draw_trophy(ctx, WIDTH * 0.15, HEIGHT * 0.25, 35, (1, 0.8, 0.2))
        draw_trophy(ctx, WIDTH * 0.85, HEIGHT * 0.25, 35, (1, 0.8, 0.2))
        
        star_positions = [
            (WIDTH * 0.10, HEIGHT * 0.15, 12),
            (WIDTH * 0.20, HEIGHT * 0.20, 10),
            (WIDTH * 0.80, HEIGHT * 0.20, 10),
            (WIDTH * 0.90, HEIGHT * 0.15, 12),
        ]
        for x, y, size in star_positions:
            draw_star(ctx, x, y, size, (1, 0.9, 0.3), math.radians(15))

    char_y = HEIGHT * 0.28
    draw_cute_character(ctx, WIDTH * 0.5, char_y, 55, char_color, char_expression)

    shadow_offset = 3
    draw_text_center(ctx, title_text, y=HEIGHT * 0.58 + shadow_offset, 
                    size=95, color=(0, 0, 0), alpha=0.3, bold=True)
    draw_text_center(ctx, title_text, y=HEIGHT * 0.58, 
                    size=95, color=accent_color, bold=True)

    draw_text_center(ctx, subtitle_text, y=HEIGHT * 0.82, 
                    size=40, color=(1, 1, 1), bold=False)

    surface.write_to_png(path)
    print(f"✅ {filename} - Popup keren tersimpan!")

def main():
    print("🎨 Membuat popup super ceria untuk anak TK...\n")
    
    # Nilai 40-59: Tema semangat dengan confetti
    draw_popup(
        "popup_bagus.png",
        "BAGUS!",
        "Kamu hebat! Ayo semangat lagi! 💪",
        bg_color1=(1.0, 0.6, 0.3),     
        bg_color2=(1.0, 0.85, 0.5),    
        accent_color=(0.9, 0.2, 0.2),  
        char_color=(1.0, 0.75, 0.2),   
        char_expression="happy",
        decorations="confetti"
    )

    # Nilai 60-79: Tema fresh dengan bintang
    draw_popup(
        "popup_semangat.png",
        "SEMANGAT!",
        "Wah keren! Kamu makin pintar! ⭐",
        bg_color1=(0.4, 0.9, 0.65),    
        bg_color2=(0.65, 1.0, 0.8),    
        accent_color=(0.15, 0.65, 0.35), 
        char_color=(0.5, 0.95, 0.7),   
        char_expression="happy",
        decorations="stars"
    )

    # Nilai 80-99: Tema juara dengan piala
    draw_popup(
        "popup_hebat.png",
        "HEBAT!",
        "Luar biasa! Kamu juara sejati! 🏆",
        bg_color1=(0.6, 0.5, 1.0),     
        bg_color2=(0.8, 0.87, 1.0),    
        accent_color=(0.35, 0.15, 0.85), 
        char_color=(0.75, 0.65, 1.0),  
        char_expression="excited",
        decorations="trophy"
    )
    
    print("\n✨ Selesai! Popup sudah jauh lebih keren dan ceria! 🎉")

if __name__ == "__main__":
    main()