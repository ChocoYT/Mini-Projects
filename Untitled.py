import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 800
FPS = 60

print(pygame.font.get_fonts())

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Untitled")
clock = pygame.time.Clock()

text_font = pygame.font.SysFont("segoescript", 30, bold = False, italic = False)

def draw_text(text, font, text_col, pos):
    text_image = font.render(text, True, text_col)
    screen.blit(text_image, (pos))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    r_mouse, m_mouse, l_mouse = pygame.mouse.get_pressed(3)

    screen.fill((15, 15, 15))

    draw_text("Text", text_font, (255, 255, 255), (0, 0))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
