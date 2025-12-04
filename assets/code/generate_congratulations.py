import cairo
import math
import random

WIDTH, HEIGHT = 900, 320

def draw_sparkle(ctx, x, y, size, color):
    ctx.save()
    ctx.set_source_rgba(*color)
    ctx.set_line_width(2.5)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.move_to(x, y - size)
    ctx.line_to(x, y + size)
    ctx.move_to(x - size, y)
    ctx.line_to(x + size, y)
    ctx.move_to(x - size*0.7, y - size*0.7)
    ctx.line_to(x + size*0.7, y + size*0.7)
    ctx.move_to(x + size*0.7, y - size*0.7)
    ctx.line_to(x - size*0.7, y + size*0.7)
    ctx.stroke()
    ctx.restore()

def draw_confetti(ctx, x, y, width, height, color, rotation):
    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(rotation)
    
    if random.random() > 0.5:
        grad = cairo.LinearGradient(-width/2, -height/2, width/2, height/2)
        grad.add_color_stop_rgba(0, color[0], color[1], color[2], color[3])
        grad.add_color_stop_rgba(1, color[0]*0.7, color[1]*0.7, color[2]*0.7, color[3])
        ctx.set_source(grad)
    else:
        ctx.set_source_rgba(*color)
    
    shape = random.randint(0, 3)
    if shape == 0:  
        ctx.rectangle(-width/2, -height/2, width, height)
    elif shape == 1:  
        ctx.arc(0, 0, width/2, 0, 2*math.pi)
    elif shape == 2:  
        ctx.move_to(0, -height/2)
        ctx.line_to(width/2, height/2)
        ctx.line_to(-width/2, height/2)
        ctx.close_path()
    else: 
        ctx.move_to(0, -height/2)
        ctx.line_to(width/2, 0)
        ctx.line_to(0, height/2)
        ctx.line_to(-width/2, 0)
        ctx.close_path()
    ctx.fill()
    ctx.restore()

def draw_star(ctx, x, y, size, color):
    ctx.save()
    ctx.translate(x, y)
    ctx.set_source_rgba(*color)
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

def draw_rainbow(ctx, center_x, center_y, radius_start, arc_width):
    rainbow_colors = [
        (1.0, 0.0, 0.0),    
        (1.0, 0.5, 0.0),    
        (1.0, 1.0, 0.0),    
        (0.0, 1.0, 0.0),    
        (0.0, 0.5, 1.0),    
        (0.3, 0.0, 0.8),    
        (0.5, 0.0, 0.5),    
    ]
    for i, color in enumerate(rainbow_colors):
        radius = radius_start + (i * arc_width)
        ctx.set_source_rgba(color[0], color[1], color[2], 0.7)
        ctx.set_line_width(arc_width)
        ctx.arc(center_x, center_y, radius, math.pi, 2 * math.pi)
        ctx.stroke()

def create_congratulations():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()
    draw_rainbow(ctx, WIDTH / 2, HEIGHT + 100, 180, 8)
    random.seed(42) 
    confetti_colors = [
        (1.0, 0.2, 0.3, 0.9),  
        (1.0, 0.8, 0.0, 0.9),  
        (0.2, 0.8, 1.0, 0.9), 
        (0.9, 0.3, 0.9, 0.9),   
        (0.3, 1.0, 0.4, 0.9),
        (1.0, 0.5, 0.0, 0.9), 
        (0.4, 0.3, 1.0, 0.9),   
        (1.0, 0.2, 0.6, 0.9),
        (0.2, 1.0, 0.8, 0.9),  
        (1.0, 1.0, 0.3, 0.9),   
    ]
    for i in range(60):
        x = random.randint(50, WIDTH - 50)
        y = random.randint(20, HEIGHT - 20)
        width = random.randint(6, 14)
        height = random.randint(10, 20)
        color = random.choice(confetti_colors)
        rotation = random.uniform(0, math.pi * 2)
        draw_confetti(ctx, x, y, width, height, color, rotation)

    ctx.set_source_rgba(0, 0, 0, 0.3)
    ctx.rectangle(88, 68, WIDTH - 160, 200)
    ctx.fill()

    radius = 25
    x, y, w, h = 80, 60, WIDTH - 160, 200
    
    ctx.new_sub_path()
    ctx.arc(x + w - radius, y + radius, radius, -math.pi/2, 0)
    ctx.arc(x + w - radius, y + h - radius, radius, 0, math.pi/2)
    ctx.arc(x + radius, y + h - radius, radius, math.pi/2, math.pi)
    ctx.arc(x + radius, y + radius, radius, math.pi, 3*math.pi/2)
    ctx.close_path()

    gradient = cairo.LinearGradient(0, 60, 0, 260)
    gradient.add_color_stop_rgb(0, 0.15, 0.45, 1.0)   
    gradient.add_color_stop_rgb(0.5, 0.25, 0.55, 1.0) 
    gradient.add_color_stop_rgb(1, 0.1, 0.35, 0.95)   
    ctx.set_source(gradient)
    ctx.fill_preserve()

    ctx.set_line_width(12)
    ctx.set_source_rgb(1.0, 0.85, 0.0)
    ctx.stroke_preserve()
    
    ctx.set_line_width(6)
    ctx.set_source_rgba(1.0, 1.0, 0.6, 0.6)
    ctx.stroke()

    draw_star(ctx, 120, 90, 12, (1.0, 0.95, 0.2, 0.9))
    draw_star(ctx, WIDTH - 120, 90, 12, (1.0, 0.95, 0.2, 0.9))
    draw_star(ctx, 120, 230, 10, (1.0, 0.95, 0.2, 0.9))
    draw_star(ctx, WIDTH - 120, 230, 10, (1.0, 0.95, 0.2, 0.9))

    ctx.set_source_rgba(0.6, 0.5, 0.0, 0.7)
    ctx.move_to(80, 160)
    ctx.line_to(35, 125)
    ctx.line_to(35, 195)
    ctx.close_path()
    ctx.fill()
    
    ribbon_gradient_l = cairo.LinearGradient(40, 130, 80, 160)
    ribbon_gradient_l.add_color_stop_rgb(0, 1.0, 0.9, 0.0)
    ribbon_gradient_l.add_color_stop_rgb(1, 1.0, 0.75, 0.0)
    ctx.set_source(ribbon_gradient_l)
    ctx.move_to(80, 160)
    ctx.line_to(40, 130)
    ctx.line_to(40, 190)
    ctx.close_path()
    ctx.fill()
    
    ctx.set_source_rgba(1.0, 1.0, 0.8, 0.5)
    ctx.move_to(80, 160)
    ctx.line_to(45, 135)
    ctx.line_to(45, 175)
    ctx.close_path()
    ctx.fill()

    ctx.set_source_rgba(0.6, 0.5, 0.0, 0.7)
    ctx.move_to(WIDTH - 80, 160)
    ctx.line_to(WIDTH - 35, 125)
    ctx.line_to(WIDTH - 35, 195)
    ctx.close_path()
    ctx.fill()
    
    ribbon_gradient_r = cairo.LinearGradient(WIDTH - 80, 160, WIDTH - 40, 130)
    ribbon_gradient_r.add_color_stop_rgb(0, 1.0, 0.75, 0.0)
    ribbon_gradient_r.add_color_stop_rgb(1, 1.0, 0.9, 0.0)
    ctx.set_source(ribbon_gradient_r)
    ctx.move_to(WIDTH - 80, 160)
    ctx.line_to(WIDTH - 40, 130)
    ctx.line_to(WIDTH - 40, 190)
    ctx.close_path()
    ctx.fill()
    
    ctx.set_source_rgba(1.0, 1.0, 0.8, 0.5)
    ctx.move_to(WIDTH - 80, 160)
    ctx.line_to(WIDTH - 45, 135)
    ctx.line_to(WIDTH - 45, 175)
    ctx.close_path()
    ctx.fill()

    trophy_x = WIDTH / 2
    trophy_y = 110
    ctx.set_source_rgba(0, 0, 0, 0.3)
    ctx.move_to(trophy_x - 18, trophy_y + 2)
    ctx.line_to(trophy_x - 13, trophy_y - 23)
    ctx.line_to(trophy_x + 17, trophy_y - 23)
    ctx.line_to(trophy_x + 22, trophy_y + 2)
    ctx.close_path()
    ctx.fill()
    trophy_grad = cairo.LinearGradient(trophy_x - 20, trophy_y - 25, trophy_x + 20, trophy_y)
    trophy_grad.add_color_stop_rgb(0, 1.0, 0.95, 0.3)
    trophy_grad.add_color_stop_rgb(1, 1.0, 0.75, 0.0)
    ctx.set_source(trophy_grad)
    ctx.move_to(trophy_x - 20, trophy_y)
    ctx.line_to(trophy_x - 15, trophy_y - 25)
    ctx.line_to(trophy_x + 15, trophy_y - 25)
    ctx.line_to(trophy_x + 20, trophy_y)
    ctx.close_path()
    ctx.fill()
    
    ctx.set_source_rgb(1.0, 0.85, 0.0)
    ctx.rectangle(trophy_x - 18, trophy_y, 36, 8)
    ctx.fill()
    ctx.rectangle(trophy_x - 12, trophy_y + 8, 24, 5)
    ctx.fill()
    
    ctx.set_line_width(3)
    ctx.arc(trophy_x - 20, trophy_y - 12, 8, math.pi, 3*math.pi/2)
    ctx.stroke()
    ctx.arc(trophy_x + 20, trophy_y - 12, 8, 3*math.pi/2, 2*math.pi)
    ctx.stroke()
    
    ctx.set_source_rgba(1.0, 1.0, 1.0, 0.6)
    ctx.arc(trophy_x - 8, trophy_y - 18, 3, 0, 2*math.pi)
    ctx.fill()

    ctx.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(50)

    text = "HEBAT! KAMU BENAR SEMUA!"
    xb, yb, tw, th, xa, ya = ctx.text_extents(text)
    text_x = (WIDTH - tw) / 2
    text_y = 200
    
    ctx.set_source_rgba(0, 0, 0, 0.5)
    ctx.move_to(text_x + 3, text_y + 3)
    ctx.show_text(text)
    
    text_gradient = cairo.LinearGradient(0, text_y - th, 0, text_y)
    text_gradient.add_color_stop_rgb(0, 1.0, 1.0, 0.6)
    text_gradient.add_color_stop_rgb(1, 1.0, 0.9, 0.0)
    ctx.set_source(text_gradient)
    ctx.move_to(text_x, text_y)
    ctx.show_text(text)

    spark_color_white = (1.0, 1.0, 1.0, 0.95)
    spark_color_yellow = (1.0, 1.0, 0.4, 0.9)
    spark_color_rainbow = [
        (1.0, 0.3, 0.3, 0.8),
        (1.0, 0.8, 0.2, 0.8),
        (0.3, 1.0, 0.3, 0.8),
        (0.3, 0.8, 1.0, 0.8),
        (1.0, 0.3, 1.0, 0.8),
    ]
    
    random.seed(100)
    for i in range(25):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(50, HEIGHT - 50)
        size = random.randint(6, 12)
        if random.random() > 0.6:
            color = random.choice(spark_color_rainbow)
        elif random.random() > 0.5:
            color = spark_color_yellow
        else:
            color = spark_color_white
        draw_sparkle(ctx, x, y, size, color)

    surface.write_to_png("congratulations.png")
    print("✔ congratulations.png berhasil dibuat dengan pelangi dan confetti meriah!")

create_congratulations()