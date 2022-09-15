from create_bot import dp
from aiogram import types
import keyboard as kb
from create_bot import bot

@dp.message_handler(commands='start')
async def send_welcome(m: types.Message):
    user_id = m.from_user.id
    await m.reply(f'<strong>Здарова, я - Леха.</strong>\n\n'
                  f'Я бот, который поможет тебе не проспать пару... :)\n\n'
                  f'Так, о чем это я... В общем, я <i>умею присылать расписание твоих пар по заданному тобой графику.</i>\n\n'
                  f'👇🏻Нажми на кнопку ниже и давай уже там согласуем, когда и чего...👇🏻'
                  , reply_markup=kb.timechoose_kb, parse_mode=types.ParseMode.HTML)

@dp.callback_query_handler(text='time')
async def time_choose(c : types.CallbackQuery):

    await c.answer('⏰Выберите удобное для вас время с помощью кнопок')

    await c.message.answer('<strong>👇🏻Доступные варианты👇🏻</strong>',
                           reply_markup=kb.timekb_markup, parse_mode=types.ParseMode.HTML)

    await c.answer()

    await bot.delete_message(chat_id=c.from_user.id, message_id=c.message.message_id)


@dp.callback_query_handler(text='usertime')
async def user_time(c : types.CallbackQuery):
    user_id = c.from_user.id



def register_handler(dp: dp):
    dp.message_handler(commands=['start'])