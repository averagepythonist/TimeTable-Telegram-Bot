from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


# Клавиатура с выбором времени

inline_time_button = InlineKeyboardButton(text='🕐Выбрать удобное время', callback_data='time')
timechoose_kb = InlineKeyboardMarkup(row_width=1)

timechoose_kb.add(inline_time_button)

# Выбор конкретного времени

inline_time1 = InlineKeyboardButton(text='🕔5:00 утра', callback_data='5:00AM')
inline_time2 = InlineKeyboardButton(text='🕕6:00 утра', callback_data='6:00AM')
inline_time3 = InlineKeyboardButton(text='🕖7:00 утра(по умолчанию)', callback_data='7:00AM')
inline_time4 = InlineKeyboardButton(text='🕗8:00 утра', callback_data='8:00AM')
inline_time5 = InlineKeyboardButton(text='🕘9:00 утра', callback_data='9:00AM')
inline_time6 = InlineKeyboardButton(text='🕘10:00 утра', callback_data='10:00AM')
inline_time_user = InlineKeyboardButton(text='❓⏰Свое время', callback_data='usertime')

timekb_markup = InlineKeyboardMarkup(row_width=3)

timekb_markup.add(inline_time1, inline_time2, inline_time3, inline_time4, inline_time5, inline_time6,inline_time_user)










