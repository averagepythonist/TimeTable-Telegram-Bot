from create_bot import dp
from aiogram import types
import keyboard as kb
from create_bot import bot
from database import sql_data as sq


@dp.message_handler(commands='start')
async def send_welcome(m: types.Message):
    user_id = m.from_user.id
    sq.check_user(user_id)
    await m.reply(f'<strong>Здарова, я - Леха.</strong>\n\n'
                  f'Я бот, который поможет тебе не проспать пару... :)\n\n'
                  f'Так, о чем это я... В общем, '
                  f'я <i>умею присылать расписание твоих пар по заданному тобой графику.</i>\n\n'
                  f'👇🏻Нажми на кнопку ниже и давай уже там согласуем, когда и чего...👇🏻'
                  , reply_markup=kb.timechoose_kb, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text='time')
async def time_choose(c: types.CallbackQuery):
    await c.answer('⏰Выберите удобное для вас время с помощью кнопок')
    await c.message.answer('<strong>👇🏻Доступные варианты👇🏻</strong>',
                           reply_markup=kb.timekb_markup, parse_mode=types.ParseMode.HTML)
    await c.answer()
    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)


# @dp.callback_query_handler(text='user_time')
# async def user_time(c : types.CallbackQuery):
#     user_id = c.from_user.id
#     await c.message.answer('<strong>👇🏻Введите удобное Вам время в формате HH:MM👇🏻</strong>',
#                            parse_mode=types.ParseMode.HTML)
#     await c.message
#     notify_time = c
#     sq.update_time(user_id, notify_time)

@dp.callback_query_handler(text='5:00AM')
async def time_5(c: types.CallbackQuery):
    user_id = c.from_user.id
    notify_time = '5:00'
    db_time = notify_time#.replace(notify_time[1], '')
    sq.update_time(user_id, db_time)
    await bot.send_message(c.from_user.id,
                           f'<strong>Удобное для Вас время рассылки в {notify_time}.</strong> Я все правильно понял?'
                           f'\n\nЕсли хотите изменить время, нажмите на соотвествующую кнопку в меню',
                           parse_mode=types.ParseMode.HTML, reply_markup=kb.main_menu)
    if sq.check_time_is_not_null(user_id, db_time) == True:
        await c.answer('✅ Время рассылки успешно обновлено')
    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)
@dp.callback_query_handler(text='6:00AM')
async def time_5(c: types.CallbackQuery):
    user_id = c.from_user.id
    notify_time = '6:00'
    db_time = notify_time#.replace(notify_time[1], '')
    sq.update_time(user_id, db_time)
    await bot.send_message(c.from_user.id,
                           f'<strong>Удобное для Вас время рассылки в {notify_time}.</strong> Я все правильно понял?'
                           f'\n\nЕсли хотите изменить время, нажмите на соотвествующую кнопку в меню',
                           parse_mode=types.ParseMode.HTML, reply_markup=kb.main_menu)
    if sq.check_time_is_not_null(user_id, db_time) == True:
        await c.answer('✅ Время рассылки успешно обновлено')
    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)
@dp.callback_query_handler(text='7:00AM')
async def time_5(c: types.CallbackQuery):
    user_id = c.from_user.id
    notify_time = '7:00'
    db_time = notify_time#.replace(notify_time[1], '')
    sq.update_time(user_id, db_time)
    await bot.send_message(c.from_user.id,
                           f'<strong>Удобное для Вас время рассылки в {notify_time}.</strong> Я все правильно понял?'
                           f'\n\nЕсли хотите изменить время, нажмите на соотвествующую кнопку в меню',
                           parse_mode=types.ParseMode.HTML, reply_markup=kb.main_menu)
    if sq.check_time_is_not_null(user_id, db_time) == True:
        await c.answer('✅ Время рассылки успешно обновлено')
    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)
@dp.callback_query_handler(text='8:00AM')
async def time_5(c: types.CallbackQuery):
    user_id = c.from_user.id
    notify_time = '8:00'
    db_time = notify_time#.replace(notify_time[1], '')
    sq.update_time(user_id, db_time)
    await bot.send_message(c.from_user.id,
                           f'<strong>Удобное для Вас время рассылки в {notify_time}.</strong> Я все правильно понял?'
                           f'\n\nЕсли хотите изменить время, нажмите на соотвествующую кнопку в меню',
                           parse_mode=types.ParseMode.HTML, reply_markup=kb.main_menu)
    if sq.check_time_is_not_null(user_id, db_time) == True:
        await c.answer('✅ Время рассылки успешно обновлено')
    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)
@dp.callback_query_handler(text='9:00AM')
async def time_5(c: types.CallbackQuery):
    user_id = c.from_user.id
    notify_time = '9:00'
    db_time = notify_time#.replace(notify_time[1], '')
    sq.update_time(user_id, db_time)
    await bot.send_message(c.from_user.id,
                           f'<strong>Удобное для Вас время рассылки в {notify_time}.</strong> Я все правильно понял?'
                           f'\n\nЕсли хотите изменить время, нажмите на соотвествующую кнопку в меню',
                           parse_mode=types.ParseMode.HTML, reply_markup=kb.main_menu)
    if sq.check_time_is_not_null(user_id, db_time) == True:
        await c.answer('✅ Время рассылки успешно обновлено')
    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)
@dp.callback_query_handler(text='10:00AM')
async def time_5(c: types.CallbackQuery):
    user_id = c.from_user.id
    notify_time = '10:00'
    db_time = notify_time#.replace(notify_time[1], ''))
    sq.update_time(user_id, db_time)
    await bot.send_message(c.from_user.id,
                           f'<strong>Удобное для Вас время рассылки в {notify_time}.</strong> Я все правильно понял?'
                           f'\n\nЕсли хотите изменить время, нажмите на соотвествующую кнопку в меню',
                           parse_mode=types.ParseMode.HTML, reply_markup=kb.main_menu)
    if sq.check_time_is_not_null(user_id, db_time) == True:
        await c.answer('✅ Время рассылки успешно обновлено')
    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)

@dp.message_handler(text='📳🕰Сменить время рассылки')
async def change_notify_time(m : types.Message):
    await m.answer('<strong>👇🏻Доступные варианты👇🏻</strong>',
                           reply_markup=kb.timekb_markup, parse_mode=types.ParseMode.HTML)
    await bot.delete_message(chat_id=m.from_user.id, message_id=m.message_id)


# Просмотр расписания (нужна excel таблица)
@dp.message_handler(text='🗒Посмотреть расписание')
async def check_timetable(m : types.Message):
    pass

# Будет скидывать точку на карте, нужна машина состояний, либо придется делать миллиард кнопок :(
@dp.message_handler(text='🏛Найти корпус')
async def find_building(m : types.Message):
    pass







def register_handler(dp: dp):
    dp.message_handler(commands=['start'])
