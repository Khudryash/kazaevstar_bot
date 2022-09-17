from aiogram.dispatcher import FSMContext
from aiogram import types
from loader import dp, bot


# pip install
@dp.message_handler(commands=['help'], state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    media = types.MediaGroup()

    media.attach_photo(
        photo=types.InputFile('data/images/goldface_bot_img_1.jpeg'),
        caption='<u><b><i>Инструкция:</i></b></u>\n'
               '<u>1.</u> Напиши отзыв о купленном товаре на Wildberries. '
               'Будет здорово, если ты добавишь пару фотографий товара к отзыву.\n'
               '<u>2.</u> Сделай скриншот опубликованного отзыва и пришли его в этот чат с ботом.\n'
               '<u>3.</u> Напиши номер карты или телефона, который привязан к карте, '
               'название банка и Имя Фамилию, куда ты хочешь получить бонус.\n'
               '<u>4.</u> Готово. Обработка отзыва займёт 1-2 недели, '
               'после чего ты получишь бонус на карту и бот пришлёт уведомление об этом.',
        parse_mode=types.ParseMode.HTML
    )

    media.attach_photo(types.InputFile('data/images/goldface_bot_img_2.jpeg'))
    media.attach_photo(types.InputFile('data/images/goldface_bot_img_3.jpeg'))
    media.attach_photo(types.InputFile('data/images/goldface_bot_img_4.jpeg'))

    await bot.send_media_group(
        chat_id=message.chat.id,
        media=media
    )
    # await bot.send_message(
    #     chat_id=message.chat.id,
    #     text = '<u><b><i>Инструкция:</i></b></u>\n'
    #            '<u>1.</u> Напиши отзыв о купленном товаре на Wildberries. '
    #            'Будет здорово, если ты добавишь пару фотографий товара к отзыву.\n'
    #            '<u>2.</u> Сделай скриншот опубликованного отзыва и пришли его в этот чат с ботом.\n'
    #            '<u>3.</u> Напиши номер карты или телефона, который привязан к карте, '
    #            'название банка и Имя Фамилию, куда ты хочешь получить бонус.\n'
    #            '<u>4.</u> Готово. Обработка отзыва займёт 1-2 недели, '
    #            'после чего ты получишь бонус на карту и бот пришлёт уведомление об этом.',
    #     parse_mode=types.ParseMode.HTML
    # )
