from aiogram import types
from loader import dp
from utils.keyboard import start_keyboard
from data.config import clients_id


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(
        text=f"Привет, {message.from_user.first_name} \n"
             f"Мы благодарны тебе за покупку в нашем магазине и "
             f"хотим подарить тебе небольшой бонус в виде возврата 50 рублей на карту.\n"
    )
    await message.answer(
        text="Готов приступить?",
        reply_markup=start_keyboard
    )

    if message.from_user.id in clients_id:
        clients_id.remove(message.from_user.id)
