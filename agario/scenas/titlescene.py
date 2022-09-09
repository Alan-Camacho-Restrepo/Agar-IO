from agario.scenas.scene import Scene
from agario.schemas import SCENES
from agario.config import settings

import pygame as pg

pg.font.init()
class TitleScene(Scene):
    def __init__(self):
        font = pg.font.SysFont('chalkduster.ttf', 72)    
        self.text = font.render('Press SPACE to play', True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (settings.screen_width / 2, 
                           settings.screen_height / 2)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                return SCENES.GAME
        return SCENES.TITLE

    def draw(self, screen):
        screen.fill((100, 140, 145))
        screen.blit(self.text, self.textRect)
