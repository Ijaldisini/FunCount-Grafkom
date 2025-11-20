import cairo
from PIL import Image, ImageFilter
import io
import random

WIDTH, HEIGHT = 800, 450

# ============================
#  SURFACE AWAL (CAIRO)
# ============================
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# ========================
# 1. LANGIT SUNRISE / SUNSET
# ========================
sky = cairo.LinearGradient(0, 0, 0, HEIGHT)
sky.add_color_stop_rgb(0, 0.90, 0.45, 0.35)
sky.add_color_stop_rgb(0.5, 0.98, 0.75, 0.50)
sky.add_color_stop_rgb(1, 0.40, 0.60, 0.90)
ctx.set_source(sky)
ctx.paint()

# ========================
# 2. AWAN
# ========================
def draw_cloud(cx, cy, scale=1.0):
    ctx.set_source_rgba(1, 1, 1, 0.85)
    ctx.arc(cx, cy, 28 * scale, 0, 6.28); ctx.fill()
    ctx.arc(cx + 22*scale, cy + 5, 22*scale, 0, 6.28); ctx.fill()
    ctx.arc(cx - 22*scale, cy + 5, 22*scale, 0, 6.28); ctx.fill()
    ctx.arc(cx, cy - 18*scale, 20*scale, 0, 6.28); ctx.fill()

clouds = [
    (100, 90, 1.0), (200, 70, 0.8), (300, 110, 1.2),
    (450, 80, 1.0), (600, 100, 1.1), (720, 80, 0.9),
    (150, 150, 0.9), (350, 140, 1.1), (550, 160, 0.85)
]

for cx, cy, s in clouds:
    draw_cloud(cx, cy, s)

# ========================
# 3. GUNUNG (MULTI-LAYER)
# ========================
def draw_mountain(y, height_scale, color):
    ctx.set_source_rgb(*color)
    ctx.move_to(0, y)
    for i in range(0, WIDTH + 150, 150):
        ctx.line_to(i, y - 80 * height_scale)
        ctx.line_to(i + 75, y)
    ctx.close_path()
    ctx.fill()

draw_mountain(330, 1.5, (0.50, 0.60, 0.55))
draw_mountain(360, 1.8, (0.40, 0.55, 0.50))
draw_mountain(390, 2.0, (0.30, 0.50, 0.45))

# ========================
# 4. PADANG BUNGA
# ========================
ctx.set_source_rgb(0.3, 0.65, 0.35)
ctx.rectangle(0, 350, WIDTH, 100)
ctx.fill()

def draw_flower(x, y, scale=1.0):
    ctx.set_source_rgb(1, 0.7, 0.8)
    ctx.arc(x, y, 4*scale, 0, 6.28); ctx.fill()
    ctx.set_source_rgb(1, 0.9, 0.4)
    ctx.arc(x, y, 2*scale, 0, 6.28); ctx.fill()

for i in range(160):
    fx = random.randint(0, WIDTH)
    fy = random.randint(355, 445)
    scale = random.uniform(0.5, 1.2)
    draw_flower(fx, fy, scale)

# ============================================
# 5. AMBIL IMAGE CAIRO → PIL UNTUK BLUR
# ============================================
buf = surface.get_data()
pil_img = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buf, "raw", "BGRA", 0, 1)

# ============================================
# 6. BLUR TENGAH (INSIDE BORDER)
# ============================================
border_margin = 20
blur_x = border_margin
blur_y = border_margin
blur_w = WIDTH - border_margin * 2
blur_h = HEIGHT - border_margin * 2

crop = pil_img.crop((blur_x, blur_y, blur_x + blur_w, blur_y + blur_h))
blurred = crop.filter(ImageFilter.GaussianBlur(10))   # 10 px blur

pil_img.paste(blurred, (blur_x, blur_y))

# ============================================
# 7. KONVERSI BALIK KE CAIRO
# ============================================
output_bytes = io.BytesIO()
pil_img.save(output_bytes, format='PNG')
output_bytes.seek(0)

blur_surface = cairo.ImageSurface.create_from_png(output_bytes)
ctx = cairo.Context(blur_surface)

# ============================================
# 8. BORDER + CARD TRANSPARAN (GLASS EFFECT)
# ============================================
ctx.set_source_rgba(1, 1, 1, 0.20)
ctx.rectangle(blur_x, blur_y, blur_w, blur_h)
ctx.fill()

ctx.set_line_width(4)
ctx.set_source_rgb(0.2, 0.4, 0.3)
ctx.rectangle(blur_x, blur_y, blur_w, blur_h)
ctx.stroke()

# ============================================
# 9. SIMPAN
# ============================================
blur_surface.write_to_png("sunset_floral_blurred_card.png")
print("Background dengan blur tengah berhasil dibuat!")
