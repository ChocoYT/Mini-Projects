import pygame
import math
import keyboard
import time

pygame.init()

FPS = 60

screen_width = 1000
screen_height = 800
mouse_x, mouse_y = pygame.mouse.get_pos()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer Test")

class Player:
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 2

    def move_player(self, speed):
        if keyboard.is_pressed("D"):
            self.x -= speed
        elif keyboard.is_pressed("A"):
            self.x += speed
        elif keyboard.is_pressed("W"):
            self.y += speed
        elif keyboard.is_pressed("S"):
            self.y -= speed
        

class Tiles:
    def __init__(self):
        self.grid_x = 0
        self.grid_y = 0
        self.tile_size = 40
        self.map = []
        self.editor = 0

    def toggle_editor(self):
        if keyboard.is_pressed("0"):
            self.editor = 1 - self.editor

    def place_tiles(self):
        self.toggle_editor()
        grid_mouse_x = (player.x % self.tile_size) - (self.tile_size / 2)
        grid_mouse_y = (player.y % self.tile_size)
        grid_mouse_x += (math.floor(mouse_x / self.tile_size)) * self.tile_size
        grid_mouse_y += (math.floor(mouse_y / self.tile_size)) * self.tile_size

        self.tile = pygame.Surface((self.tile_size, self.tile_size)).convert_alpha()
        self.tile.fill((255, 255, 255, 50))

        if self.editor == 1:
            screen.blit(self.tile, (grid_mouse_x, grid_mouse_y))

            grid_mouse_x -= player.x
            grid_mouse_y -= player.y

            if left_click == 1 and (grid_mouse_x, grid_mouse_y) not in self.map:
                self.map.append((grid_mouse_x, grid_mouse_y))

        self.tile.fill((255, 255, 255))
        self.item = 0
        for self.item in range(len(self.map)):
            tilemap_x, tilemap_y, = self.map[self.item]
            tilemap_x += player.x
            tilemap_y += player.y
            screen.blit(self.tile, (tilemap_x, tilemap_y))
            self.item += 1


player = Player()
tiles = Tiles()

run = True
while run:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()

        left_click, middle_click, right_click = pygame.mouse.get_pressed()

    screen.fill((0, 0, 0))
    player.move_player(10)
    tiles.place_tiles()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()