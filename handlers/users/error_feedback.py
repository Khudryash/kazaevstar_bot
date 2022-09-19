from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from data.config import admins_id
from utils.keyboard import ad_chck_keyboard
import re


@dp.message_handler(lambda message: message.chat.id in admins_id, commands='error')
async def error_report(message: types.Message):
    try:
        if 'status: done' not in message.reply_to_message.caption:
            msg = message.reply_to_message
            if msg.from_user.username != "kazaev_bot":
                await message.answer('Вместе с этой командой необходимо прислать сообщение от бота')
            else:
                client = msg.caption.split('client: ')[1].split('status:')[0]
                report = message.text.split("/error")[1]
                await message.answer("Проверим данные перед отправкой")
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'<u><b>client:</b></u> {client}\n'
                         f'<u><b>message:</b></u> {report}',
                    reply_to_message_id=msg.message_id,
                    parse_mode=types.ParseMode.HTML,
                    reply_markup=ad_chck_keyboard
                )
        else:
            await message.answer('Запрос уже обработан и снят с работы')
    except (AttributeError, TypeError):
        await message.answer('Вместе с этой командой необходимо прислать сообщение бота с карточкой клиента!!')
    except IndexError:
        await message.answer('Вместе с этой командой необходимо написать сообщение!!')


@dp.callback_query_handler(text='send_report', state="*")
async def send_fucking_report(call: types.CallbackQuery):
    try:
        client_id = re.search('II(.+?)II', call.message.text.split("message: ")[0]).group(1)
        await bot.send_message(
            chat_id=client_id,
            text=call.message.text.split('message: ')[1] + 'Используй команду /restart, чтобы попробовать снова'
        )
    except AttributeError:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Ой, произошла ошибка, бот не нашёл id пользователя"
        )
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )


@dp.callback_query_handler(text='fuck_off', state="*")
async def shuttind_thefuck_off(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Понял, иду нахуй",
        reply_markup=None
    )
