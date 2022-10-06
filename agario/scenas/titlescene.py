import pygame as pg

from agario.config import settings
from agario.scenas.scene import Scene
from agario.schemas import SCENES

pg.font.init()


class TitleScene(Scene):
    def __init__(self):
        self.font = pg.font.Font(settings.font_title, 40)
        self.text = self.font.render('Press SPACE to play', True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (settings.screen_width / 2,
                                settings.screen_height / 2)

        self.font1 = pg.font.Font(settings.font_title, 25)
        self.text1 = self.font1.render('settings', True, (0, 0, 0))
        self.textRect1 = self.text1.get_rect()
        self.textRect1.center = (settings.screen_width / 2,
                                 5 * settings.screen_height / 8)

        self.text2 = self.font1.render('credits', True, (0, 0, 0))
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = (settings.screen_width / 2,
                                 11 * settings.screen_height / 16)

    def update(self, events):
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                return SCENES.GAME

            if settings.screen_width / 2 - 88 <= mouse_x\
                <= settings.screen_width / 2 + 85 and\
                11 * settings.screen_height / 16 - 10 <= mouse_y\
                <= 11 * settings.screen_height / 16 + 10:
                self.text2 = self.font1.render('credits', True, (0, 200, 0))
                if event.type == pg.MOUSEBUTTONDOWN:
                    return SCENES.CREDITS
            else:
                self.text2 = self.font1.render('credits', True, (0, 0, 0))

            if settings.screen_width / 2 - 100 <= mouse_x\
                <= settings.screen_width / 2 + 96 and\
                5 * settings.screen_height / 8 - 10 <= mouse_y\
                <= 5 * settings.screen_height / 8 + 10:
                self.text1 = self.font1.render('settings', True, (0, 200, 0))
                if event.type == pg.MOUSEBUTTONDOWN:
                    return SCENES.SETTINGS
            else:
                self.text1 = self.font1.render('settings', True, (0, 0, 0))

        return SCENES.TITLE

    def draw(self, screen):
        screen.fill(settings.background_color)
        # Horizontal lines
        pg.draw.line(
            screen, settings.lines_color,
            (0, settings.screen_height / 15),
            (settings.screen_width, settings.screen_height / 15),
            4
        )
        pg.draw.line(
            screen, settings.lines_color,
            (0, settings.screen_height / 2),
            (settings.screen_width, settings.screen_height / 2),
            4
        )
        pg.draw.line(
            screen, settings.lines_color,
            (0, 14 * settings.screen_height / 15),
            (settings.screen_width, 14 * settings.screen_height / 15),
            4
        )

        # Vertical lines
        pg.draw.line(
            screen, settings.lines_color,
            (2 * settings.screen_width / 9, 0),
            (2 * settings.screen_width / 9, settings.screen_height),
            4
        )
        pg.draw.line(
            screen, settings.lines_color,
            (settings.screen_width / 2, 0),
            (settings.screen_width / 2, settings.screen_height),
            4
        )
        pg.draw.line(
            screen, settings.lines_color,
            (7 * settings.screen_width / 9, 0),
            (7 * settings.screen_width / 9, settings.screen_height),
            4
        )

        # Circles design
        pg.draw.circle(
            screen, (255, 0, 0),
            ((3 / 4) * settings.screen_width / 9, 0),
            95
        )
        pg.draw.circle(
            screen, (200, 24, 40),
            ((3 / 4) * settings.screen_width / 9, 0),
            95, 5
        )

        pg.draw.circle(
            screen, (0, 100, 220),
            (4 * settings.screen_width / 9, settings.screen_height / 15),
            190
        )
        pg.draw.circle(
            screen, (0, 130, 230),
            (4 * settings.screen_width / 9, settings.screen_height / 15),
            190, 5
        )

        pg.draw.circle(
            screen, (107, 32, 174),
            (8 * settings.screen_width / 9, 0),
            40
        )
        pg.draw.circle(
            screen, (107, 32, 144),
            (8 * settings.screen_width / 9, 0),
            40, 5
        )

        pg.draw.circle(
            screen, (205, 100, 0),
            (7 * settings.screen_width / 9, 3 * settings.screen_height / 15),
            60
        )
        pg.draw.circle(
            screen, (195, 80, 40),
            (7 * settings.screen_width / 9, 3 * settings.screen_height / 15),
            60, 5
        )

        pg.draw.circle(
            screen, (12, 24, 200),
            (0.5 * settings.screen_width / 9,
            (29 / 2) * settings.screen_height / 15),
            50
        )
        pg.draw.circle(
            screen, (0, 60, 150),
            (0.5 * settings.screen_width / 9,
            (29 / 2) * settings.screen_height / 15),
            50, 5
        )

        pg.draw.circle(
            screen, (40, 232, 24),
            (2 * settings.screen_width / 9,
            (27 / 2) * settings.screen_height / 15),
            85
        )
        pg.draw.circle(
            screen, (80, 232, 24),
            (2 * settings.screen_width / 9,
            (27 / 2) * settings.screen_height / 15),
            85, 5
        )

        pg.draw.circle(
            screen, (26, 194, 125),
            ((17 / 2) * settings.screen_width / 9,
            11 * settings.screen_height / 15),
            30
        )
        pg.draw.circle(
            screen, (36, 164, 115),
            ((17 / 2) * settings.screen_width / 9,
            11 * settings.screen_height / 15),
            30, 5
        )

        pg.draw.circle(
            screen, (229, 27, 85),
            (9 * settings.screen_width / 9, 18 * settings.screen_height / 15),
            230
        )
        pg.draw.circle(
            screen, (210, 27, 65),
            (9 * settings.screen_width / 9, 18 * settings.screen_height / 15),
            230, 5
        )

        pg.draw.circle(
            screen, (255, 250, 0),
            ((11 / 2) * settings.screen_width / 9, settings.screen_height),
            85
        )
        pg.draw.circle(
            screen, (255, 215, 30),
            ((11 / 2) * settings.screen_width / 9, settings.screen_height),
            85, 5
        )

        pg.draw.circle(
            screen, (250, 0, 255),
            (4 * settings.screen_width / 9, 12 * settings.screen_height / 15),
            30
        )
        pg.draw.circle(
            screen, (200, 50, 210),
            (4 * settings.screen_width / 9, 12 * settings.screen_height / 15),
            30, 5
        )

        pg.draw.circle(
            screen, (31, 145, 95),
            ((5 / 3) * settings.screen_width / 9, 
              5 * settings.screen_height / 15),
            35
        )
        pg.draw.circle(
            screen, (0, 140, 104),
            ((5 / 3) * settings.screen_width / 9, 
              5 * settings.screen_height / 15),
            35, 5
        )

        screen.blit(self.text, self.textRect)
        screen.blit(self.text1, self.textRect1)
        screen.blit(self.text2, self.textRect2)
