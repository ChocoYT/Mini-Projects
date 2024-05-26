import keyboard
import math
import pygame

pygame.init()

screenWidth = 1000
screenHeight = 800
FPS = 60

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

class Cell():
    def __init__(self):
        # Initialises the 'Cell' class
        self.mouseX, self.mouseY = 0, 0

        self.oldMousePos = (0, 0)
        self.oldDraw = False

        self.tiles = []

        self.size = 40
        self.colour = (170, 170, 170)
        
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill(self.colour)

    def calculateGridMouse(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()

        self.gridMouseX = math.floor((self.mouseX - grid.xOffset) / self.size)
        self.gridMouseY = math.ceil((grid.yOffset - self.mouseY) / self.size)

        return self.gridMouseX, self.gridMouseY
    
    def drawCells(self):
        self.draw = pygame.mouse.get_pressed()[0]
        self.mousePos = self.calculateGridMouse()

        if self.draw and (self.draw == self.oldDraw) == (not self.mousePos == self.oldMousePos):
                # Adds the tile coordinate to 'self.tiles' list
                self.add = True
                for _i, pos in enumerate(self.tiles):
                    if pos == self.mousePos:
                        self.add = False

                if self.add:
                    self.tiles.append(self.mousePos)
                else:
                    self.tiles.remove(self.mousePos)

                self.oldMousePos = self.mousePos

        self.rows = []
        self.columns = []

        # Draws the tiles
        for _i, pos in enumerate(self.tiles):
            self.posX = pos[0]
            self.posY = -pos[1]

            # Blits the cell(s) to the screen
            if keyboard.is_pressed("R"):
                self.tiles.clear()
                break
            else:
                screen.blit(self.surface, ((self.posX * self.size) + grid.xOffset, (self.posY * self.size) + grid.yOffset)) 
        
        self.oldDraw = self.draw

    def simulate(self):
        self.step = keyboard.is_pressed("SPACE")

        if self.step:

            if len(self.tiles) > 0:
                # Calculates the range of simulation
                for i, num in enumerate(self.tiles):

                    if i == 0:
                        self.xRange = [num[0], num[0]]
                        self.yRange = [num[1], num[1]]
                        
                    # Calculates the range of horizontal simulation
                    if num[0] < self.xRange[0]:
                        self.xRange.pop(0)
                        self.xRange.insert(0, num[0])
                    if num[0] > self.xRange[1]:
                        self.xRange.pop(1)
                        self.xRange.insert(1, num[0])
                        
                    # Calculates the range of vertical simulation
                    if num[1] < self.yRange[0]:
                        self.yRange.pop(0)
                        self.yRange.insert(0, num[1])
                    if num[1] > self.yRange[1]:
                        self.yRange.pop(1)
                        self.yRange.insert(1, num[1])

                self.xRange = [self.xRange[0] - 1, self.xRange[1] + 1]
                self.yRange = [self.yRange[0] - 1, self.yRange[1] + 1]

                self.add = []
                self.remove = []

                # Calculates the state changes in the range
                for x in range((self.xRange[1] - self.xRange[0]) + 1):
                    for y in range((self.yRange[1] - self.yRange[0]) + 1):

                        self.xOffset = x + self.xRange[0]
                        self.yOffset = y + self.yRange[0]

                        self.pos = (self.xOffset, self.yOffset)

                        # Calulates if the cell should change state
                        if self.pos in self.tiles:
                            neighbours = self.calculateNeighbours(self.tiles.index(self.pos))

                            if not (neighbours == 2 or neighbours == 3):
                                self.remove.append(self.pos)
                        else:
                            self.tiles.insert(0, self.pos)
                            neighbours = self.calculateNeighbours(0)

                            if neighbours == 3:
                                self.add.append(self.pos)
                            self.tiles.pop(0)
                
                # Changes the state of the tiles
                for _i, data in enumerate(self.add):
                    self.tiles.append(data)

                for _i, data in enumerate(self.remove):
                    self.tiles.remove(data)

    def calculateNeighbours(self, index):
        self.tileX = self.tiles[index][0]
        self.tileY = self.tiles[index][1]

        self.neighbours = 0

        for i, pos in enumerate(self.tiles):
            if not i == index:
                if self.inRange(pos[0], self.tileX, 1) and self.inRange(pos[1], self.tileY, 1):
                    self.neighbours += 1
        
        return self.neighbours

    def inRange(self, num1, num2, range):
        if abs(num1 - num2) > range:
            return False
        else:
            return True


class Grid():
    def __init__(self):
        # Initialises the 'Grid' class
        self.xOffset = 0
        self.yOffset = 0

        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.mouseZoom = 0
        self.zoomSize = 6

        self.width = 1
        self.surface = pygame.Surface((screenWidth, screenHeight))

    def draw(self):
        self.surface.fill((0, 0, 0))
        self.calculateOffsets()

        # Draws vertical lines
        for i in range(math.ceil(screenWidth / cell.size)):

            # Calculates vertical X line positions and draws
            self.posX = (i * cell.size) + (self.xOffset % cell.size)
            pygame.draw.line(self.surface, cell.colour, (self.posX, 0), (self.posX, screenHeight), self.width)

        # Draws horizontal lines
        for i in range(math.ceil(screenHeight / cell.size)):

            # Calculates horizontal Y line positions and draws
            self.posY = (i * cell.size) + (self.yOffset % cell.size)
            pygame.draw.line(self.surface, cell.colour, (0, self.posY), (screenWidth, self.posY), self.width)

        self.surface.set_colorkey((0, 0, 0))
        screen.blit(self.surface, (0, 0))

    def calculateOffsets(self):
        # Scrolls the grid
        self.move = pygame.mouse.get_pressed()[2]

        if self.move:
            self.xOffset += pygame.mouse.get_pos()[0] - self.mouseX
            self.yOffset += pygame.mouse.get_pos()[1] - self.mouseY

        self.mouseX, self.mouseY = pygame.mouse.get_pos()

        return self.xOffset, self.yOffset


cell = Cell()
grid = Grid()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEWHEEL:
            grid.mouseZoom += event.x
            grid.mouseZoom -= event.y


    screen.fill((30, 30, 30))

    grid.draw()
    cell.drawCells()
    cell.simulate()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()