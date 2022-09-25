import random
import pygame as pg
from agario.config import settings

def add(x, y):
    return x + y

def substract(x, y):
    return x - y


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
        # TODO: color choice in enemies
        pg.draw.circle(image, (255, 0, 0),
                       (self.width / 2, self.width / 2),
                       self.width / 2)

        return image

    def random_direction(self):
        self.func1 = random.choice([add, substract])
        self.func2 = random.choice([add, substract])

    def move(self, player):
        xd, yd = self.rect_real.center
        if player.camera.x + player.camera.width / 8 < xd\
            < player.camera.x + 7 * player.camera.width / 8\
            and player.camera.y + player.camera.height / 8 < yd\
                < player.camera.y + 7 * player.camera.height / 8:
            xc, yc = player.camera.center
            Dx = xc - xd
            Dy = yc - yd
            p = 0.03
            xd += p * Dx
            yd += p * Dy
            self.rect_real.center = (xd, yd)

        else:
            self.rect_real.x = self.func1(self.rect_real.x, self.speed_x)
            self.rect_real.y = self.func2(self.rect_real.y, self.speed_y)

            if self.rect_real.x >= settings.map_width - self.width\
                    and self.rect_real.y <= settings.map_height - self.width:
                self.speed_x = -self.speed_x

            if self.rect_real.y >= settings.map_height - self.width\
                    and self.rect_real.x <= settings.map_width - self.width:
                self.speed_y = -self.speed_y

            if self.rect_real.x <= 0 and self.rect_real.y >= 0:
                self.speed_x = -self.speed_x

            if self.rect_real.y <= 0 and self.rect_real.x >= 0:
                self.speed_y = -self.speed_y

            # if self.rect_real.x == 0 and self.rect_real.y == 0:
            #     self.speed_x = -self.speed_x
            #     self.speed_y = -self.speed_y

            # if self.rect_real.x == settings.map_width - self.width\
            #         and self.rect_real.y == settings.map_height - self.width:
            #     self.speed_x = -self.speed_x
            #     self.speed_y = -self.speed_y

            # if self.rect_real.x == settings.map_width - self.width\
            #         and self.rect_real.y == 0:
            #     self.speed_x = -self.speed_x
            #     self.speed_y = -self.speed_y

            # if self.rect_real.x == 0\
            #         and self.rect_real.y == settings.map_height - self.width:
            #     self.speed_x = -self.speed_x
            #     self.speed_y = -self.speed_y

    def set_position(self, x, y):
        self.rect.center = (x, y)
        self.rect_real = pg.Rect(x, y, self.width, self.width)
