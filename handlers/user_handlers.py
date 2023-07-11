import openai

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from messages import messages

router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message) -> None:
    await message.answer('Привет!\nЯ бот на основе модели gpt-3.5-turbo\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на любое сообщение пользователя, кроме "/start"
@router.message()
async def send_message(message: Message) -> None:

    messages.append({
        "role": "user", "content": message.text
    })

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
      max_tokens=500,
    )

    ans = response['choices'][0]['message']['content']

    messages.append({
        "role": "assistant", "content": ans
    })

    await message.answer(ans)
