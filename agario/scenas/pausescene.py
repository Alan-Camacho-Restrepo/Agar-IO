import pygame as pg

from agario.config import settings
from agario.schemas import SCENES

pg.font.init()


class Pause:
    def __init__(self):
        font = pg.font.Font(settings.font_title,
                               72)
        self.text = font.render('Paused', True, (30, 30, 30))
        self.text.set_alpha(15)
        self.textRect = self.text.get_rect()
        self.textRect.center = (settings.screen_width / 2,
                                settings.screen_height / 2)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return SCENES.GAME
        return SCENES.PAUSE

    def draw(self, screen):    
        screen.blit(self.text, self.textRect)
