import pygame as pg

from agario.config import settings
from agario.scenas.scene import Scene
from agario.schemas import SCENES

pg.font.init()


class SettingScene(Scene):
    def __init__(self):
        self.width = 600
        self.height = 600
        self.surface = pg.Surface((self.width, self.height))
        self.surf_rect = self.surface.get_rect()
        self.surf_rect.center = (settings.screen_width / 2,
                                 settings.screen_height / 2)
        self.colorBack = (155, 155, 155)
        self.fonts()
        self.text()
        self.textRects()
        self.update_rects()

    def fonts(self):
        self.font = pg.font.Font(settings.font_title, 50)
        self.font2 = pg.font.Font(settings.font_title, 10)

    def text(self):
        self.text1 = self.font.render('PLAY', True, (190, 190, 190))
        self.text2 = self.font.render('FEATURES', True, (190, 190, 190))
        self.text3 = self.font.render('CREDITS', True, (190, 190, 190))
        self.exit = self.font2.render('X', True, (190, 190, 190))

    def textRects(self):
        self.Rect1 = self.text1.get_rect()
        self.Rect2 = self.text2.get_rect()
        self.Rect3 = self.text3.get_rect()
        self.exitRect = self.exit.get_rect()

    def update_rects(self):
        self.Rect1.center = (settings.screen_width / 2, self.height / 3)
        self.Rect2.center = (settings.screen_width / 2, 2 * self.height / 3)
        self.Rect3.center = (settings.screen_width / 2, 3 * self.height / 3)
        self.exitRect.center = ((settings.screen_width + self.width) / 2 - 15,
                                (settings.screen_height - self.height) / 2 + 15)

    def update(self, events):
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return SCENES.PAUSE

            if ((settings.screen_width + self.width) / 2 - 25) <= mouse_x <= ((settings.screen_width + self.width) / 2 - 5)\
                and ((settings.screen_height - self.height) / 2 + 5) <= mouse_y <= ((settings.screen_height - self.height) / 2 + 25):
                self.exit = self.font2.render('X', True, (0, 200, 0))
                self.colorBack = (255, 255, 255)
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    return SCENES.TITLE
            else:
                self.exit = self.font2.render('X', True, (190, 190, 190))
                self.colorBack = (155, 155, 155)

            if settings.screen_width / 2 - 100 <= mouse_x\
                <= settings.screen_width / 2 + 100 and\
                self.height / 3- 25 <= mouse_y\
                <= self.height / 3 + 20:
                self.text1 = self.font.render('PLAY', True, (0, 200, 0))
                if event.type == pg.MOUSEBUTTONDOWN:
                    return SCENES.GAME
            else:
                self.text1 = self.font.render('PLAY', True, (190, 190, 190))

            if settings.screen_width / 2 - 200 <= mouse_x\
                <= settings.screen_width / 2 + 196 and\
                2 * self.height / 3 - 25 <= mouse_y\
                <= 2 * self.height / 3 + 20:
                self.text2 = self.font.render('FEATURES', True, (0, 200, 0))
            else:
                self.text2 = self.font.render('FEATURES', True, (190, 190, 190))

            if settings.screen_width / 2 - 174 <= mouse_x\
                <= settings.screen_width / 2 + 170 and\
                3 * self.height / 3 - 25 <= mouse_y\
                <= 3 * self.height / 3 + 20:
                self.text3 = self.font.render('CREDITS', True, (0, 200, 0))
                if event.type == pg.MOUSEBUTTONDOWN:
                    return SCENES.CREDITS
            else:
                self.text3 = self.font.render('CREDITS', True, (190, 190, 190))

        return SCENES.SETTINGS

    def draw(self, screen):
        self.surface.fill((25, 25, 25))
        self.surface.set_alpha(30)
        screen.blit(self.surface, self.surf_rect)
        pg.draw.rect(
            screen, self.colorBack, 
            ((settings.screen_width + self.width) / 2 - 25, 
            (settings.screen_height - self.height) / 2 + 5, 20, 20)
            )
        screen.blit(self.text1, self.Rect1)
        screen.blit(self.text2, self.Rect2)
        screen.blit(self.text3, self.Rect3)
        screen.blit(self.exit, self.exitRect)
