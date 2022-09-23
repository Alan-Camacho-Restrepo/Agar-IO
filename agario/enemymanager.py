import random

import pygame as pg

from agario.config import settings
from agario.enemy import Enemy


class EnemyManager(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.generate_enemies()

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

                # for enemy in enemies:
                #     actual_center = player.rect.center
                #     player.width = 0.96 *\
                #         math.sqrt(player.width ** 2 + food.width ** 2)
                #     player.image = player.get_image(player.width)
                #     # points = int(player.width) -
                #     # settings.player_initial_width
                #     # print('Puntaje: ', points)
                #     player.rect = player.image.get_rect()
                #     player.rect.center = actual_center
                #     player.mask = pg.mask.from_surface(player.image)

            else:
                enemy.rect.x = -100
                enemy.rect.y = -100

        # for enemy in self:
            # enemy.move()
