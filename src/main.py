from aiogram import executor

from create_bot import bot, dp
from exceptions import EnvVariableNotFound
from handlers import register_handlers
from settings import TELEGRAM_TOKEN, DB_NAME, COLLECTION_NAME, TELEGRAM_CHAT_ID


async def on_startup(dispatcher) -> None:
    """Выполняется при включении бота."""
    await bot.send_message(TELEGRAM_CHAT_ID, 'Бот включился')


def check_settings() -> bool:
    """Проверяем наличием необходимых токенов."""
    return all([DB_NAME, COLLECTION_NAME, TELEGRAM_CHAT_ID, TELEGRAM_TOKEN,])


def main() -> None:
    """Основная функция бота."""
    if not check_settings():
        raise EnvVariableNotFound(
            'Отсутствуют переменные окружения. Проверьте settings.py, .env'
        )
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    main()
