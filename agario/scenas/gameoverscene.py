import pygame as pg

from agario.config import settings
from agario.schemas import SCENES

pg.font.init()


class GameOver:
    def __init__(self):
        font = pg.font.Font(settings.font_title, 72)
        self.text = font.render('Game Over', True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (settings.screen_width / 2,
                                settings.screen_height / 2)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_e:
                pg.quit()
        return SCENES.GAMEOVER

    def draw(self, screen):
        screen.blit(self.text, self.textRect)
