from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from data.config import admins_id, clients_id
from utils.keyboard import admin_keyboard
import logging


@dp.callback_query_handler(text='check_answer', state='*')
async def send_to_admins(call: types.CallbackQuery, state: FSMContext):
    if call.from_user.id not in clients_id:
        await bot.edit_message_reply_markup(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            reply_markup=None
        )
        data = await state.get_data()
        for admin in admins_id:
            await bot.send_photo(
                chat_id=admin,
                photo=data['screenshot'],
                caption=f'card: {data["card"]}\n'
                        f'bank: {data["bank"]}\n'
                        f'name: {data["name"]}\n'
                        f'client: t.me/{call.from_user.username} II{call.from_user.id}II\n'
                        f'status: request',
                reply_markup=admin_keyboard
            )

        await bot.send_message(
            chat_id=call.from_user.id,
            text='Спасибо! Твой отзыв принят в обработку. Мы сообщим как отправим бонус, если всё выполнено верно.'
        )
        clients_id.append(call.from_user.id)
        current_state = await state.get_state()
        if current_state is None:
            return

        logging.info('Cancelling state %r', current_state)
        # Cancel state and inform user about it
        await state.finish()
