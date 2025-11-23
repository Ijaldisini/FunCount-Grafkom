import cairo
from PIL import Image, ImageFilter
import random
import io

WIDTH, HEIGHT = 800, 450

# ========================================
# 1. RENDER BACKGROUND DENGAN CAIRO
# ========================================
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# ========================
# LANGIT HIJAU LEMBUT
# ========================
sky = cairo.LinearGradient(0, 0, 0, HEIGHT)
sky.add_color_stop_rgb(0, 0.65, 0.85, 0.70)
sky.add_color_stop_rgb(1, 0.75, 0.95, 0.80)
ctx.set_source(sky)
ctx.paint()

# ========================
# GUNUNG FOREST
# ========================
def draw_mountain(y, height_scale, color):
    ctx.set_source_rgb(*color)
    ctx.move_to(0, y)
    for i in range(0, WIDTH + 120, 120):
        ctx.line_to(i, y - 70 * height_scale)
        ctx.line_to(i + 60, y)
    ctx.close_path()
    ctx.fill()

draw_mountain(320, 1.0, (0.45, 0.65, 0.45))
draw_mountain(350, 1.2, (0.35, 0.55, 0.35))

# ========================
# MIST / KABUT
# ========================
mist = cairo.LinearGradient(0, 250, 0, 400)
mist.add_color_stop_rgba(0, 1, 1, 1, 0.35)
mist.add_color_stop_rgba(1, 1, 1, 1, 0.0)

ctx.set_source(mist)
ctx.rectangle(0, 200, WIDTH, 200)
ctx.fill()

# ========================
# POHON LEBIH BANYAK
# ========================
def draw_tree(x, base_y=340, scale=1.0):
    ctx.set_source_rgb(0.40, 0.28, 0.12)
    ctx.rectangle(x + 10*scale, base_y - 35*scale, 10*scale, 40*scale)
    ctx.fill()

    ctx.set_source_rgb(0.10, 0.45, 0.18)
    ctx.arc(x + 15*scale, base_y - 55*scale, 25*scale, 0, 6.28)
    ctx.fill()

tree_positions = [
    (20, 340, 1.0), (80, 345, 0.9), (140, 335, 1.1),
    (200, 345, 0.8), (260, 340, 1.0), (320, 350, 0.9),
    (380, 340, 1.2), (440, 345, 1.0), (500, 335, 1.1),
    (560, 340, 0.9), (620, 350, 1.0), (680, 340, 1.1),
    (740, 345, 0.9), (780, 340, 1.0)
]

for x, y, s in tree_positions:
    draw_tree(x, y, s)

# ========================
# RUMPUT BAWAH
# ========================
ctx.set_source_rgb(0.30, 0.60, 0.30)
ctx.rectangle(0, 350, WIDTH, 100)
ctx.fill()

# ========================================
# 2. CONVERT CAIRO → PIL UNTUK BLUR
# ========================================
buf = surface.get_data()
pil_img = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buf, "raw", "BGRA", 0, 1)

# ========================================
# 3. BLUR AREA DALAM BORDER
# ========================================
border_margin = 20
blur_x = border_margin
blur_y = border_margin
blur_w = WIDTH - border_margin * 2
blur_h = HEIGHT - border_margin * 2

# crop area
crop = pil_img.crop((blur_x, blur_y, blur_x + blur_w, blur_y + blur_h))

# gaussian blur
blurred = crop.filter(ImageFilter.GaussianBlur(12))

# tempel kembali
pil_img.paste(blurred, (blur_x, blur_y))

# ========================================
# 4. KONVERSI PIL → CAIRO KEMBALI
# ========================================
output_bytes = io.BytesIO()
pil_img.save(output_bytes, format='PNG')
output_bytes.seek(0)

final_surface = cairo.ImageSurface.create_from_png(output_bytes)
ctx = cairo.Context(final_surface)

# ========================================
# 5. TAMBAHKAN CARD TRANSPARAN + BORDER
# ========================================
ctx.set_source_rgba(1, 1, 1, 0.18)  # lebih tipis biar sesuai blur
ctx.rectangle(blur_x, blur_y, blur_w, blur_h)
ctx.fill()

# BORDER
ctx.set_line_width(4)
ctx.set_source_rgb(0.15, 0.35, 0.15)
ctx.rectangle(blur_x, blur_y, blur_w, blur_h)
ctx.stroke()

# ========================================
# 6. SIMPAN
# ========================================
final_surface.write_to_png("forest_background_blurred.png")
print("Background Hutan Blur berhasil dibuat!")
