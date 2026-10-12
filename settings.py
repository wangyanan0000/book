from typing import Any, Literal, Mapping

from django.conf import settings
from pydantic_settings import BaseSettings, SettingsConfigDict, CliSettingsSource, PydanticBaseSettingsSource
from functools import lru_cache

class Settings(BaseSettings):
    APP_TITLE:str
    model_config = SettingsConfigDict(env_file=".env")
    @lru_cache()
    def get_setting(self):
        return settings
