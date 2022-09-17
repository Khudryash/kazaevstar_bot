from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# main
start_keyboard = InlineKeyboardMarkup(row_width=2)
strt_kbrd1 = InlineKeyboardButton(f'Да', callback_data='start_kashback')
start_keyboard.add(strt_kbrd1)

# check data
chck_keyboard = InlineKeyboardMarkup(row_width=2)
chck_kbrd1 = InlineKeyboardButton(f'Да', callback_data='check_answer')
chck_kbrd2 = InlineKeyboardButton(f'Нет', callback_data='restart_kashback')
chck_keyboard.add(chck_kbrd1, chck_kbrd2)

# wait for admin
admin_keyboard = InlineKeyboardMarkup(row_width=2)
admin_kbrd1 = InlineKeyboardButton(f'Взяться за возврат', callback_data='move_to_work')
admin_keyboard.add(admin_kbrd1)

#admin check report
ad_chck_keyboard = InlineKeyboardMarkup(row_width=2)
ad_chck_kbrd1 = InlineKeyboardButton(f'Да', callback_data='send_report')
ad_chck_kbrd2 = InlineKeyboardButton(f'Нет', callback_data='fuck_off')
ad_chck_keyboard.add(ad_chck_kbrd1, ad_chck_kbrd2)
