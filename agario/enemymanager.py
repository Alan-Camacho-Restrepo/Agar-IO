import random

import pygame as pg
from agario.foodmanager import FoodManager
from agario.config import settings
from agario.enemy import Enemy


class EnemyManager(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.generate_enemies()
        self.food_manager = FoodManager()

    def generate_enemies(self):
        for _ in range(settings.enemy_initial_number):
            enemy = Enemy()
            x = random.randint(0, settings.map_width)
            y = random.randint(0, settings.map_height)
            enemy.set_position(x, y)
            self.add(enemy)

    def update(self, player):
        for enemy in self:
            enemy.move(player)
            if player.camera.colliderect(enemy.rect_real):
                enemy.rect.x = enemy.rect_real.x - player.camera.x
                enemy.rect.y = enemy.rect_real.y - player.camera.y
                enemies = pg.sprite.spritecollide(player, self,
                                                  False, 
                                                  pg.sprite.collide_mask)

            else:
                enemy.rect.x = -200
                enemy.rect.y = -200
