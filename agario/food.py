import math
import random

import pygame as pg

from agario.config import settings


class Food(pg.sprite.Sprite):
    def __init__(self, width):
        super().__init__()

        self.width = width
        self.image = self.get_image()
        # TODO: Modificar el tamaño del rectangulo usando https://www.pygame.org/docs/ref/rect.html
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.mask = pg.mask.from_surface(self.image)


        # TODO: Definir nuevos atributos para la comida (algo masa o energia, ....)

    def get_image(self):
        # Tamaño del surface, en este caso un cuadrado
        surface = pg.Surface((self.width, self.width))
        # surface.fill((0, 255, 0))
        # Escoger aletoriamente si dibujar un pentagono o un hexagono
        to_draw = ['Pentagon', 'Hexagon']
        draw = random.choice(to_draw)

        if draw == 'Pentagon':
            '''
            Dibujando un pentagono regular, donde el angulo interior es de 108 grados
            y la longitu de sus lados es el mismo
            '''
            lado = self.width * math.sin(36 * (math.pi / 180)) / math.sin(108 * (math.pi / 180))
            point1 = (int(self.width / 2), 0)
            point2 = (0, lado * math.sin(36 * (math.pi / 180)))
            point5 = (self.width, lado * math.sin(36 * (math.pi / 180)))
            point3 = (lado * math.cos(72 * (math.pi / 180)), self.width)
            point4 =  (self.width - lado * math.cos(72 * (math.pi / 180)), self.width)

            # Color aleatorio
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

            # Dibujando el pentagono
            pg.draw.polygon(surface, color, (point1, point2, point3, point4, point5))

            return surface

        else:
            '''
            Definiendo los puntos de los vertices del hexagono, HEXAGONO REGULAR
            donde el angulo interior es de 120 grados para todos los angulos interiores
            y los lados tienes la misma longitud
            '''
            l = self.width / (2 * math.cos(60 * (math.pi / 180)) + 1)  # longitud de los lados del hexagono
            p1 = (l * math.cos(60 * (math.pi / 180)), 0)
            p2 = (self.width - l * math.cos(60 * (math.pi / 180)), 0)
            p3 = (self.width, l * math.sin(60 * (math.pi / 180)))
            p4 = (self.width - l * math.cos(60 * (math.pi / 180)), self.width)
            p5 = (l * math.cos(60 * (math.pi / 180)), self.width)
            p6 = (0, l*math.sin(60 * (math.pi / 180)))

            # Color aleaotrio
            color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

            # Dibujando el hexagono
            pg.draw.polygon(surface, color, (p1, p2, p3, p4, p5, p6))

            return surface

    def set_position(self, x, y):
        """
        Esta funcion modifica el atributo rect de la clase
        """
        # Cambiando las coordenadas del centro del rect de la imagen o comida
        self.rect.center = (x, y)

    # def draw(self, screen):
    #     # Insertando en el screen la comida en el Rect con posicion aleaotria de su centro
    #     screen.blit(self.image, self.rect)

