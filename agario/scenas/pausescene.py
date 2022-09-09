import pygame as pg

from agario.config import settings
from agario.schemas import SCENES

pg.font.init()


class Pause:
    def __init__(self):
        self

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return SCENES.GAME
        return SCENES.PAUSE

    def draw(self, screen):
        font = pg.font.SysFont('chalkduster.ttf',
                               72, bold=True, italic=True)
        text = font.render('Pause', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (settings.screen_width / 2,
                           settings.screen_height / 2)
        screen.blit(text, textRect)
