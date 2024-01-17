import random
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text
from scripts.player import Player
from scripts.camera import Camera
from scripts.fade import Fade

class Game(Scene):

    def __init__(self):
        super().__init__()
        self.collision_sprites = pygame.sprite.Group()
        self.stage = 0
        self.maps = [MAP0, MAP1, MAP2]
        self.current_level = Level(self.maps[self.stage])

    def events(self, event):
        pass

    def draw(self):
        self.current_level.draw()

    def update(self):
        self.current_level.update()

class Ui:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.ui_group = pygame.sprite.Group()

        self.hud1 = Obj("assets/player/idle_0.png", [0, 10], [self.ui_group])
        self.hud2 = Obj("assets/player/idle_0.png", [74, 10], [self.ui_group])
        self.hud3 = Obj("assets/player/idle_0.png", [144, 10], [self.ui_group])

    def draw(self):
        self.ui_group.draw(self.display)

class Level:
    def __init__(self, worldmap):
        self.display = pygame.display.get_surface()
        self.all_sprites = Camera()
        self.collision_sprites = pygame.sprite.Group()

        self.active = True
        self.gameover = False
        self.fade = Fade(5)
        self.finish = Obj("assets/title/finish.png", [0, 0], [self.all_sprites])
        self.player = Player([100, 128],[self.all_sprites], self.collision_sprites)
        self.worldmap = worldmap
        self.generate_map()
        self.hud_ui = Ui()

    def events(self, event):
        pass

    def next_stage(self):
        if self.player.rect.colliderect(self.finish):
            self.active = False


    def draw(self):
        self.all_sprites.costum_draw(self.player)
        self.hud_ui.draw()
        self.fade.draw()
        # self.current_level.draw()

    def generate_map(self):
        for row_index, row in enumerate(self.worldmap):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if col == "X":
                    Obj("assets/title/tile.png", [x, y], [self.all_sprites, self.collision_sprites])

                elif col == "C":
                    self.finish.rect.x = x
                    self.finish.rect.y = y
                elif col == "P":
                    self.player.rect.x = x
                    self.player.rect.y = y

    def collision(self):
        pass

    def gameover(self):
        pass

    def update(self):
        self.all_sprites.update()
        self.next_stage()
        #self.reset_position()
        #self.hud_ui.update()





