from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    screen_width: int = Field(None, env="SCREEN_WIDTH")
    screen_height: int = Field(None, env="SCREEN_HEIGHT")
    title: str = Field(None, env="TITLE")
    game_icon: str = Field(None, env="ICON_DIR")

    # Map settings
    map_width: int = Field(None, env="MAP_WIDTH")
    map_height: int = Field(None, env="MAP_HEIGHT")
    dx: int = Field(None, env='DX')

    # player configurations
    player_initial_width: int = Field(None, env="PLAYER_INITIAL_WIDTH")

    # Food configurations
    food_initial_width: int = Field(None, env='FOOD_INITIAL_WIDTH')
    food_initial_number: int = Field(None, env="FOOD_INITIAL_NUMBER")

    class Config:
        env_file = "settings.env"
        env_file_encoding = 'utf-8'


settings = Settings()
