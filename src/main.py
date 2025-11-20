import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FunCount")

# =====================
# LOAD ASSETS
# =====================

dashboard = pygame.image.load("assets/dashboard.png").convert_alpha()
dashboard = pygame.transform.scale(dashboard, (SCREEN_WIDTH, SCREEN_HEIGHT))

dashboard_blur = pygame.image.load("assets/dashboard_blur.png").convert_alpha()
dashboard_blur = pygame.transform.scale(dashboard_blur, (SCREEN_WIDTH, SCREEN_HEIGHT))

welcome_img = pygame.image.load("assets/welcome.png").convert_alpha()
welcome_img = pygame.transform.scale(welcome_img, (500, 170))
welcome_rect = welcome_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120))

# =====================
# START BUTTON
# =====================

button_start_original = pygame.image.load("assets/button_start.png").convert_alpha()

SMALL_SIZE = (200, 100)
BIG_SIZE = (300, 150)

button_start_small = pygame.transform.scale(button_start_original, SMALL_SIZE)
button_start_big = pygame.transform.scale(button_start_original, BIG_SIZE)

button_start = button_start_small
button_start_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

# =====================
# DASHBOARD MODE BUTTONS
# =====================

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

# Initial positions (centered)
btn_mh_rect = btn_mh.get_rect(center=(SCREEN_WIDTH // 2, 130))
btn_pj_rect = btn_pj.get_rect(center=(SCREEN_WIDTH // 2, 250))
btn_pg_rect = btn_pg.get_rect(center=(SCREEN_WIDTH // 2, 370))

# =====================
# STATE SYSTEM
# =====================

STATE_MENU_AWAL = 0
STATE_DASHBOARD_MODE = 1
current_state = STATE_MENU_AWAL

# =====================
# GAME LOOP
# =====================

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
                    print("Start clicked!")
                    current_state = STATE_DASHBOARD_MODE

        # DASHBOARD MODE
        elif current_state == STATE_DASHBOARD_MODE:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_mh_rect.collidepoint(mouse_pos):
                    print("Mode Menghitung dipilih!")
                if btn_pj_rect.collidepoint(mouse_pos):
                    print("Mode Penjumlahan dipilih!")
                if btn_pg_rect.collidepoint(mouse_pos):
                    print("Mode Pengurangan dipilih!")

    # ==========================
    # RENDER MENU AWAL
    # ==========================
    if current_state == STATE_MENU_AWAL:

        # Hover effect for start button
        if button_start_rect.collidepoint(mouse_pos):
            button_start = button_start_big
        else:
            button_start = button_start_small

        button_start_rect = button_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))

        screen.blit(dashboard, (0, 0))
        screen.blit(welcome_img, welcome_rect)
        screen.blit(button_start, button_start_rect)

    # ==========================
    # RENDER DASHBOARD MODE
    # ==========================
    elif current_state == STATE_DASHBOARD_MODE:

        screen.blit(dashboard_blur, (0, 0))

        # Hover effects for all buttons
        if btn_mh_rect.collidepoint(mouse_pos):
            btn_mh = btn_mh_big
        else:
            btn_mh = btn_mh_small

        if btn_pj_rect.collidepoint(mouse_pos):
            btn_pj = btn_pj_big
        else:
            btn_pj = btn_pj_small

        if btn_pg_rect.collidepoint(mouse_pos):
            btn_pg = btn_pg_big
        else:
            btn_pg = btn_pg_small

        # Keep centers in place
        btn_mh_rect = btn_mh.get_rect(center=(SCREEN_WIDTH // 2, 130))
        btn_pj_rect = btn_pj.get_rect(center=(SCREEN_WIDTH // 2, 250))
        btn_pg_rect = btn_pg.get_rect(center=(SCREEN_WIDTH // 2, 370))

        # Draw buttons
        screen.blit(btn_mh, btn_mh_rect)
        screen.blit(btn_pj, btn_pj_rect)
        screen.blit(btn_pg, btn_pg_rect)

    pygame.display.update()
