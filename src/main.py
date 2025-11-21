import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FunCount")

# LOAD ASSETS

dashboard = pygame.image.load("assets/bg_utama.png").convert_alpha()
dashboard = pygame.transform.scale(dashboard, (SCREEN_WIDTH, SCREEN_HEIGHT))

dashboard_blur = pygame.image.load("assets/bg_utama_blur.png").convert_alpha()
dashboard_blur = pygame.transform.scale(dashboard_blur, (SCREEN_WIDTH, SCREEN_HEIGHT))

welcome_img = pygame.image.load("assets/welcome.png").convert_alpha()
welcome_img = pygame.transform.scale(welcome_img, (500, 170))
welcome_rect = welcome_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))

# Background halaman masing-masing mode
bg_mh = pygame.image.load("assets/bg_menghitung.png").convert_alpha()
bg_mh = pygame.transform.scale(bg_mh, (SCREEN_WIDTH, SCREEN_HEIGHT))

bg_pj = pygame.image.load("assets/bg_penjumlahan.png").convert_alpha()
bg_pj = pygame.transform.scale(bg_pj, (SCREEN_WIDTH, SCREEN_HEIGHT))

bg_pg = pygame.image.load("assets/bg_pengurangan.png").convert_alpha()
bg_pg = pygame.transform.scale(bg_pg, (SCREEN_WIDTH, SCREEN_HEIGHT))


# START BUTTON
button_start_original = pygame.image.load("assets/button_start.png").convert_alpha()

SMALL_SIZE = (200, 100)
BIG_SIZE = (300, 150)

button_start_small = pygame.transform.scale(button_start_original, SMALL_SIZE)
button_start_big = pygame.transform.scale(button_start_original, BIG_SIZE)

button_start = button_start_small
button_start_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))


# DASHBOARD MODE BUTTONS
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

btn_mh_rect = btn_mh.get_rect(center=(SCREEN_WIDTH // 2, 130))
btn_pj_rect = btn_pj.get_rect(center=(SCREEN_WIDTH // 2, 250))
btn_pg_rect = btn_pg.get_rect(center=(SCREEN_WIDTH // 2, 370))


# STATE SYSTEM
STATE_MENU_AWAL = 0
STATE_DASHBOARD = 1
STATE_MENGHITUNG = 2
STATE_PENJUMLAHAN = 3
STATE_PENGURANGAN = 4

current_state = STATE_MENU_AWAL


# =====================================
# COUNTDOWN ASSET SYSTEM
# =====================================
countdown_imgs = {}

for i in range(1, 11):
    img = pygame.image.load(f"assets/angka_{i}.png").convert_alpha()
    countdown_imgs[i] = pygame.transform.scale(img, (50, 50))

countdown_start = None
countdown_duration = 10  # 10 detik


# =====================================
# GAME LOOP
# =====================================
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # MENU AWAL
        if current_state == STATE_MENU_AWAL:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_start_rect.collidepoint(mouse_pos):
                    current_state = STATE_DASHBOARD

        # DASHBOARD
        elif current_state == STATE_DASHBOARD:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if btn_mh_rect.collidepoint(mouse_pos):
                    current_state = STATE_MENGHITUNG

                elif btn_pj_rect.collidepoint(mouse_pos):
                    current_state = STATE_PENJUMLAHAN
                    countdown_start = pygame.time.get_ticks()

                elif btn_pg_rect.collidepoint(mouse_pos):
                    current_state = STATE_PENGURANGAN
                    countdown_start = pygame.time.get_ticks()


    # =============== MENU AWAL ===============
    if current_state == STATE_MENU_AWAL:

        if button_start_rect.collidepoint(mouse_pos):
            button_start = button_start_big
        else:
            button_start = button_start_small

        button_start_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

        screen.blit(dashboard, (0, 0))
        screen.blit(welcome_img, welcome_rect)
        screen.blit(button_start, button_start_rect)


    # =============== DASHBOARD ===============
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


    # =============== MODE MENGHITUNG ===============
    elif current_state == STATE_MENGHITUNG:
        screen.blit(bg_mh, (0, 0))


    # =============== MODE PENJUMLAHAN ===============
    elif current_state == STATE_PENJUMLAHAN:

        screen.blit(bg_pj, (0, 0))

        elapsed = (pygame.time.get_ticks() - countdown_start) // 1000
        remaining = 10 - elapsed

        if remaining > 0:
            img = countdown_imgs.get(remaining)
            rect = img.get_rect(topleft=(10, 10))   # pojok kiri atas
            screen.blit(img, rect)
        else:
            current_state = STATE_DASHBOARD


    # =============== MODE PENGURANGAN ===============
    elif current_state == STATE_PENGURANGAN:

        screen.blit(bg_pg, (0, 0))

        elapsed = (pygame.time.get_ticks() - countdown_start) // 1000
        remaining = 10 - elapsed

        if remaining > 0:
            img = countdown_imgs.get(remaining)
            rect = img.get_rect(topleft=(10, 10))   # pojok kiri atas
            screen.blit(img, rect)
        else:
            current_state = STATE_DASHBOARD


    pygame.display.update()
