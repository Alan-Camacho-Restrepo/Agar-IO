from agario.scenas.scene import Scene
from agario.schemas import SCENES
from agario.foodmanager import FoodManager
from agario.player import Player
from agario.config import settings
import pygame as pg

class GameScene(Scene):
    def __init__(self):
        self.initialized_objects()

    def initialized_objects(self):
        self.food_manager = FoodManager()
        self.player = Player(settings.player_initial_width)

    def update(self, events):
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.player.update(mouse_x, mouse_y)
        self.food_manager.update(self.player)
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return SCENES.PAUSE
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                return SCENES.SETTINGS
        return SCENES.GAME

    def draw(self, screen):
        screen.fill(pg.Color("black"))
        self.food_manager.draw(screen)
        screen.blit(self.player.image, self.player.rect)
