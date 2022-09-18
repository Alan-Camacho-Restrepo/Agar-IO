import pygame as pg

from agario.config import settings
from agario.scenas.scene import Scene
from agario.schemas import SCENES


class SettingScene(Scene):
    def __init__(self):
        width = 600
        height = 600
        self.surface = pg.Surface((width, height))
        self.surf_rect = self.surface.get_rect()
        self.surf_rect.center = (settings.screen_width / 2,
                                 settings.screen_height / 2)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                return SCENES.GAME
        return SCENES.SETTINGS

    def draw(self, screen):
        self.surface.fill((0, 155, 0))
        screen.blit(self.surface, self.surf_rect)
        # return screen.get_rect()
