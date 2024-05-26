import pygame
import keyboard

pygame.init()

screen_width = 1000
screen_height = 800
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

class Snake():
    def __init__ (self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.length = 3
        self.speed = 2
    
    def move(self, speed):
        pass

    def draw_tile(self, pos, col, size):
        # Creates the Surface
        self.surface = pygame.Surface((size, size))
        self.surface.fill(col)
        self.draw_x, self.draw_y = pos
        
        # Centres the Tile
        self.draw_x -= size / 2
        self.draw_y -= size / 2

        pos = (self.draw_x, self.draw_y)
        screen.blit(self.surface, pos)

def check_if_pressed(key):
    for i in range(len(key)):
        if keyboard.is_pressed(key[i]):
            if key[i] not in keys: 
                keys.append(key[i])
        elif key[i] in keys:
            keys.remove(key[i])

keys = []
snake = Snake()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    r_mouse, m_mouse, l_mouse = pygame.mouse.get_pressed(3)

    screen.fill((15, 15, 15))

    check_if_pressed(["W", "A", "S", "D"])
    snake.move(snake.speed)
    snake.draw_tile((snake.x, snake.y), (255, 255, 255), 40)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
