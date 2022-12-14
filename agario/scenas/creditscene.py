import pygame as pg

from agario.config import settings
from agario.schemas import SCENES

pg.font.init()


class Credits:
    def __init__(self):
        self.fonts()
        self.texts()
        self.textRects()
        self.update_rects()
        self.colorBack = (155, 155, 155)

    def fonts(self):
        self.font1 = pg.font.Font(settings.font_title,
                               25, bold=False)
        self.font2 = pg.font.Font(settings.font_title,
                               20, bold=False, italic=True)

    def texts(self):
        self.author1 = self.font1.render('Alan Camacho', True, (190, 190, 190))
        self.github1 = self.font2.render('https://github.com/Alan-Camacho-Restrepo',
                                   True, (210, 210, 210))
        self.author2 = self.font1.render('Luis Papiernik', True, (190, 190, 190))
        self.github2 = self.font2.render('https://github.com/Luispapiernik',
                                   True, (210, 210, 210))

        self.year = self.font1.render('2022 CopyrightÂ© ', True, (190, 190, 190))
        self.back = self.font2.render('<- ', True, (190, 190, 190))

    def textRects(self):
        self.textRect1 = self.author1.get_rect()
        self.gitRect1 = self.github1.get_rect()
        self.textRect2 = self.author2.get_rect()
        self.gitRect2 = self.github2.get_rect()
        self.textRect3 = self.year.get_rect()
        self.backRect = self.back.get_rect()

    def update_rects(self):
        self.textRect1.center = (settings.screen_width / 2, -150)
        self.gitRect1.center = (settings.screen_width / 2, -120)
        self.textRect2.center = (settings.screen_width / 2, -60)
        self.gitRect2.center = (settings.screen_width / 2, -30)
        self.textRect3.center = (settings.screen_width / 2, 60) 
        self.backRect.center = (39, 25)

    def update(self, events):
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_p:
                return SCENES.PAUSE

            if 10 <= mouse_x <= 50 and 10 <= mouse_y <= 40:
                self.back = self.font2.render('<-', True, (0, 200, 0))
                self.colorBack = (255, 255, 255)
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    return SCENES.TITLE
            else:
                self.back = self.font2.render('<- ', True, (100, 100, 100))
                self.colorBack = (155, 155, 155)

        return SCENES.CREDITS

    def draw(self, screen):
        screen.fill((0, 0, 0))
        # Horizontal lines
        pg.draw.line(
            screen, settings.lines_color_credits,
            (0, settings.screen_height / 15),
            (settings.screen_width, settings.screen_height / 15),
            4
        )
        pg.draw.line(
            screen, settings.lines_color_credits,
            (0, settings.screen_height / 2),
            (settings.screen_width, settings.screen_height / 2),
            4
        )
        pg.draw.line(
            screen, settings.lines_color_credits,
            (0, 14 * settings.screen_height / 15),
            (settings.screen_width, 14 * settings.screen_height / 15),
            4
        )

        # Vertical lines
        pg.draw.line(
            screen, settings.lines_color_credits,
            (2 * settings.screen_width / 9, 0),
            (2 * settings.screen_width / 9, settings.screen_height),
            4
        )
        pg.draw.line(
            screen, settings.lines_color_credits,
            (settings.screen_width / 2, 0),
            (settings.screen_width / 2, settings.screen_height),
            4
        )
        pg.draw.line(
            screen, settings.lines_color_credits,
            (7 * settings.screen_width / 9, 0),
            (7 * settings.screen_width / 9, settings.screen_height),
            4
        )

        pg.draw.rect(screen, self.colorBack, (10, 10, 40, 30))

        self.textRect1.y += 1
        self.gitRect1.y += 1
        self.textRect2.y += 1
        self.gitRect2.y += 1
        self.textRect3.y += 1

        screen.blit(self.author1, self.textRect1)
        screen.blit(self.github1, self.gitRect1)
        screen.blit(self.author2, self.textRect2)
        screen.blit(self.github2, self.gitRect2)
        screen.blit(self.year, self.textRect3)    
        screen.blit(self.back, self.backRect)    
