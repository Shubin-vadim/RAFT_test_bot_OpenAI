from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import openai
from config import Config, load_config
from messanges import messages
from googletrans import Translator

router: Router = Router()
translator: Translator = Translator()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот на основе модели gpt-3.5-turbo\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на любое сообщение пользователя, кроме "/start"
@router.message()
async def send_message(message: Message):
    config: Config = load_config('.env')
    openai.api_key = config.openai_key.token
    promt = translator.translate(message.text, src='ru', dest='en').text

    messages.append({
        "role": "user", "content": promt
    })

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
      max_tokens=500,
    )

    ans = response['choices'][0]['message']['content']
    ans = translator.translate(ans, src='en', dest='ru').text
    messages.append({
        "role": "assistant", "content": ans
    })
    await message.answer(ans)
