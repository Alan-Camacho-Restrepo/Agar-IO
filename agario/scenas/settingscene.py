import pygame as pg

from agario.config import settings
from agario.scenas.scene import Scene
from agario.schemas import SCENES


class SettingScene(Scene):
    def __init__(self):
        self

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                return SCENES.GAME
        return SCENES.SETTINGS

    def draw(self, screen):
        # set_w = settings.screen_width - 400
        # set_h = settings.screen_height - 300
        set_w = 600
        set_h = 600
        surface = pg.Surface((set_w, set_h))
        surf_rect = surface.get_rect()
        surf_rect.center = (settings.screen_width / 2,
                            settings.screen_height / 2)
        surface.fill((0, 155, 0))
        screen.blit(surface, surf_rect)
