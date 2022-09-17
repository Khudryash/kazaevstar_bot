from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@dp.callback_query_handler(text='move_to_work')
async def moving(call: types.CallbackQuery):
    new_admin_keyboard = InlineKeyboardMarkup(row_width=2)
    n_a_kbrd = InlineKeyboardButton(f'{call.from_user.username} взялся/взялась за возврат', callback_data='end_of_work')
    new_admin_keyboard.add(n_a_kbrd)
    text_temp = call.message.caption
    await bot.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption=text_temp.replace('status: request', 'status: in_work')
    )
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=new_admin_keyboard
    )

@dp.callback_query_handler(text='end_of_work')
async def removing(call: types.CallbackQuery):
    text_temp = call.message.caption
    client = text_temp.split('II')[1].split('II')[0]
    await bot.edit_message_reply_markup(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=None
    )
    await bot.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption=text_temp.replace('status: in_work', 'status: done')
    )

    await bot.send_message(
        chat_id=client,
        text="Готово, деньги скоро поступят"
    )
