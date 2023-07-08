from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import openai
from config import Config, load_config
from googletrans import Translator

router: Router = Router()
translator: Translator = Translator()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот на основе модели gpt-3.5-turbo\nНапиши мне что-нибудь')


@router.message()
async def send_message(message: Message):
    config: Config = load_config('.env')
    openai.api_key = config.openai_key.token
    promt = translator.translate(message.text, src='ru', dest='en').text
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": promt},
        ]
)
    ans = response['choices'][0]['message']['content']
    ans = translator.translate(ans, src='en', dest='ru').text
    await message.answer(ans)
