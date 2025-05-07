import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage

from tg_bot.config import load_config

logger = logging.getLogger(__name__)

async def main() -> None:
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage() if config.tg_bot.use_redis else MemoryStorage()

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)

    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")