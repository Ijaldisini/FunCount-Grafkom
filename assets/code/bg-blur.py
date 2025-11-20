import cairo

WIDTH, HEIGHT = 800, 450

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)


# ========================
# 0. FAKE BLUR FUNCTION
# ========================
def fake_blur(surface, scale=0.2):
    width = surface.get_width()
    height = surface.get_height()

    # Resize ke ukuran kecil
    small_w = int(width * scale)
    small_h = int(height * scale)

    small_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, small_w, small_h)
    small_ctx = cairo.Context(small_surface)

    # Render background ke versi kecil
    small_ctx.scale(scale, scale)
    small_ctx.set_source_surface(surface, 0, 0)
    small_ctx.paint()

    # Perbesar kembali (blur effect)
    blurred_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    blur_ctx = cairo.Context(blurred_surface)

    blur_ctx.scale(1/scale, 1/scale)
    blur_ctx.set_source_surface(small_surface, 0, 0)
    blur_ctx.paint()

    return blurred_surface



# ========================
# 1. LANGIT ORANYE GRADASI
# ========================
sky = cairo.LinearGradient(0, 0, 0, HEIGHT)
sky.add_color_stop_rgb(0, 1.0, 0.65, 0.25)
sky.add_color_stop_rgb(1, 1.0, 0.75, 0.45)
ctx.set_source(sky)
ctx.paint()


# ========================
# 2. AWAN LEBIH TEBAL & REALISTIS
# ========================
def draw_cloud(cx, cy, scale=1.0):
    ctx.set_source_rgb(1.0, 0.90, 0.75)

    ctx.arc(cx, cy, 30 * scale, 0, 3.14 * 2)
    ctx.fill()

    ctx.arc(cx + 25 * scale, cy + 5 * scale, 25 * scale, 0, 3.14 * 2)
    ctx.fill()

    ctx.arc(cx - 25 * scale, cy + 5 * scale, 25 * scale, 0, 3.14 * 2)
    ctx.fill()

    ctx.arc(cx, cy - 15 * scale, 20 * scale, 0, 3.14 * 2)
    ctx.fill()

cloud_positions = [
    (120, 130, 1.1),
    (260, 110, 0.9),
    (420, 125, 1.0),
    (580, 115, 0.95),
    (720, 130, 1.1)
]

for (cx, cy, s) in cloud_positions:
    draw_cloud(cx, cy, s)



# ========================
# 3. PEGUNUNGAN BERTUMPUK
# ========================
def draw_mountain(y, color, height_scale):
    ctx.set_source_rgb(*color)
    ctx.move_to(0, y)
    for i in range(0, WIDTH + 120, 120):
        ctx.line_to(i, y - 80 * height_scale)
        ctx.line_to(i + 60, y)
    ctx.close_path()
    ctx.fill()

draw_mountain(320, (0.28, 0.45, 0.28), 1.4)
draw_mountain(340, (0.24, 0.40, 0.24), 1.2)
draw_mountain(360, (0.20, 0.35, 0.20), 1.0)



# ========================
# 6. TANAH / PLATFORM
# ========================
ctx.set_source_rgb(0.35, 0.2, 0.1)
ctx.rectangle(0, 360, WIDTH, 90)
ctx.fill()

ctx.set_source_rgb(0.18, 0.5, 0.18)
ctx.rectangle(0, 360, WIDTH, 12)
ctx.fill()

ctx.set_source_rgb(0.25, 0.15, 0.05)
for i in range(0, WIDTH, 50):
    ctx.rectangle(i + 10, 390, 15, 8)
    ctx.fill()



# ========================
# SAVE BACKGROUND NORMAL
# ========================
surface.write_to_png("jungle_background.png")
print("Background jungle pixel-art berhasil dibuat!")



# ========================
# GENERATE FAKE BLUR VERSION
# ========================
blurred = fake_blur(surface, scale=0.22)
blurred.write_to_png("jungle_background_blur.png")
print("Fake blur berhasil dibuat → jungle_background_blur.png")
