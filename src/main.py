import pygame
import sys
import random
import math

pygame.init()

# =====================================
# WINDOW
# =====================================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FunCount")

# =====================================
# LOAD ASSETS UMUM
# =====================================

dashboard = pygame.image.load("assets/bg_utama.png").convert_alpha()
dashboard = pygame.transform.scale(dashboard, (SCREEN_WIDTH, SCREEN_HEIGHT))

dashboard_blur = pygame.image.load("assets/bg_utama_blur.png").convert_alpha()
dashboard_blur = pygame.transform.scale(dashboard_blur, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Welcome banner besar
welcome_img = pygame.image.load("assets/welcome.png").convert_alpha()
welcome_img = pygame.transform.scale(welcome_img, (650, 200))
welcome_rect = welcome_img.get_rect(center=(SCREEN_WIDTH // 2, 120))

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

# initial set to small; we'll choose big on hover in rendering
button_start = button_start_small
button_start_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

# =====================================
# DASHBOARD / MENU BUTTONS
# =====================================
btn_mh_original = pygame.image.load("assets/button_menghitung.png").convert_alpha()
btn_pj_original = pygame.image.load("assets/button_penjumlahan.png").convert_alpha()
btn_pg_original = pygame.image.load("assets/button_pengurangan.png").convert_alpha()

btn_mh_small = pygame.transform.scale(btn_mh_original, SMALL_SIZE)
btn_mh_big   = pygame.transform.scale(btn_mh_original, BIG_SIZE)

btn_pj_small = pygame.transform.scale(btn_pj_original, SMALL_SIZE)
btn_pj_big   = pygame.transform.scale(btn_pj_original, BIG_SIZE)

btn_pg_small = pygame.transform.scale(btn_pg_original, SMALL_SIZE)
btn_pg_big   = pygame.transform.scale(btn_pg_original, BIG_SIZE)

btn_mh = btn_mh_small
btn_pj = btn_pj_small
btn_pg = btn_pg_small

# posisi awal (nanti akan di-update setiap frame)
btn_mh_rect = btn_mh.get_rect(center=(SCREEN_WIDTH // 2 - 220, 300))
btn_pj_rect = btn_pj.get_rect(center=(SCREEN_WIDTH // 2,       300))
btn_pg_rect = btn_pg.get_rect(center=(SCREEN_WIDTH // 2 + 220, 300))

# =====================================
# STATE SYSTEM
# =====================================
STATE_MENU_AWAL      = 0
STATE_DASHBOARD      = 1   # sekarang tidak dipakai, tapi dibiarkan saja
STATE_MENGHITUNG     = 2
STATE_PENJUMLAHAN    = 3
STATE_PENGURANGAN    = 4
STATE_POPUP_WIN      = 5
STATE_POPUP_LOSE     = 6

current_state = STATE_MENU_AWAL
last_quiz_mode = "pj"   # "pj" atau "pg" untuk popup

# =====================================
# BELAJAR MENGHITUNG (1–10)
# =====================================
apple_img = pygame.image.load("assets/apple_transparent.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img, (100, 100))

banana_img = pygame.image.load("assets/banana_transparent.png").convert_alpha()
banana_img = pygame.transform.scale(banana_img, (100, 100))

fruit_list = [apple_img, banana_img]

angka_images = {}
for i in range(1, 11):
    img = pygame.image.load(f"assets/angka_{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (150, 150))
    angka_images[i] = img

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
# SOAL PENJUMLAHAN
# =====================================
soal_pj = []
for i in range(1, 11):
    img = pygame.image.load(f"assets/soalPenjumlahan{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (430, 210))
    soal_pj.append(img)

current_pj_level = 0

# jawaban benar penjumlahan
jumlah_jawaban_benar = [2, 3, 3, 4, 4, 4, 5, 6, 6, 8]

# tombol angka hijau (button_1–button_10)
button_nums = []
for i in range(1, 11):
    img = pygame.image.load(f"assets/button_{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (150, 80))
    button_nums.append(img)

# posisi tiga tombol jawaban (berjejer)
PJ_BUTTON_POSITIONS = [(200, 320), (400, 320), (600, 320)]
pj_button_rects = [None, None, None]
pj_hover_alpha = [0, 0, 0]  # untuk efek glow halus

# =====================================
# SKOR DAN NYAWA (GAMBAR)
# =====================================
nilai_images = {}  # key: skor 10,20,...,100
for score in range(10, 110, 10):
    img = pygame.image.load(f"assets/nilai{score}.png").convert_alpha()
    img = pygame.transform.scale(img, (100, 100))
    nilai_images[score] = img

lives_images = []
for i in range(0, 4):
    img = pygame.image.load(f"assets/lives_{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (200, 70))
    lives_images.append(img)

# popup messages
msg_win_img  = pygame.image.load("assets/show_message_win.png").convert_alpha()
msg_win_img  = pygame.transform.scale(msg_win_img, (600, 230))
msg_lose_img = pygame.image.load("assets/show_message_lose.png").convert_alpha()
msg_lose_img = pygame.transform.scale(msg_lose_img, (600, 230))

popup_start_time = None
POPUP_DURATION   = 2000  # ms

# =====================================
# LOGIC PENJUMLAHAN
# =====================================
pj_score      = 0
pj_lives      = 3
pj_mistakes   = 0   # berapa kali salah
pj_choices    = []  # list 3 angka pilihan
pj_time_start = None
PJ_TIME_LIMIT = 10  # detik

# =====================================
# SOAL PENGURANGAN
# =====================================
soal_pg = []
for i in range(1, 11):
    img = pygame.image.load(f"assets/soalPengurangan{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (430, 210))
    soal_pg.append(img)

# Jawaban benar pengurangan:
# 1) 1 - 1 = 0
# 2) 2 - 1 = 1
# 3) 3 - 2 = 1
# 4) 4 - 2 = 2
# 5) 5 - 3 = 2
# 6) 6 - 3 = 3
# 7) 6 - 4 = 2
# 8) 9 - 5 = 4
# 9) 10 - 5 = 5
pg_correct_answers   = [0, 1, 1, 2, 2, 3, 2, 4, 5]
PG_TOTAL_QUESTIONS   = len(pg_correct_answers)
PG_TIME_LIMIT        = 10

current_pg_level = 0
pg_score         = 0
pg_lives         = 3
pg_mistakes      = 0
pg_choices       = []
pg_time_start    = None
pg_button_rects  = [None, None, None]
pg_hover_alpha   = [0, 0, 0]

# Tombol khusus angka 0 (karena tidak ada asset button_0.png)
zero_button = pygame.Surface((150, 80), pygame.SRCALPHA)
pygame.draw.rect(zero_button, (48, 210, 80), zero_button.get_rect(), border_radius=40)
font_zero = pygame.font.Font(None, 72)
text0 = font_zero.render("0", True, (255, 255, 255))
zero_button.blit(text0, text0.get_rect(center=zero_button.get_rect().center))

# =====================================
# COUNTDOWN IMAGES (dipakai PJ & PG)
# =====================================
countdown_imgs = {}
for i in range(1, 11):
    img = pygame.image.load(f"assets/angka_{i}.png").convert_alpha()
    countdown_imgs[i] = pygame.transform.scale(img, (50, 50))

# =====================================
# FUNGSI BANTUAN
# =====================================
def generate_choices(correct):
    """Bikin 3 pilihan jawaban (1 benar + 2 salah acak, rentang 0..10)."""
    options = [correct]
    while len(options) < 3:
        r = random.randint(0, 10)
        if r not in options:
            options.append(r)
    random.shuffle(options)
    return options

def reset_penjumlahan_to_dashboard():
    """Sekarang balik ke MENU_AWAL (bukan dashboard blur lagi)."""
    global current_state, pj_score, pj_lives, pj_mistakes
    global current_pj_level, pj_choices, pj_time_start, pj_hover_alpha
    current_state     = STATE_MENU_AWAL
    pj_score          = 0
    pj_lives          = 3
    pj_mistakes       = 0
    current_pj_level  = 0
    pj_choices        = []
    pj_time_start     = None
    pj_hover_alpha    = [0, 0, 0]

def reset_pengurangan_to_dashboard():
    """Sekarang balik ke MENU_AWAL (bukan dashboard blur lagi)."""
    global current_state, pg_score, pg_lives, pg_mistakes
    global current_pg_level, pg_choices, pg_time_start, pg_hover_alpha
    current_state     = STATE_MENU_AWAL
    pg_score          = 0
    pg_lives          = 3
    pg_mistakes       = 0
    current_pg_level  = 0
    pg_choices        = []
    pg_time_start     = None
    pg_hover_alpha    = [0, 0, 0]

# =====================================
# GAME LOOP
# =====================================
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ---------------------------
        # MENU AWAL (SEKARANG SEBAGAI MAIN MENU)
        # ---------------------------
        if current_state == STATE_MENU_AWAL:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # hanya start button yang aktif di main menu
                # gunakan button_start_rect (rect dikalkulasi di rendering karena bisa berubah ukuran saat hover)
                if button_start_rect.collidepoint(mouse_pos):
                    # masuk ke dashboard blur dengan 3 tombol
                    current_state = STATE_DASHBOARD

        # ---------------------------
        # DASHBOARD (TIDAK DIPAKAI, DIBIARKAN SAJA)
        # ---------------------------
        elif current_state == STATE_DASHBOARD:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_mh_rect.collidepoint(mouse_pos):
                    current_state = STATE_MENGHITUNG
                    menghitung_level = 1

                elif btn_pj_rect.collidepoint(mouse_pos):
                    current_state    = STATE_PENJUMLAHAN
                    current_pj_level = 0
                    pj_score         = 0
                    pj_lives         = 3
                    pj_mistakes      = 0
                    pj_choices       = []
                    pj_time_start    = None
                    pj_hover_alpha   = [0, 0, 0]

                elif btn_pg_rect.collidepoint(mouse_pos):
                    current_state    = STATE_PENGURANGAN
                    current_pg_level = 0
                    pg_score         = 0
                    pg_lives         = 3
                    pg_mistakes      = 0
                    pg_choices       = []
                    pg_time_start    = None
                    pg_hover_alpha   = [0, 0, 0]

        # ---------------------------
        # BELAJAR MENGHITUNG
        # ---------------------------
        elif current_state == STATE_MENGHITUNG:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_kembali_rect.collidepoint(mouse_pos):
                    current_state = STATE_MENU_AWAL

                elif btn_back_rect.collidepoint(mouse_pos):
                    menghitung_level -= 1
                    if menghitung_level < 1:
                        menghitung_level = 1

                elif btn_next_rect.collidepoint(mouse_pos):
                    menghitung_level += 1
                    if menghitung_level > 10:
                        menghitung_level = 10

        # ---------------------------
        # PENJUMLAHAN (CLICK JAWABAN)
        # ---------------------------
        elif current_state == STATE_PENJUMLAHAN:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for idx, rect in enumerate(pj_button_rects):
                    if rect and rect.collidepoint(mouse_pos) and pj_choices:
                        chosen_value = pj_choices[idx]
                        correct      = jumlah_jawaban_benar[current_pj_level]

                        # cek benar / salah
                        if chosen_value == correct:
                            pj_score += 10
                        else:
                            pj_mistakes += 1
                            pj_lives = max(3 - pj_mistakes, 0)

                        # cek game over (salah ke-4)
                        if pj_mistakes > 3:
                            last_quiz_mode  = "pj"
                            current_state    = STATE_POPUP_LOSE
                            popup_start_time = pygame.time.get_ticks()
                        else:
                            # lanjut soal berikutnya
                            current_pj_level += 1
                            if current_pj_level >= len(jumlah_jawaban_benar):
                                # sudah habis soal
                                if pj_score == 100:
                                    last_quiz_mode  = "pj"
                                    current_state    = STATE_POPUP_WIN
                                    popup_start_time = pygame.time.get_ticks()
                                else:
                                    reset_penjumlahan_to_dashboard()
                            else:
                                pj_choices     = []
                                pj_time_start  = None
                                pj_hover_alpha = [0, 0, 0]
                        break

        # ---------------------------
        # PENGURANGAN (CLICK JAWABAN)
        # ---------------------------
        elif current_state == STATE_PENGURANGAN:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for idx, rect in enumerate(pg_button_rects):
                    if rect and rect.collidepoint(mouse_pos) and pg_choices:
                        chosen_value = pg_choices[idx]
                        correct      = pg_correct_answers[current_pg_level]

                        if chosen_value == correct:
                            pg_score += 10
                        else:
                            pg_mistakes += 1
                            pg_lives = max(3 - pg_mistakes, 0)

                        if pg_mistakes > 3:
                            last_quiz_mode  = "pg"
                            current_state    = STATE_POPUP_LOSE
                            popup_start_time = pygame.time.get_ticks()
                        else:
                            current_pg_level += 1
                            if current_pg_level >= PG_TOTAL_QUESTIONS:
                                max_score = PG_TOTAL_QUESTIONS * 10
                                if pg_score == max_score:
                                    last_quiz_mode  = "pg"
                                    current_state    = STATE_POPUP_WIN
                                    popup_start_time = pygame.time.get_ticks()
                                else:
                                    reset_pengurangan_to_dashboard()
                            else:
                                pg_choices     = []
                                pg_time_start  = None
                                pg_hover_alpha = [0, 0, 0]
                        break

        # Popup states tidak perlu handle click

    # =====================================
    # RENDERING
    # =====================================

    # ---------------------------
    # MENU AWAL (MAIN MENU)
    # ---------------------------
    if current_state == STATE_MENU_AWAL:
        # background biasa (dashboard)
        screen.blit(dashboard, (0, 0))

        # Welcome banner di atas
        screen.blit(welcome_img, welcome_rect)

        # START button (hover scale -> small/big)
        # pilih gambar berdasarkan hover
        # gunakan posisi center tetap (SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 40)
        if button_start_small.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)).collidepoint(mouse_pos):
            button_start_draw = button_start_big
        else:
            button_start_draw = button_start_small

        # recompute rect based on chosen size so collision check tetap akurat
        button_start_rect = button_start_draw.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        screen.blit(button_start_draw, button_start_rect)

    # ---------------------------
    # DASHBOARD (JARANG DIPAKAI)
    # ---------------------------
    elif current_state == STATE_DASHBOARD:
        screen.blit(dashboard_blur, (0, 0))

        # pilih gambar berdasarkan hover (tetap)
        btn_mh_draw = btn_mh_big if btn_mh_rect.collidepoint(mouse_pos) else btn_mh_small
        btn_pj_draw = btn_pj_big if btn_pj_rect.collidepoint(mouse_pos) else btn_pj_small
        btn_pg_draw = btn_pg_big if btn_pg_rect.collidepoint(mouse_pos) else btn_pg_small

        # ========= POSISI BARU (VERTIKAL SIMETRIS + TENGAH) =========
        spacing = 90  # jarak antar tombol

        center_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2 - spacing  # biar 3 tombol centered

        btn_mh_rect = btn_mh_draw.get_rect(center=(center_x, start_y + spacing * -0.2))
        btn_pj_rect = btn_pj_draw.get_rect(center=(center_x, start_y + spacing))
        btn_pg_rect = btn_pg_draw.get_rect(center=(center_x, start_y + spacing * 2.2))

        # gambar tombol
        screen.blit(btn_mh_draw, btn_mh_rect)
        screen.blit(btn_pj_draw, btn_pj_rect)
        screen.blit(btn_pg_draw, btn_pg_rect)

    # ---------------------------
    # MODE BELAJAR MENGHITUNG
    # ---------------------------
    elif current_state == STATE_MENGHITUNG:
        screen.blit(bg_mh, (0, 0))

        screen.blit(btn_kembali, btn_kembali_rect)
        screen.blit(btn_back, btn_back_rect)
        screen.blit(btn_next, btn_next_rect)

        fruit_img = fruit_list[(menghitung_level - 1) % len(fruit_list)]

        max_per_row = 5
        base_x      = 150
        base_y      = 120
        spacing_x   = 85
        spacing_y   = 100

        for index in range(menghitung_level):
            row = index // max_per_row
            col = index % max_per_row
            x   = base_x + col * spacing_x
            y   = base_y + row * spacing_y
            screen.blit(fruit_img, (x, y))

        angka_img  = angka_images[menghitung_level]
        angka_rect = angka_img.get_rect(center=(SCREEN_WIDTH - 200, SCREEN_HEIGHT // 2))
        screen.blit(angka_img, angka_rect)

    # ---------------------------
    # MODE PENJUMLAHAN
    # ---------------------------
    elif current_state == STATE_PENJUMLAHAN:
        screen.blit(bg_pj, (0, 0))

        if current_pj_level >= len(jumlah_jawaban_benar):
            reset_penjumlahan_to_dashboard()
        else:
            soal_img  = soal_pj[current_pj_level]
            soal_rect = soal_img.get_rect(center=(SCREEN_WIDTH // 2, 150))
            screen.blit(soal_img, soal_rect)

            if not pj_choices or pj_time_start is None:
                correct       = jumlah_jawaban_benar[current_pj_level]
                pj_choices    = generate_choices(correct)
                pj_time_start = pygame.time.get_ticks()
                pj_hover_alpha = [0, 0, 0]

            pj_button_rects = []
            for idx, value in enumerate(pj_choices):
                btn_img = button_nums[value - 1]
                cx, cy  = PJ_BUTTON_POSITIONS[idx]
                rect    = btn_img.get_rect(center=(cx, cy))
                pj_button_rects.append(rect)
                screen.blit(btn_img, rect)

                if rect.collidepoint(mouse_pos):
                    target_alpha = 140
                else:
                    target_alpha = 0

                if pj_hover_alpha[idx] < target_alpha:
                    pj_hover_alpha[idx] = min(target_alpha, pj_hover_alpha[idx] + 15)
                elif pj_hover_alpha[idx] > target_alpha:
                    pj_hover_alpha[idx] = max(target_alpha, pj_hover_alpha[idx] - 15)

                if pj_hover_alpha[idx] > 0:
                    overlay = pygame.Surface(rect.size, pygame.SRCALPHA)
                    overlay.fill((255, 255, 255, pj_hover_alpha[idx]))
                    screen.blit(overlay, rect.topleft)

            if pj_score > 0 and pj_score in nilai_images:
                nilai_img  = nilai_images[pj_score]
                nilai_rect = nilai_img.get_rect(topright=(SCREEN_WIDTH - 20, 10))
                screen.blit(nilai_img, nilai_rect)

            lives_index = max(0, min(3, pj_lives))
            lives_img   = lives_images[lives_index]
            screen.blit(lives_img, (20, 10))

            elapsed   = (pygame.time.get_ticks() - pj_time_start) // 1000
            remaining = PJ_TIME_LIMIT - elapsed

            if remaining > 0:
                r       = max(1, min(10, remaining))
                cd_img  = countdown_imgs.get(r)
                cd_rect = cd_img.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
                screen.blit(cd_img, cd_rect)
            else:
                pj_mistakes += 1
                pj_lives = max(3 - pj_mistakes, 0)

                if pj_mistakes > 3:
                    last_quiz_mode  = "pj"
                    current_state    = STATE_POPUP_LOSE
                    popup_start_time = pygame.time.get_ticks()
                else:
                    current_pj_level += 1
                    if current_pj_level >= len(jumlah_jawaban_benar):
                        if pj_score == 100:
                            last_quiz_mode  = "pj"
                            current_state    = STATE_POPUP_WIN
                            popup_start_time = pygame.time.get_ticks()
                        else:
                            reset_penjumlahan_to_dashboard()
                    else:
                        pj_choices     = []
                        pj_time_start  = None
                        pj_hover_alpha = [0, 0, 0]

    # ---------------------------
    # MODE PENGURANGAN
    # ---------------------------
    elif current_state == STATE_PENGURANGAN:
        screen.blit(bg_pg, (0, 0))

        if current_pg_level >= PG_TOTAL_QUESTIONS:
            reset_pengurangan_to_dashboard()
        else:
            soal_img  = soal_pg[current_pg_level]
            soal_rect = soal_img.get_rect(center=(SCREEN_WIDTH // 2, 150))
            screen.blit(soal_img, soal_rect)

            if not pg_choices or pg_time_start is None:
                correct       = pg_correct_answers[current_pg_level]
                pg_choices    = generate_choices(correct)
                pg_time_start = pygame.time.get_ticks()
                pg_hover_alpha = [0, 0, 0]

            pg_button_rects = []
            for idx, value in enumerate(pg_choices):
                if value == 0:
                    btn_img = zero_button
                else:
                    btn_img = button_nums[value - 1]
                cx, cy  = PJ_BUTTON_POSITIONS[idx]
                rect    = btn_img.get_rect(center=(cx, cy))
                pg_button_rects.append(rect)
                screen.blit(btn_img, rect)

                if rect.collidepoint(mouse_pos):
                    target_alpha = 140
                else:
                    target_alpha = 0

                if pg_hover_alpha[idx] < target_alpha:
                    pg_hover_alpha[idx] = min(target_alpha, pg_hover_alpha[idx] + 15)
                elif pg_hover_alpha[idx] > target_alpha:
                    pg_hover_alpha[idx] = max(target_alpha, pg_hover_alpha[idx] - 15)

                if pg_hover_alpha[idx] > 0:
                    overlay = pygame.Surface(rect.size, pygame.SRCALPHA)
                    overlay.fill((255, 255, 255, pg_hover_alpha[idx]))
                    screen.blit(overlay, rect.topleft)

            if pg_score > 0 and pg_score in nilai_images:
                nilai_img  = nilai_images[pg_score]
                nilai_rect = nilai_img.get_rect(topright=(SCREEN_WIDTH - 20, 10))
                screen.blit(nilai_img, nilai_rect)

            lives_index = max(0, min(3, pg_lives))
            lives_img   = lives_images[lives_index]
            screen.blit(lives_img, (20, 10))

            elapsed   = (pygame.time.get_ticks() - pg_time_start) // 1000
            remaining = PG_TIME_LIMIT - elapsed

            if remaining > 0:
                r       = max(1, min(10, remaining))
                cd_img  = countdown_imgs.get(r)
                cd_rect = cd_img.get_rect(midtop=(SCREEN_WIDTH // 2, 10))
                screen.blit(cd_img, cd_rect)
            else:
                pg_mistakes += 1
                pg_lives = max(3 - pg_mistakes, 0)

                if pg_mistakes > 3:
                    last_quiz_mode  = "pg"
                    current_state    = STATE_POPUP_LOSE
                    popup_start_time = pygame.time.get_ticks()
                else:
                    current_pg_level += 1
                    if current_pg_level >= PG_TOTAL_QUESTIONS:
                        max_score = PG_TOTAL_QUESTIONS * 10
                        if pg_score == max_score:
                            last_quiz_mode  = "pg"
                            current_state    = STATE_POPUP_WIN
                            popup_start_time = pygame.time.get_ticks()
                        else:
                            reset_pengurangan_to_dashboard()
                    else:
                        pg_choices     = []
                        pg_time_start  = None
                        pg_hover_alpha = [0, 0, 0]

    # ---------------------------
    # POPUP WIN
    # ---------------------------
    elif current_state == STATE_POPUP_WIN:
        # background menyesuaikan mode terakhir
        if last_quiz_mode == "pj":
            screen.blit(bg_pj, (0, 0))
        else:
            screen.blit(bg_pg, (0, 0))

        elapsed = pygame.time.get_ticks() - popup_start_time
        t = max(0.0, min(1.0, elapsed / POPUP_DURATION))

        alpha = int(255 * t)
        scale = 1.0 + 0.05 * math.sin(t * math.pi)

        base_w, base_h = msg_win_img.get_size()
        draw_w = int(base_w * scale)
        draw_h = int(base_h * scale)
        popup_surf = pygame.transform.smoothscale(msg_win_img, (draw_w, draw_h))
        popup_surf.set_alpha(alpha)

        popup_rect = popup_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(popup_surf, popup_rect)

        center_x, center_y = popup_rect.center
        max_radius = 120
        for i in range(10):
            angle = (2 * math.pi / 10) * i
            radius = t * max_radius
            sx = int(center_x + math.cos(angle) * radius)
            sy = int(center_y + math.sin(angle) * radius)
            pygame.draw.line(screen, (255, 255, 255), (sx - 5, sy), (sx + 5, sy), 2)
            pygame.draw.line(screen, (255, 255, 255), (sx, sy - 5), (sx, sy + 5), 2)

        if elapsed >= POPUP_DURATION:
            if last_quiz_mode == "pj":
                reset_penjumlahan_to_dashboard()
            else:
                reset_pengurangan_to_dashboard()

    # ---------------------------
    # POPUP LOSE
    # ---------------------------
    elif current_state == STATE_POPUP_LOSE:
        if last_quiz_mode == "pj":
            screen.blit(bg_pj, (0, 0))
        else:
            screen.blit(bg_pg, (0, 0))

        elapsed = pygame.time.get_ticks() - popup_start_time
        t = max(0.0, min(1.0, elapsed / POPUP_DURATION))

        alpha = int(255 * t)
        amplitude = (1.0 - t) * 10

        base_w, base_h = msg_lose_img.get_size()
        popup_surf = msg_lose_img.copy()
        popup_surf.set_alpha(alpha)

        dx = math.sin(elapsed * 0.03) * amplitude
        popup_rect = popup_surf.get_rect(center=(SCREEN_WIDTH // 2 + dx, SCREEN_HEIGHT // 2))
        screen.blit(popup_surf, popup_rect)

        if elapsed >= POPUP_DURATION:
            if last_quiz_mode == "pj":
                reset_penjumlahan_to_dashboard()
            else:
                reset_pengurangan_to_dashboard()

    pygame.display.update()
