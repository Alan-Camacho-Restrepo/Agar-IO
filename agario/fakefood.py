import pygame as pg


class FakeFood(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 5
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

    def get_image(self):
        # Tamaño del surface, en este caso un cuadrado
        surface = pg.Surface((self.width, self.width))
        pg.draw.rect(surface, (255, 0, 0), (0, 0, self.width, self.width))
        return surface

    def set_position(self, x, y):
        # Cambiando las coordenadas del centro del rect de la imagen o comida
        self.rect.center = (x, y)

    def draw(self, screen):
        # Insertando en el screen la comida en el Rect con posicion aleaotria de su centro
        screen.blit(self.image, self.rect)
