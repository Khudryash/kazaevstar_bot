from aiogram import types
from loader import dp, bot
from data.user_data import Proofs
from aiogram.dispatcher import FSMContext
from utils.keyboard import chck_keyboard
from data.config import clients_id


@dp.callback_query_handler(text='start_kashback')
async def cashbackstart(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="Для получения подробной инструкции воспользуйся командой /help",
        parse_mode='Markdown'
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Пришли скриншот.\n"
             "Должен быть виден сам отзыв и товар, к которому он относится",
        parse_mode='Markdown'
    )
    await Proofs.screenshot.set()


@dp.message_handler(commands=['restart'])
async def cashbackrestart(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Для получения подробной инструкции воспользуйся командой /help",
        parse_mode='Markdown'
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="Пришли скриншот.\n"
             "Должен быть виден сам отзыв и товар, к которому он относится",
        parse_mode='Markdown'
    )
    await Proofs.screenshot.set()


@dp.callback_query_handler(lambda message: message.from_user.id not in clients_id, text='restart_kashback')
async def cashback_restart(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Для получения подробной инструкции воспользуйся командой /help",
        parse_mode='Markdown'
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Пришли скриншот.\n"
             "Должен быть виден сам отзыв и товар, к которому он относится",
        parse_mode='Markdown'
    )
    await Proofs.screenshot.set()


@dp.message_handler(content_types=['photo'], state=Proofs.screenshot)
async def get_screenshot(message: types.Message, state: FSMContext):
    await state.update_data(screenshot=message.photo[-1]['file_id'])
    await message.answer("Пришли номер карты или номер телефона")
    # tmp = await state.get_data()
    # await bot.send_photo(chat_id=message.from_user.id, photo=tmp['screenshot']['file_id'])
    await Proofs.next()


@dp.message_handler(state=Proofs.screenshot)
async def not_photo(message: types.Message):
    await message.reply("Пришли скриншот,\n"
                        "Должен быть виден сам отзыв и товар, к которому он относится.")


@dp.message_handler(lambda message: not "".join(message.text.split(' ')).isdigit(), state=Proofs.card)
async def process_card_invalid(message: types.Message):
    await message.reply("!!!Номер карты или телефона должен содержать только цифры!!!")


@dp.message_handler(lambda message: "".join(message.text.split(' ')).isdigit(), state=Proofs.card)
async def get_card(message: types.Message, state: FSMContext):
    if (len("".join(message.text.split(' '))) == 16) or (len("".join(message.text.split(' '))) == 11):
        await state.update_data(card=message.text)
        await message.answer('Теперь \nНапиши название вашего банка.')
        await Proofs.next()
    else:
        await message.reply('!!!Некорректно введён номер!!!')


@dp.message_handler(state=Proofs.bank)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(bank=message.text)
    await message.answer('И последнее \nНапиши имя и фамилию получателя.')
    await Proofs.next()


@dp.message_handler(state=Proofs.name)
async def get_bank(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Проверим данные перед отправкой")
    tmp = await state.get_data()
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=tmp['screenshot'],
        caption=f'card: {tmp["card"]}\nbank: {tmp["bank"]}\nname: {tmp["name"]}',
        reply_markup=chck_keyboard
    )
