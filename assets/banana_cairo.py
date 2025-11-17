import math
import cairo

# -------------------------------------------------
# Surface maker
# -------------------------------------------------
def make_surface(filename, w=600, h=600):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
    ctx = cairo.Context(surface)
    return surface, ctx

# -------------------------------------------------
# Draw banana
# -------------------------------------------------
def draw_banana(ctx, cx, cy, scale=1.0):
    ctx.save()
    ctx.translate(cx, cy)
    ctx.scale(scale, scale)
    ctx.rotate(math.radians(20))  # Rotasi pisang sedikit

    # ---------------------------------------
    # BAYANGAN PISANG
    # ---------------------------------------
    ctx.save()
    ctx.translate(10, 20)
    ctx.scale(1.0, 0.4)
    
    grad_shadow = cairo.RadialGradient(0, 0, 30, 0, 0, 150)
    grad_shadow.add_color_stop_rgba(0, 0, 0, 0, 0.25)
    grad_shadow.add_color_stop_rgba(1, 0, 0, 0, 0)
    
    ctx.set_source(grad_shadow)
    ctx.arc(0, 0, 150, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()

    # ---------------------------------------
    # BADAN PISANG (bentuk melengkung)
    # ---------------------------------------
    ctx.set_line_width(18)
    ctx.set_line_join(cairo.LineJoin.ROUND)
    ctx.set_line_cap(cairo.LineCap.ROUND)

    # Kurva luar pisang
    ctx.move_to(-20, -180)
    ctx.curve_to(-80, -150, -120, -80, -130, 0)
    ctx.curve_to(-135, 80, -100, 140, -40, 165)
    ctx.curve_to(-10, 175, 20, 175, 35, 168)
    
    # Kurva dalam (sisi kanan)
    ctx.curve_to(45, 145, 40, 120, 30, 90)
    ctx.curve_to(20, 40, 10, -20, 15, -80)
    ctx.curve_to(18, -120, 25, -155, 35, -175)
    ctx.curve_to(20, -180, 0, -185, -20, -180)

    # Gradient kuning pisang
    grad_banana = cairo.LinearGradient(-130, 0, 40, 0)
    grad_banana.add_color_stop_rgb(0, 1.0, 0.85, 0.0)   # Kuning terang
    grad_banana.add_color_stop_rgb(0.3, 1.0, 0.90, 0.2)
    grad_banana.add_color_stop_rgb(0.7, 0.95, 0.75, 0.0)
    grad_banana.add_color_stop_rgb(1, 0.85, 0.65, 0.0)  # Kuning gelap

    ctx.set_source(grad_banana)
    ctx.fill_preserve()

    # Outline hitam tebal
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

    # ---------------------------------------
    # GARIS LENGKUNG TENGAH (detail pisang)
    # ---------------------------------------
    ctx.set_line_width(12)
    ctx.set_source_rgb(0, 0, 0)
    
    ctx.move_to(-15, -170)
    ctx.curve_to(-60, -140, -95, -70, -102, 10)
    ctx.curve_to(-105, 75, -80, 130, -35, 155)
    ctx.stroke()

    # Garis lengkung kedua (lebih detail)
    ctx.set_line_width(8)
    ctx.move_to(0, -175)
    ctx.curve_to(-30, -145, -50, -80, -55, 0)
    ctx.curve_to(-58, 60, -45, 110, -15, 145)
    ctx.stroke()

    # ---------------------------------------
    # UJUNG ATAS PISANG (warna coklat)
    # ---------------------------------------
    ctx.save()

    # POSISI PALING PAS dengan kurva pisang kamu
    ctx.translate(35, -175)
    ctx.rotate(math.radians(-20))

    # Area coklat
    ctx.arc(0, 0, 25, 0, 2 * math.pi)
    grad_tip = cairo.RadialGradient(0, 0, 5, 0, 0, 25)
    grad_tip.add_color_stop_rgb(0, 0.25, 0.15, 0.05)
    grad_tip.add_color_stop_rgb(1, 0.40, 0.28, 0.12)
    ctx.set_source(grad_tip)
    ctx.fill()

    # Outline hitam
    ctx.arc(0, 0, 25, 0, 2 * math.pi)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(12)
    ctx.stroke()

    ctx.restore()


    # ---------------------------------------
    # BINTIK-BINTIK COKLAT (matang)
    # ---------------------------------------
    ctx.set_source_rgba(0.4, 0.25, 0.05, 0.6)
    
    # Bintik 1
    ctx.save()
    ctx.translate(-90, -50)
    ctx.scale(1.5, 1.0)
    ctx.arc(0, 0, 8, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()
    
    # Bintik 2
    ctx.save()
    ctx.translate(-70, 30)
    ctx.scale(1.3, 1.0)
    ctx.arc(0, 0, 10, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()
    
    # Bintik 3
    ctx.save()
    ctx.translate(-50, 90)
    ctx.scale(1.2, 1.0)
    ctx.arc(0, 0, 7, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()
    
    # Bintik 4
    ctx.save()
    ctx.translate(-85, -100)
    ctx.scale(1.4, 0.9)
    ctx.arc(0, 0, 6, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()
    
    # Bintik 5
    ctx.save()
    ctx.translate(-40, -10)
    ctx.scale(1.1, 1.0)
    ctx.arc(0, 0, 9, 0, 2 * math.pi)
    ctx.fill()
    ctx.restore()

    ctx.restore()

# -------------------------------------------------
# SAVE PNG
# -------------------------------------------------
surface, ctx = make_surface("banana_transparent.png")
draw_banana(ctx, 300, 300, 1.0)
surface.write_to_png("banana_transparent.png")

print("Pisang dengan background transparan berhasil dibuat -> banana_transparent.png")