import cairo
from PIL import Image, ImageFilter
import io
import random

WIDTH, HEIGHT = 800, 450

# ========================================
# 1. RENDER BACKGROUND DENGAN CAIRO
# ========================================
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# ========================
# LANGIT BIRU CERAH
# ========================
sky = cairo.LinearGradient(0, 0, 0, HEIGHT)
sky.add_color_stop_rgb(0, 0.45, 0.75, 1.0)
sky.add_color_stop_rgb(1, 0.75, 0.90, 1.0)
ctx.set_source(sky)
ctx.paint()

# ========================
# AWAN LEMBUT
# ========================
def draw_cloud(cx, cy, scale=1.0):
    ctx.set_source_rgb(1, 1, 1)
    ctx.arc(cx, cy, 25 * scale, 0, 6.28); ctx.fill()
    ctx.arc(cx + 20 * scale, cy + 5, 20 * scale, 0, 6.28); ctx.fill()
    ctx.arc(cx - 20 * scale, cy + 5, 20 * scale, 0, 6.28); ctx.fill()
    ctx.arc(cx, cy - 15 * scale, 18 * scale, 0, 6.28); ctx.fill()

clouds = [
    (150, 120, 1.0), (350, 100, 0.9),
    (570, 130, 1.1), (700, 110, 0.85)
]

for cx, cy, s in clouds:
    draw_cloud(cx, cy, s)

# ========================
# GUNUNG LEMBUT
# ========================
def draw_mountain(y, height_scale, color):
    ctx.set_source_rgb(*color)
    ctx.move_to(0, y)
    for i in range(0, WIDTH + 120, 120):
        ctx.line_to(i, y - 60 * height_scale)
        ctx.line_to(i + 60, y)
    ctx.close_path()
    ctx.fill()

draw_mountain(330, 1.2, (0.35, 0.65, 0.35))
draw_mountain(350, 1.0, (0.30, 0.60, 0.30))

# ========================
# PEPOHONAN
# ========================
def draw_tree(x, base_y=340):
    ctx.set_source_rgb(0.45, 0.28, 0.12)
    ctx.rectangle(x + 12, base_y - 40, 8, 40)
    ctx.fill()

    ctx.set_source_rgb(0.10, 0.50, 0.15)
    ctx.arc(x + 16, base_y - 60, 25, 0, 6.28)
    ctx.fill()

for pos in [50, 140, 230, 330, 440, 540, 650, 740]:
    draw_tree(pos)

# ========================
# RUMPUT BAWAH
# ========================
ctx.set_source_rgb(0.25, 0.50, 0.20)
ctx.rectangle(0, 340, WIDTH, 110)
ctx.fill()

# ============================================
# 2. CONVERT CAIRO → PIL UNTUK PROSES BLUR
# ============================================
buf = surface.get_data()
pil_img = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buf, "raw", "BGRA", 0, 1)

# ============================================
# 3. BLUR AREA DALAM BORDER
# ============================================
border_margin = 20
blur_x = border_margin
blur_y = border_margin
blur_w = WIDTH - border_margin * 2
blur_h = HEIGHT - border_margin * 2

crop = pil_img.crop((blur_x, blur_y, blur_x + blur_w, blur_y + blur_h))
blurred = crop.filter(ImageFilter.GaussianBlur(10))
pil_img.paste(blurred, (blur_x, blur_y))

# ============================================
# 4. KEMBALIKAN KE CAIRO
# ============================================
output_bytes = io.BytesIO()
pil_img.save(output_bytes, format='PNG')
output_bytes.seek(0)

final_surface = cairo.ImageSurface.create_from_png(output_bytes)
ctx = cairo.Context(final_surface)

# ============================================
# 5. CARD TRANSPARAN + BORDER
# ============================================
ctx.set_source_rgba(1, 1, 1, 0.25)
ctx.rectangle(blur_x, blur_y, blur_w, blur_h)
ctx.fill()

ctx.set_line_width(4)
ctx.set_source_rgb(0.2, 0.4, 0.2)
ctx.rectangle(blur_x, blur_y, blur_w, blur_h)
ctx.stroke()

# ============================================
# 6. SIMPAN FILE
# ============================================
final_surface.write_to_png("addition_background_blurred.png")
print("Background Penjumlahan Blur berhasil dibuat!")
