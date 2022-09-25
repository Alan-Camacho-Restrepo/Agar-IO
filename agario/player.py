import pygame as pg

from agario.config import settings


class Player(pg.sprite.Sprite):
    def __init__(self, width):
        super().__init__()
        self.width = width
        # Surface to draw player's object
        self.image = self.get_image(width)
        self.rect = self.image.get_rect()
        x_ps = settings.screen_width / 2
        y_ps = settings.screen_height / 2
        self.rect.center = (x_ps, y_ps)
        # self.points = 0
        # mask of the image/surface
        self.mask = pg.mask.from_surface(self.image)

        x_camera = settings.map_width / 2 - settings.screen_width / 2
        y_camera = settings.map_height / 2 - settings.screen_height / 2
        self.camera = pg.Rect(x_camera, y_camera,
                              settings.screen_width, settings.screen_height)

    def get_image(self, width):
        image = pg.Surface((width, width))
        image.fill((0, 0, 0))
        image.set_colorkey((0, 0, 0))
        pg.draw.circle(image, (7, 255, 211),
                       (width / 2, width / 2), width / 2)
        pg.draw.circle(image, (255, 255, 255),
                       (width / 2, width / 2), 1)

        return image

    def update(self, mouse_x, mouse_y):
        x0, y0 = self.rect.center
        Dx = mouse_x - x0
        Dy = mouse_y - y0
        # smoothness of the movement
        p = 0.05
        # TODO: arreglar el smoothness para que siempre
        # quede centrado el jugador respecto al mouse
        x_new_cam = self.camera.x + p * Dx
        y_new_cam = self.camera.y + p * Dy

        if -settings.screen_width / 2 < x_new_cam < \
           settings.map_width - settings.screen_width / 2:
            self.camera.x = x_new_cam

        if -settings.screen_height / 2 < y_new_cam < \
           settings.map_height - settings.screen_height / 2:
            self.camera.y = y_new_cam

    def draw(self, screen):
        x_dinamic = settings.dx - self.camera.x % settings.dx
        y_dinamic = settings.dx - self.camera.y % settings.dx

        for x in range(0, settings.screen_width, settings.dx):
            up_point = (x + x_dinamic, 0)
            down_point = (x + x_dinamic, settings.screen_height)
            pg.draw.line(
                screen,
                (0, 0, 0),
                up_point,
                down_point
            )

        for y in range(0, settings.screen_height, settings.dx):
            left_point = (0, y + y_dinamic)
            rigth_point = (settings.screen_width, y + y_dinamic)
            pg.draw.line(
                screen,
                (0, 0, 0),
                left_point,
                rigth_point
            )

        screen.blit(self.image, self.rect)
