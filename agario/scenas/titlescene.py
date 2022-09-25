import pygame as pg

from agario.config import settings
from agario.scenas.scene import Scene
from agario.schemas import SCENES

pg.font.init()


class TitleScene(Scene):
    def __init__(self):
        font = pg.font.Font(settings.font_title, 40)
        self.text = font.render('Press SPACE to play', True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (settings.screen_width / 2,
                                settings.screen_height / 2)

        font1 = pg.font.Font(settings.font_title, 25)
        self.text1 = font1.render('settings', True, (0, 0, 0))
        self.textRect1 = self.text1.get_rect()
        self.textRect1.center = (settings.screen_width / 2,
                                 5 * settings.screen_height / 8)

        self.text2 = font1.render('credits', True, (0, 0, 0))
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = (settings.screen_width / 2,
                                 11 * settings.screen_height / 16)

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                return SCENES.GAME
        return SCENES.TITLE

    def draw(self, screen):
        screen.fill((100, 140, 145))
        # Horizontal lines
        pg.draw.line(
            screen, (100, 100, 100),
            (0, settings.screen_height / 15),
            (settings.screen_width, settings.screen_height / 15),
            4
        )
        pg.draw.line(
            screen, (100, 100, 100),
            (0, settings.screen_height / 2),
            (settings.screen_width, settings.screen_height / 2),
            4
        )
        pg.draw.line(
            screen, (100, 100, 100),
            (0, 14 * settings.screen_height / 15),
            (settings.screen_width, 14 * settings.screen_height / 15),
            4
        )

        # Vertical lines
        pg.draw.line(
            screen, (100, 100, 100),
            (2 * settings.screen_width / 9, 0),
            (2 * settings.screen_width / 9, settings.screen_height),
            4
        )
        pg.draw.line(
            screen, (100, 100, 100),
            (settings.screen_width / 2, 0),
            (settings.screen_width / 2, settings.screen_height),
            4
        )
        pg.draw.line(
            screen, (100, 100, 100),
            (7 * settings.screen_width / 9, 0),
            (7 * settings.screen_width / 9, settings.screen_height),
            4
        )

        # Circles design
        pg.draw.circle(
            screen, (255, 0, 0),
            ((3 / 4) * settings.screen_width / 9, 0),
            95, 5
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            (4 * settings.screen_width / 9, settings.screen_height / 15),
            190
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            (8 * settings.screen_width / 9, 0),
            40
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            (7 * settings.screen_width / 9, 3 * settings.screen_height / 15),
            60
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            (0.5 * settings.screen_width / 9,
            (29 / 2) * settings.screen_height / 15),
            50
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            (2 * settings.screen_width / 9,
            (27 / 2) * settings.screen_height / 15),
            85
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            ((17 / 2) * settings.screen_width / 9,
            11 * settings.screen_height / 15),
            30
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            (9 * settings.screen_width / 9, 18 * settings.screen_height / 15),
            230
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            ((11 / 2) * settings.screen_width / 9, settings.screen_height),
            85
        )
        pg.draw.circle(
            screen, (255, 0, 0),
            (4 * settings.screen_width / 9, 12 * settings.screen_height / 15),
            30
        )
        screen.blit(self.text, self.textRect)
        screen.blit(self.text1, self.textRect1)
        screen.blit(self.text2, self.textRect2)

