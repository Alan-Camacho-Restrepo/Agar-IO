from pydantic import BaseSettings, Field
from typing import Tuple

class Settings(BaseSettings):
    screen_width: int = Field(None, env="SCREEN_WIDTH")
    screen_height: int = Field(None, env="SCREEN_HEIGHT")
    title: str = Field(None, env="TITLE")
    game_icon: str = Field(None, env="ICON_DIR")

    # Font settings
    font_score: str = Field(None, env="FONT_SCORE")
    font_title: str = Field(None, env="FONT_TITLE")

    # Colors feautures
    player_color: Tuple[int, int, int] = Field(None, env="PLAYER_COLOR")
    background_color: Tuple[int, int, int] = Field(None, env="BACKGROUND_COLOR")
    lines_color: Tuple[int, int, int] = Field(None, env="LINES_COLOR")

    # Map settings
    map_width: int = Field(None, env="MAP_WIDTH")
    map_height: int = Field(None, env="MAP_HEIGHT")
    dx: int = Field(None, env='DX')

    # player configurations
    player_initial_width: int = Field(None, env="PLAYER_INITIAL_WIDTH")

    # Food configurations
    food_initial_width: int = Field(None, env='FOOD_INITIAL_WIDTH')
    food_initial_number: int = Field(None, env="FOOD_INITIAL_NUMBER")

    # Enemy configurations
    enemy_initial_width: int = Field(None, env='ENEMY_INITIAL_WIDTH')
    enemy_initial_number: int = Field(None, env="ENEMY_INITIAL_NUMBER")
    enemy_speed: float = Field(None, env='ENEMY_SPEED')

    class Config:
        env_file = "settings.env"
        env_file_encoding = 'utf-8'


settings = Settings()
