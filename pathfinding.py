import math
import pygame
import sys

pygame.init()

screenWidth = 1000
screenHeight = 800
FPS = 99999

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pathfinding")
clock = pygame.time.Clock()

class Mouse():
    def __init__(self) -> None:
        super().__init__()

        # Initialises the 'Mouse' class
        self.oldMouseX, self.oldMouseY = pygame.mouse.get_pos()

    def calulateMouseMovement(self) -> tuple[float]:
        move = pygame.mouse.get_pressed()[2]

        if move:
            xVel = mouseX - self.oldMouseX
            yVel = mouseY - self.oldMouseY

            self.oldMouseX, self.oldMouseY = mouseX, mouseY

            return xVel, yVel
        else:
            self.oldMouseX, self.oldMouseY = mouseX, mouseY

            return 0, 0

class Grid():
    def __init__(self) -> None:
        super().__init__()

        # Initialises the 'Grid' class
        self.xOffset = 0
        self.yOffset = 0

        self.gridSize = 50
        self.lineSize = 2
        self.colour = (50, 50, 50)

    def drawGrid(self, surface: pygame.Surface) -> pygame.Surface:
        gridSurface = pygame.Surface(surface.get_size())

        # Calculates the x and y offset
        xVel, yVel = mouse.calulateMouseMovement()
        self.xOffset += xVel
        self.yOffset += yVel
        self.xGridOffset = self.xOffset % self.gridSize
        self.yGridOffset = self.yOffset % self.gridSize

        # Calculates the amount of columns and rows
        horizontalCells = math.ceil(screenWidth / self.gridSize)
        verticalCells = math.ceil(screenHeight / self.gridSize)

        # Draws the columns
        for x in range(horizontalCells):
            x *= self.gridSize
            x += self.xGridOffset
            pygame.draw.line(gridSurface, self.colour, (x, 0), (x, screenHeight), self.lineSize)

        # Draws the rows
        for y in range(verticalCells):
            y *= self.gridSize
            y += self.yGridOffset
            pygame.draw.line(gridSurface, self.colour, (0, y), (screenWidth, y), self.lineSize)

        surface.blit(gridSurface, (0, 0))

        return gridSurface
    
    def calculateMouse(self):
        gridMouseX = mouseX + self.xOffset
        gridMouseY = mouseY + self.yOffset

        return gridMouseX, gridMouseY
    
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        
        # Initialises the 'Tile' class
        self.x, self.y = pos

        self.colour = (255, 255, 255)
        self.size = grid.gridSize

        # Creates a Surface and collision Rect
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.colour)
        self.rect = self.surface.get_rect(topleft = (self.x, self.y))

    def update(self, surface):
        self.rect.topleft = (self.x + grid.xOffset, self.y + grid.yOffset)
        surface.blit(self.surface, (self.x + grid.xOffset, self.y + grid.yOffset))


mouseX, mouseY = (0, 0)

grid = Grid()
mouse = Mouse()

tiles = pygame.sprite.Group()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    grid.drawGrid(screen)
    
    if pygame.mouse.get_pressed()[0]:
        tiles.add(Tile(grid.calculateMouse()))
    print(tiles)

    tiles.update(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
