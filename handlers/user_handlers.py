from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import openai
from config import Config, load_config

router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот на основе моделе text-davinci-001\nНапиши мне что-нибудь')


@router.message()
async def send_message(message: Message):
    config: Config = load_config('.env')
    openai.api_key = config.openai_key.token
    promt = message.text
    response = openai.Completion.create(engine='text-davinci-001', prompt=promt)
    ans = response['choices'][0]['text']
    await message.answer(ans)
