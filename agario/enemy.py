import random

import pygame as pg

from agario.config import settings


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = settings.enemy_initial_width
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.mask = pg.mask.from_surface(self.image)
        self.speed_x = settings.enemy_speed
        self.speed_y = settings.enemy_speed
        self.random_direction()

    def get_image(self):
        image = pg.Surface((self.width, self.width))
        pg.draw.circle(image, (255, 0, 0),
                       (self.width / 2, self.width / 2),
                       self.width / 2)

        return image

    def random_direction(self):
        def add(x, y):
            return x + y

        def substract(x, y):
            return x - y
        self.func1 = random.choice([add, substract])
        self.func2 = random.choice([add, substract])

    def move(self):
        self.rect_real.x = self.func1(self.rect_real.x, self.speed_x)
        self.rect_real.y = self.func2(self.rect_real.y, self.speed_y)

        if self.rect_real.x > settings.map_width - self.width\
                and self.rect_real.y < settings.map_height - self.width:
            self.speed_x = -self.speed_x
        if self.rect_real.y > settings.map_height - self.width\
                and self.rect_real.x < settings.map_width - self.width:
            self.speed_y = -self.speed_y
        if self.rect_real.x < abs(settings.enemy_speed) \
                and self.rect_real.y > abs(settings.enemy_speed):
            self.speed_x = -self.speed_x
        if self.rect_real.y < abs(settings.enemy_speed) \
                and self.rect_real.x > abs(settings.enemy_speed):
            self.speed_y = -self.speed_y

    def set_position(self, x, y):
        self.rect.center = (x, y)
        self.rect_real = pg.Rect(x, y, self.width, self.width)
