import pygame

pygame.init()

screen_width = 1000
screen_height = 800
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

class Player():
    def __init__(self):
        self.x = 20
        self.y = 20

        self.xvel = 0
        self.yvel = 0
        self.size = 40

    def draw(self):
        self.surface = pygame.Surface((self.size, self.size))
        self.surface.fill((255, 255, 255))

        screen.blit(self.surface, (self.x - (self.size / 2), self.y - (self.size / 2)))

    def move(self):
        pass


class Level():
    def __init__(self):
        self.tile_size = 80

        self.map = [

        "                         ",
        "                         ",
        "                         ",
        "                         ",
        "       P                 ",
        "XX    XXX        XX      ",
        "XXX               X      ",
        "XXXX          X   X      ",
        "XXXXX     XXXXXXXXX      ",
        "XXXXXXX   XXXXXXXXX  XXXX", 
        ]

    def draw_cell(self, x, y, tile):
        if tile == "X":
            self.surface = pygame.Surface((self.tile_size, self.tile_size))
            self.surface.fill((255, 255, 255))

            screen.blit(self.surface, (x * self.tile_size, y * self.tile_size))

    def draw(self):
        for y, _ in enumerate(self.map):
            for x, _ in enumerate(self.map[1]):
                self.tile = (self.map[y])[x]
                if self.tile != " ":
                    self.draw_cell(x, y, self.tile)


player = Player()
level = Level()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    level.draw()
    player.move()
    player.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()