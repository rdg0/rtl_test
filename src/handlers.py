import json
from aiogram import Dispatcher, types


from db import get_collection, get_aggregation
from services import (
    validate_msg, get_labels, create_me_friendly_dict, preserialazing
)


async def cmd_start(message: types.Message):
    """Хендлер для приветствия."""
    await message.reply("Привет!")


async def get_data(message: types.Message):
    """Хэндлер для обработки всех сообщений."""
    if validate_msg(message):
        request = create_me_friendly_dict(message)
        labeles = get_labels(request)
        collection = get_collection()
        aggrigate_collection = get_aggregation(collection, request)
        data = preserialazing(aggrigate_collection, labeles, request)
        await message.reply(json.dumps(data))

    else:
        await message.reply('Проверьте корректность ввода')


def register_handlers(dp: Dispatcher):
    """Регистрируем все хэндлеры здесь."""
    dp.register_message_handler(cmd_start, commands=['start', 'help'])
    dp.register_message_handler(get_data)
