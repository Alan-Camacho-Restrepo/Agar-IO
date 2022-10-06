import pygame as pg

from agario.config import settings
from agario.scenas.gamescene import GameScene
from agario.scenas.pausescene import Pause
from agario.scenas.settingscene import SettingScene
from agario.scenas.titlescene import TitleScene
from agario.scenas.gameoverscene import GameOver
from agario.scenas.creditscene import Credits
from agario.scenas.winscene import Win
from agario.schemas import SCENES

pg.display.init()


class GameManager:
    def __init__(self):
        self.screen = pg.display.set_mode((settings.screen_width,
                                           settings.screen_height))
        self.initialized_features()
        self.initialized_scenes()
        self.current_scene = self.scenes[SCENES.TITLE]

    def initialized_features(self):
        GameIcon = pg.image.load(settings.game_icon)
        self.clock = pg.time.Clock()
        pg.display.set_caption(settings.title)
        pg.display.set_icon(GameIcon)
        self.quit = False

    def initialized_scenes(self):
        self.scenes = {
            SCENES.TITLE: TitleScene(),
            SCENES.GAME: GameScene(),
            SCENES.PAUSE: Pause(),
            SCENES.SETTINGS: SettingScene(),
            SCENES.GAMEOVER: GameOver(),
            SCENES.CREDITS: Credits(),
            SCENES.WIN: Win()
        }

    def run(self):
        while not self.quit:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.quit = True
                if event.type == pg.KEYDOWN and event.key == pg.K_q:
                    self.quit = True

            out = self.current_scene.update(events)
            self.current_scene = self.scenes[out]
            self.current_scene.draw(self.screen)
            pg.display.flip()
            self.clock.tick(60)

        pg.display.quit()
