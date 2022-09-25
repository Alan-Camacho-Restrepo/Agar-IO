import pygame as pg

from agario.config import settings
from agario.enemymanager import EnemyManager
from agario.foodmanager import FoodManager
from agario.player import Player
from agario.scenas.scene import Scene
from agario.schemas import SCENES


class GameScene(Scene):
    def __init__(self):
        self.initialized_objects()

    def initialized_objects(self):
        self.food_manager = FoodManager()
        self.enemy_manager = EnemyManager()
        self.player = Player(settings.player_initial_width)

    def collide_group(self):
        pg.sprite.groupcollide(self.enemy_manager, self.food_manager,
                               False, True, pg.sprite.collide_mask)

    def update(self, events):
        mouse_x, mouse_y = pg.mouse.get_pos()
        self.player.update(mouse_x, mouse_y)
        self.food_manager.update(self.player)
        self.enemy_manager.update(self.player)
        # self.collide_group()
        # if pg.sprite.spritecollide(self.player, self.enemy_manager,
        #                            False, pg.sprite.collide_mask):
        #     return SCENES.GAMEOVER
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return SCENES.PAUSE
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                return SCENES.SETTINGS
        return SCENES.GAME

    def draw(self, screen):
        screen.fill(pg.Color("white"))
        self.player.draw(screen)
        self.enemy_manager.draw(screen)
        self.food_manager.draw(screen)
