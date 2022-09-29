import math
import random

import pygame as pg

from agario.config import settings
from agario.colors import COLORS

food_colors = list(COLORS.values())


class Food(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = settings.food_initial_width
        self.image = self.get_image()
        # TODO: Modificar el tamaño del rectangulo
        # usando https://www.pygame.org/docs/ref/rect.html
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.mask = pg.mask.from_surface(self.image)

    def get_image(self):
        surface = pg.Surface((self.width, self.width))
        to_draw = ['Pentagon', 'Hexagon']
        draw = random.choice(to_draw)

        if draw == 'Pentagon':
            lado = self.width * math.sin(36 * (math.pi / 180))\
                   / math.sin(108 * (math.pi / 180))
            point1 = (int(self.width / 2), 0)
            point2 = (0, lado * math.sin(36 * (math.pi / 180)))
            point5 = (self.width, lado * math.sin(36 * (math.pi / 180)))
            point3 = (
                      lado * math.cos(72 * (math.pi / 180)), self.width
                     )
            point4 = (self.width - lado *
                      math.cos(72 * (math.pi / 180)), self.width)

            # Color aleatorio
            color = random.choice(food_colors)

            # Dibujando el pentagono
            pg.draw.polygon(surface, color,
                            (point1, point2, point3, point4, point5)
                            )

            return surface

        else:
            l = self.width / (2 * math.cos(60 * (math.pi / 180)) + 1)
            p1 = (l * math.cos(60 * (math.pi / 180)), 0)
            p2 = (self.width - l * math.cos(60 * (math.pi / 180)), 0)
            p3 = (self.width, l * math.sin(60 * (math.pi / 180)))
            p4 = (self.width - l * math.cos(60 * (math.pi / 180)), self.width)
            p5 = (l * math.cos(60 * (math.pi / 180)), self.width)
            p6 = (0, l*math.sin(60 * (math.pi / 180)))

            # Color aleaotrio
            color = random.choice(food_colors)

            # Dibujando el hexagono
            pg.draw.polygon(surface, color, (p1, p2, p3, p4, p5, p6))

            return surface

    def set_position(self, x, y):
        self.rect.center = (x, y)
        self.rect_real = pg.Rect(x, y, self.width, self.width)
