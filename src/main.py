import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FunCount")

# =====================================
# LOAD ASSETS
# =====================================

dashboard = pygame.image.load("assets/bg_utama.png").convert_alpha()
dashboard = pygame.transform.scale(dashboard, (SCREEN_WIDTH, SCREEN_HEIGHT))

dashboard_blur = pygame.image.load("assets/bg_utama_blur.png").convert_alpha()
dashboard_blur = pygame.transform.scale(dashboard_blur, (SCREEN_WIDTH, SCREEN_HEIGHT))

welcome_img = pygame.image.load("assets/welcome.png").convert_alpha()
welcome_img = pygame.transform.scale(welcome_img, (500, 170))
welcome_rect = welcome_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))

bg_mh = pygame.image.load("assets/bg_menghitung.png").convert_alpha()
bg_mh = pygame.transform.scale(bg_mh, (SCREEN_WIDTH, SCREEN_HEIGHT))

bg_pj = pygame.image.load("assets/bg_penjumlahan.png").convert_alpha()
bg_pj = pygame.transform.scale(bg_pj, (SCREEN_WIDTH, SCREEN_HEIGHT))

bg_pg = pygame.image.load("assets/bg_pengurangan.png").convert_alpha()
bg_pg = pygame.transform.scale(bg_pg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# =====================================
# START BUTTON
# =====================================
button_start_original = pygame.image.load("assets/button_start.png").convert_alpha()

SMALL_SIZE = (200, 100)
BIG_SIZE = (300, 150)

button_start_small = pygame.transform.scale(button_start_original, SMALL_SIZE)
button_start_big = pygame.transform.scale(button_start_original, BIG_SIZE)

button_start = button_start_small
button_start_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

# =====================================
# DASHBOARD BUTTONS
# =====================================
btn_mh_original = pygame.image.load("assets/button_menghitung.png").convert_alpha()
btn_pj_original = pygame.image.load("assets/button_penjumlahan.png").convert_alpha()
btn_pg_original = pygame.image.load("assets/button_pengurangan.png").convert_alpha()

btn_mh_small = pygame.transform.scale(btn_mh_original, SMALL_SIZE)
btn_mh_big = pygame.transform.scale(btn_mh_original, BIG_SIZE)

btn_pj_small = pygame.transform.scale(btn_pj_original, SMALL_SIZE)
btn_pj_big = pygame.transform.scale(btn_pj_original, BIG_SIZE)

btn_pg_small = pygame.transform.scale(btn_pg_original, SMALL_SIZE)
btn_pg_big = pygame.transform.scale(btn_pg_original, BIG_SIZE)

btn_mh = btn_mh_small
btn_pj = btn_pj_small
btn_pg = btn_pg_small

btn_mh_rect = btn_mh.get_rect(center=(SCREEN_WIDTH // 2, 130))
btn_pj_rect = btn_pj.get_rect(center=(SCREEN_WIDTH // 2, 250))
btn_pg_rect = btn_pg.get_rect(center=(SCREEN_WIDTH // 2, 370))

# =====================================
# STATE SYSTEM
# =====================================
STATE_MENU_AWAL = 0
STATE_DASHBOARD = 1
STATE_MENGHITUNG = 2
STATE_PENJUMLAHAN = 3
STATE_PENGURANGAN = 4

current_state = STATE_MENU_AWAL

# =====================================
# LOAD BELAJAR MENGHITUNG (URUT 1-10)
# =====================================
# apple and banana (transparent assets expected)
apple_img = pygame.image.load("assets/apple_transparent.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img, (80, 80))

banana_img = pygame.image.load("assets/banana_transparent.png").convert_alpha()
banana_img = pygame.transform.scale(banana_img, (80, 80))

# fruit list for Choice A alternating per level
fruit_list = [apple_img, banana_img]

angka_images = {}
for i in range(1, 11):
    img = pygame.image.load(f"assets/angka_{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (150, 150))
    angka_images[i] = img

# Navigasi tombol belajar menghitung (small sizes)
btn_kembali = pygame.image.load("assets/button_kembali.png").convert_alpha()
btn_kembali = pygame.transform.scale(btn_kembali, (100, 50))
btn_kembali_rect = btn_kembali.get_rect(topleft=(15, 15))

btn_back = pygame.image.load("assets/button_back.png").convert_alpha()
btn_back = pygame.transform.scale(btn_back, (120, 70))
btn_back_rect = btn_back.get_rect(midleft=(40, SCREEN_HEIGHT // 2))

btn_next = pygame.image.load("assets/button_next.png").convert_alpha()
btn_next = pygame.transform.scale(btn_next, (120, 70))
btn_next_rect = btn_next.get_rect(midright=(SCREEN_WIDTH - 40, SCREEN_HEIGHT // 2))

menghitung_level = 1  # mulai dari 1

# =====================================
# LOAD SOAL PENJUMLAHAN
# =====================================
soal_pj = []
for i in range(1, 11):
    img = pygame.image.load(f"assets/soalPenjumlahan{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (430, 210))
    soal_pj.append(img)

current_pj_level = 0

# =====================================
# LOAD SOAL PENGURANGAN
# =====================================
soal_pg = []
for i in range(1, 11):
    img = pygame.image.load(f"assets/soalPengurangan{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (430, 210))
    soal_pg.append(img)

current_pg_level = 0

# =====================================
# COUNTDOWN SYSTEM (for PJ & PG)
# =====================================
countdown_imgs = {}
for i in range(1, 11):
    img = pygame.image.load(f"assets/angka_{i}.png").convert_alpha()
    countdown_imgs[i] = pygame.transform.scale(img, (50, 50))

countdown_start = None
countdown_duration = 10

# =====================================
# GAME LOOP
# =====================================
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # cap 60 FPS
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------------------------
        # MENU AWAL
        # ---------------------------
        if current_state == STATE_MENU_AWAL:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_start_rect.collidepoint(mouse_pos):
                    current_state = STATE_DASHBOARD

        # ---------------------------
        # DASHBOARD
        # ---------------------------
        elif current_state == STATE_DASHBOARD:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_mh_rect.collidepoint(mouse_pos):
                    current_state = STATE_MENGHITUNG
                    menghitung_level = 1  # mulai dari 1 setiap kali masuk

                elif btn_pj_rect.collidepoint(mouse_pos):
                    current_state = STATE_PENJUMLAHAN
                    countdown_start = pygame.time.get_ticks()
                    current_pj_level = 0

                elif btn_pg_rect.collidepoint(mouse_pos):
                    current_state = STATE_PENGURANGAN
                    countdown_start = pygame.time.get_ticks()
                    current_pg_level = 0

        # ---------------------------
        # BELAJAR MENGHITUNG
        # ---------------------------
        elif current_state == STATE_MENGHITUNG:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # tombol kembali (ke dashboard)
                if btn_kembali_rect.collidepoint(mouse_pos):
                    current_state = STATE_DASHBOARD

                # tombol back (mundur level)
                elif btn_back_rect.collidepoint(mouse_pos):
                    menghitung_level -= 1
                    if menghitung_level < 1:
                        menghitung_level = 1

                # tombol next (maju level)
                elif btn_next_rect.collidepoint(mouse_pos):
                    menghitung_level += 1
                    if menghitung_level > 10:
                        menghitung_level = 10

    # =====================================
    # RENDERING
    # =====================================

    # ---------------------------
    # MENU AWAL
    # ---------------------------
    if current_state == STATE_MENU_AWAL:
        if button_start_rect.collidepoint(mouse_pos):
            button_start = button_start_big
        else:
            button_start = button_start_small

        button_start_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

        screen.blit(dashboard, (0, 0))
        screen.blit(welcome_img, welcome_rect)
        screen.blit(button_start, button_start_rect)

    # ---------------------------
    # DASHBOARD MENU
    # ---------------------------
    elif current_state == STATE_DASHBOARD:
        screen.blit(dashboard_blur, (0, 0))

        btn_mh = btn_mh_big if btn_mh_rect.collidepoint(mouse_pos) else btn_mh_small
        btn_pj = btn_pj_big if btn_pj_rect.collidepoint(mouse_pos) else btn_pj_small
        btn_pg = btn_pg_big if btn_pg_rect.collidepoint(mouse_pos) else btn_pg_small

        btn_mh_rect = btn_mh.get_rect(center=(SCREEN_WIDTH // 2, 130))
        btn_pj_rect = btn_pj.get_rect(center=(SCREEN_WIDTH // 2, 250))
        btn_pg_rect = btn_pg.get_rect(center=(SCREEN_WIDTH // 2, 370))

        screen.blit(btn_mh, btn_mh_rect)
        screen.blit(btn_pj, btn_pj_rect)
        screen.blit(btn_pg, btn_pg_rect)

    # ---------------------------
    # MODE BELAJAR MENGHITUNG
    # ---------------------------
    elif current_state == STATE_MENGHITUNG:
        screen.blit(bg_mh, (0, 0))

        # tombol navigasi
        screen.blit(btn_kembali, btn_kembali_rect)
        screen.blit(btn_back, btn_back_rect)
        screen.blit(btn_next, btn_next_rect)

        # pilih buah bergantian berdasarkan level (Choice A)
        fruit_img = fruit_list[(menghitung_level - 1) % len(fruit_list)]

        # pengaturan tata letak buah (max 5 per baris => 2 baris jika >5)
        max_per_row = 5
        base_x = 150
        base_y = 120
        spacing_x = 70
        spacing_y = 80

        for index in range(menghitung_level):
            row = index // max_per_row      # 0 atau 1
            col = index % max_per_row       # 0 → 4
            x = base_x + col * spacing_x
            y = base_y + row * spacing_y
            screen.blit(fruit_img, (x, y))

        # tampilkan angka di kanan
        angka_img = angka_images[menghitung_level]
        angka_rect = angka_img.get_rect(center=(SCREEN_WIDTH - 200, SCREEN_HEIGHT // 2))
        screen.blit(angka_img, angka_rect)

    # ---------------------------
    # MODE PENJUMLAHAN
    # ---------------------------
    elif current_state == STATE_PENJUMLAHAN:
        screen.blit(bg_pj, (0, 0))

        # tampil soal
        soal_img = soal_pj[current_pj_level]
        rect = soal_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(soal_img, rect)

        # countdown (safety: ensure countdown_start set)
        if countdown_start is None:
            countdown_start = pygame.time.get_ticks()

        elapsed = (pygame.time.get_ticks() - countdown_start) // 1000
        remaining = countdown_duration - elapsed

        if remaining > 0:
            img = countdown_imgs.get(max(1, remaining))
            if img:
                screen.blit(img, (10, 10))
        else:
            current_pj_level += 1
            if current_pj_level >= 10:
                current_state = STATE_DASHBOARD
                countdown_start = None
            else:
                countdown_start = pygame.time.get_ticks()

    # ---------------------------
    # MODE PENGURANGAN
    # ---------------------------
    elif current_state == STATE_PENGURANGAN:
        screen.blit(bg_pg, (0, 0))

        soal_img = soal_pg[current_pg_level]
        rect = soal_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(soal_img, rect)

        if countdown_start is None:
            countdown_start = pygame.time.get_ticks()

        elapsed = (pygame.time.get_ticks() - countdown_start) // 1000
        remaining = countdown_duration - elapsed

        if remaining > 0:
            img = countdown_imgs.get(max(1, remaining))
            if img:
                screen.blit(img, (10, 10))
        else:
            current_pg_level += 1
            if current_pg_level >= 10:
                current_state = STATE_DASHBOARD
                countdown_start = None
            else:
                countdown_start = pygame.time.get_ticks()

    pygame.display.update()
