import keyboard
import math
import pygame
import sys

pygame.init()

screenWidth = 1000
screenHeight = 800
FPS = 60

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Shape Simulation")
clock = pygame.time.Clock()

class Shape(pygame.sprite.Sprite):
    def __init__(self, points: int, pos: tuple | list, size: int | float, colour: tuple | list, direction: int | float) -> None:
        super().__init__()

        # Initialises the class Shape
        self.points = points
        self.x, self.y = pos
        self.size = size
        self.colour = colour
        self.direction = direction

        self.xVel = 0
        self.yVel = 0

        self.pointSize = 10
        self.lineSize = 5

        self.radius = self.pointSize / 2
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.surface, self.colour, (self.radius, self.radius), self.radius)

        self.image = pygame.Surface((0, 0))
        self.update()

        # Sprite attributes
        self.image = self.draw(screen)
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.shape = []

        # Iterates over the points and appends the position of the point to self.shape
        for i in range(self.points):
            i += 1

            # Calculates the position of the point
            x = self.size * math.sin(math.radians(i * (360 / self.points) - self.direction))
            y = self.size * math.cos(math.radians(i * (360 / self.points) - self.direction))

            # Rounds the postition of the point
            x = round(x + self.xVel)
            y = round(y + self.yVel)

            self.shape.append([x, y])

        self.rect = pygame.Rect((self.x, self.y), self.image.get_size())

    def draw(self, surface: pygame.Surface) -> pygame.Surface:
        self.update()
        tempSurface = pygame.Surface((screenWidth, screenHeight)).convert()

        # Draws each point to the screen
        for i, pos in enumerate(self.shape):
            x, y = pos

            x += self.x
            y += self.y
            tempSurface.blit(self.surface, (x - (self.pointSize / 2), y - (self.pointSize / 2)))

            if not i == 0:
                pygame.draw.line(tempSurface, self.colour, (x, y), lastPos, self.lineSize)
            lastPos = (x, y)
        
        x, y = self.shape[-1]
        lastX, lastY = self.shape[0]
        
        x += self.x
        y += self.y

        lastX += self.x
        lastY += self.y

        # Draws the final line
        pygame.draw.line(tempSurface, self.colour, (x, y), (lastX, lastY), self.lineSize)

        tempSurface.set_colorkey((0, 0, 0))
        surface.blit(tempSurface, (0, 0))

        return tempSurface


shape0 = Shape(6, (screenWidth / 2, screenHeight / 2), 100, (255, 255, 255), 0)
shape0Sprite = pygame.sprite.GroupSingle(shape0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    shape0.x, shape0.y = pygame.mouse.get_pos()
    shape0.direction += 3
    shape0.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
