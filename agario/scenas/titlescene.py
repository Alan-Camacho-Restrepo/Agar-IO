from agario.scenas.scene import Scene
from agario.schemas import SCENES
from agario.config import settings

import pygame as pg

pg.font.init()
class TitleScene(Scene):
    
    def update(self, events):
    
        if len(events) != 0:
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    return SCENES.GAME
                else:
                    return SCENES.TITLE
        else:
            return SCENES.TITLE
                        
    
    def draw(self, screen):
        
        font = pg.font.SysFont('chalkduster.ttf', 72)
        text = font.render('Press SPACE to play', True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (settings.screen_width / 2, settings.screen_height / 2)
        screen.fill((100, 140, 145))
        screen.blit(text, textRect)

