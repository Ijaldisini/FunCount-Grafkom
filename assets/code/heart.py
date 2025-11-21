import cairo

def make_surface(w=256, h=256):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(surface)
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()
    return surface, ctx

HEART_PATTERN = [
    [0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,2,2,2,1,1,0,1,1,2,2,2,1,0,0],
    [1,2,3,3,2,2,2,1,2,2,2,2,2,2,1,0],
    [1,2,3,2,2,2,2,2,2,2,2,2,2,2,1,0],
    [1,2,3,2,2,2,2,2,2,2,2,2,2,2,1,0],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
    [1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,0],
    [0,1,2,2,2,2,2,2,2,2,2,2,2,1,0,0],
    [0,1,2,2,2,2,2,2,2,2,2,2,2,1,0,0],
    [0,0,1,2,2,2,2,2,2,2,2,2,1,0,0,0],
    [0,0,0,1,2,2,2,2,2,2,2,1,0,0,0,0],
    [0,0,0,0,1,2,2,2,2,2,1,0,0,0,0,0],
    [0,0,0,0,0,1,2,2,2,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
]

def draw_pixel_heart(ctx, cx, cy, pixel_size=12, active=True):
    """
    active=True  -> Hati merah (nyawa ada)
    active=False -> Hati putih/abu (nyawa hilang)
    """
    ctx.save()
    grid_w = len(HEART_PATTERN[0]) * pixel_size
    grid_h = len(HEART_PATTERN) * pixel_size
    start_x = cx - grid_w // 2
    start_y = cy - grid_h // 2
    
    if active:
        colors = {
            1: (0.1, 0.1, 0.1),      
            2: (0.85, 0.12, 0.18),  
            3: (1.0, 0.55, 0.6),     
        }
    else:
        colors = {
            1: (0.5, 0.5, 0.5),      
            2: (0.9, 0.9, 0.9),      
            3: (1.0, 1.0, 1.0),      
        }
    
    for row_idx, row in enumerate(HEART_PATTERN):
        for col_idx, pixel in enumerate(row):
            if pixel == 0:
                continue
            
            x = start_x + col_idx * pixel_size
            y = start_y + row_idx * pixel_size
            
            r, g, b = colors[pixel]
            ctx.set_source_rgb(r, g, b)
            
            ctx.rectangle(x, y, pixel_size, pixel_size)
            ctx.fill()
    
    ctx.restore()

def draw_lives_display(ctx, cx, cy, lives=3, max_lives=3, pixel_size=10, spacing=20):
    """
    Gambar display nyawa dengan hati aktif dan tidak aktif
    lives = jumlah nyawa saat ini
    max_lives = jumlah maksimal nyawa
    """
    heart_width = len(HEART_PATTERN[0]) * pixel_size
    total_width = max_lives * heart_width + (max_lives - 1) * spacing
    start_x = cx - total_width // 2 + heart_width // 2
    
    for i in range(max_lives):
        x = start_x + i * (heart_width + spacing)
        is_active = i < lives
        draw_pixel_heart(ctx, x, cy, pixel_size, active=is_active)

surface, ctx = make_surface(512, 128)
draw_lives_display(ctx, 256, 64, lives=3, max_lives=3, pixel_size=6, spacing=25)
surface.write_to_png("assets/lives_3.png")

surface, ctx = make_surface(512, 128)
draw_lives_display(ctx, 256, 64, lives=2, max_lives=3, pixel_size=6, spacing=25)
surface.write_to_png("assets/lives_2.png")

surface, ctx = make_surface(512, 128)
draw_lives_display(ctx, 256, 64, lives=1, max_lives=3, pixel_size=6, spacing=25)
surface.write_to_png("assets/lives_1.png")

surface, ctx = make_surface(512, 128)
draw_lives_display(ctx, 256, 64, lives=0, max_lives=3, pixel_size=6, spacing=25)
surface.write_to_png("assets/lives_0.png")
