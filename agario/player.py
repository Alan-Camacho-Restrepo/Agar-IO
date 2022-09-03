import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, width):
        super().__init__()

        self.width = width
        # Surface to draw player's object
        self.image = self.get_image(width)
        self.rect = self.image.get_rect()
        self.points = 0
        # mask of the image/surface
        self.mask = pg.mask.from_surface(self.image)

    def get_image(self, width):

        image = pg.Surface((width, width))
        image.fill((0, 0, 0))
        image.set_colorkey((0, 0, 0))
        pg.draw.circle(image, (0, 255, 100), (width / 2, width / 2), width / 2)
        pg.draw.circle(image, (255, 255, 255), (width / 2, width / 2), 1)

        return image

    def update(self, mouse_x, mouse_y):
        x0, y0 = self.rect.center  # Position of center of the rect object player
        # Difference or distance between the two positions (object and mouse)
        Dx = mouse_x - x0
        Dy = mouse_y - y0
        # smoothness of the movement
        p = 0.1
        # TODO: arreglar el smoothness para que siempre quede centrado el jugador respecto al mouse
        x0 += p * Dx
        y0 += p * Dy

        self.rect.center = (x0, y0)
