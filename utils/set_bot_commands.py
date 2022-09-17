from aiogram import types
from data.config import admins_id


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустить бота'),
            types.BotCommand('cancel', 'Закончить общение'),
            types.BotCommand('help', 'Получить инструкцию')
        ],
        scope=types.bot_command_scope.BotCommandScopeAllPrivateChats()
    )
    await dp.bot.set_my_commands(
        [
            types.BotCommand('error', 'Ошибка'),
        ],
        scope=types.bot_command_scope.BotCommandScopeChat(chat_id=-1001668232300)
    )
