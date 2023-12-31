import logging
import asyncio
import openai

from aiogram import Bot, Dispatcher
from config import Config, load_config
from handlers import user_handlers


logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s'
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config('.env')

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML'
                   )

    openai.api_key = config.openai_key.token

    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
