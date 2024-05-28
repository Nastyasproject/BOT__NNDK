import logging  # библиотека логирования (журналирование)
import asyncio  # библиотека для асинхронного программирования
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from handlers import register_message_handler
from handlers import commands_for_bot
from db import async_create_table


# асинхронный вызов функции - конкурентный вызов с ожиданием события для продолжения процесса выполнения
async def main():
    """Настройки перед запуском"""

    # уровень логирования
    logging.basicConfig(level=logging.INFO)

    # создание экземпляров классов Bot и Dispatcher
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # функция для вызова хендлеров из пакета handlers
    register_message_handler(dp)

    # передача списка команд боту
    await bot.set_my_commands(commands=commands_for_bot)
    await dp.start_polling(bot)


# запуск бота через long_polling
if __name__ == "__main__":
    # обработка исключений try-except
    try:
        asyncio.run(async_create_table())
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logging.info("Пока!")