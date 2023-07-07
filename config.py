from dataclasses import dataclass
from environs import Env


@dataclass
class Tokens:
    token: str


@dataclass
class Config:
    tg_bot: Tokens
    openai_key: Tokens


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=Tokens(token=env('BOT_TOKEN')), openai_key=Tokens(token=env('OPENAI_KEY')))
