import math
import random

import pygame as pg

from agario.config import settings
from agario.food import Food


class FoodManager(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.generate_food()

    def generate_food(self):
        for _ in range(settings.food_initial_number):
            food = Food(settings.food_initial_width)
            x = random.randint(0, settings.map_width)
            y = random.randint(0, settings.map_height)
            food.set_position(x, y)
            self.add(food)

    def update(self, player):
        for food in self:
            if player.camera.colliderect(food.rect_real):
                food.rect.x = food.rect_real.x - player.camera.x
                food.rect.y = food.rect_real.y - player.camera.y
                foods = pg.sprite.spritecollide(player, self,
                                                True, pg.sprite.collide_mask)

                for food in foods:
                    actual_center = player.rect.center
                    player.width = 0.96 *\
                        math.sqrt(player.width ** 2 + food.width ** 2)
                    player.image = player.get_image(player.width)
                    # points = int(player.width) -
                    # settings.player_initial_width
                    # print('Puntaje: ', points)
                    player.rect = player.image.get_rect()
                    player.rect.center = actual_center
                    player.mask = pg.mask.from_surface(player.image)

            else:
                food.rect.x = -10
                food.rect.y = -10
