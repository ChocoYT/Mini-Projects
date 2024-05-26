import pygame

pygame.init()

screen_width = 1000
screen_height = 800
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Test")

def create_hexagon(size):
    if size % 2 == 0:
        pass
    else:
        pass

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((10, 10, 10))
    create_hexagon(3)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()