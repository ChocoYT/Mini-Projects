import keyboard
import pygame
import sys

pygame.init()

screenWidth = 1000
screenHeight = 800
FPS = 60

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Top Down Test")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int | float], speed: int | float, size: int) -> None:
        super().__init__()

        # Position
        self.x, self.y = pos
        self.xVel, self.yVel = 0, 0

        self.speed = speed
        self.friction = 0.8

        # Surface
        self.size = size
        self.colour = (255, 255, 255)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.colour)

        # Rect
        self.rect = self.image.get_rect()

    def move(self):
        # Calculates the movement
        moveX = int(keyboard.is_pressed("D") or keyboard.is_pressed("RIGHT")) - int(keyboard.is_pressed("A") or keyboard.is_pressed("LEFT"))
        moveY = int(keyboard.is_pressed("W") or keyboard.is_pressed("UP")) - int(keyboard.is_pressed("S") or keyboard.is_pressed("DOWN"))

        moveDist = ((moveX ** 2) + (moveY ** 2)) ** 0.5

        # Normalises movement
        if moveDist > 1:
            moveX /= moveDist
            moveY /= moveDist
        
        # Increases velocity
        self.xVel += moveX * self.speed
        self.yVel += moveY * self.speed

        # Changes the position
        if pygame.sprite.spritecollide(playerGroup.sprite, tileGroup, False):
            self.xVel, self.yVel = 0, 0
        else:
            self.x += self.xVel
            self.y -= self.yVel

        # Adds friction
        self.xVel *= self.friction
        self.yVel *= self.friction

    def update(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.x, self.y))


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int | float]) -> None:
        super().__init__()

        # Position
        self.x, self.y = pos
        self.x *= grid.cellSize
        self.y *= grid.cellSize

        # Surface
        self.size = grid.cellSize
        self.colour = (255, 0, 0)
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.colour)

        # Rect
        self.rect = self.image.get_rect()

    def update(self) -> None:
        self.rect.x = self.x + (grid.lineSize / 2)
        self.rect.y = self.y + (grid.lineSize / 2)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, (self.x, self.y))


class Mouse():
    def __init__(self) -> None:
        self.x, self.y = pygame.mouse.get_pos()
        self.xVel, self.yVel = 0, 0

    def calculatePos(self) -> tuple[int | float]:
        self.x, self.y = pygame.mouse.get_pos()

        return self.x, self.y
        
    def calculateVelocity(self) -> tuple[int | float]:
        newX, newY = pygame.mouse.get_pos()
        self.xVel = newX - self.x
        self.yVel = newY - self.y

        self.x, self.y = newX, newY

        return self.xVel, self.yVel


class Grid():
    def __init__(self, cellSize: int | float, thickness: int) -> None:
        self.cellSize = cellSize
        self.lineSize = thickness

        self.colour = (70, 70, 70)

        self.scrollX, self.scrollY = 0, 0

    def getMouseCell(self) -> tuple[int | float]:
        x, y = mouse.calculatePos()

        x //= grid.cellSize
        y //= grid.cellSize

        return x, y

    def draw(self, surface: pygame.Surface) -> None:
        surfaceWidth, surfaceHeight = surface.get_size()

        columns = surfaceWidth // self.cellSize
        rows = surfaceHeight // self.cellSize

        scroll = pygame.mouse.get_pressed()[2]

        mouseXVel, mouseYVel = mouse.calculateVelocity()
        if scroll:
            self.scrollX += mouseXVel
            self.scrollY += mouseYVel

        for i in range(columns):
            x = self.cellSize * i
            x += self.scrollX % self.cellSize

            pygame.draw.line(surface, self.colour, (x, 0), (x, surfaceHeight), self.lineSize)

        for i in range(rows):
            y = self.cellSize * i
            y += self.scrollY % self.cellSize

            pygame.draw.line(surface, self.colour, (0, y), (surfaceWidth, y), self.lineSize)


tiles = set()

player = Player((0, 0), 2, 50)
mouse = Mouse()
grid = Grid(50, 2)

playerGroup = pygame.sprite.GroupSingle(player)
tileGroup = pygame.sprite.Group()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((20, 20, 20))
    grid.draw(screen)

    # Updates the player
    player.move()
    player.update()
    player.draw(screen)

    # Attempts to add a tile to the set
    tileGroup = pygame.sprite.Group()

    place = pygame.mouse.get_pressed()[0]
    if place:
        tiles.add(grid.getMouseCell())
    for pos in tiles:
        tileGroup.add(Tile(pos))

    tileGroup.update()
    tileGroup.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()