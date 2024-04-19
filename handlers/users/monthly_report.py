import re

from aiogram import types
from loader import dp
from keyboards.inline.months import months_button
import sqlite3 as sq
db = sq.connect("sendSMS.db")
cur = db.cursor()

@dp.callback_query_handler(text="oylik_hisobot")
async def monthly_report(request: types.CallbackQuery):
    await request.message.answer(text=f"Kerakli oyni tanlang!", reply_markup=months_button)

@dp.callback_query_handler(text="dekabr")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '12'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '12' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '12' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Dekabr oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nDekabr oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")

@dp.callback_query_handler(text="yanvar")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '01'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '01' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '01' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Yanvar oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nYanvar oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")

@dp.callback_query_handler(text="fevral")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '02'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '02' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '02' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Fevral oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nFevral oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")

@dp.callback_query_handler(text="mart")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '03'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '03' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '03' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Mart oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nMart oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")


@dp.callback_query_handler(text="aprel")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '04'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '04' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '04' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Aprel oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(text=f" ```js \nAprel oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ", parse_mode="MARKDOWN")


@dp.callback_query_handler(text="may")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '05'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '05' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '05' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"May oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nMay oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")


@dp.callback_query_handler(text="iyun")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '06'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '06' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '06' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Iyun oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nIyun oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")


@dp.callback_query_handler(text="iyul")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '07'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '07' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '07' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Iyul oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nIyul oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")


@dp.callback_query_handler(text="avgust")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '08'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '08' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '08' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Avgust oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nAvgust oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")


@dp.callback_query_handler(text="sentyabr")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '09'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '09' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '09' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Sentyabr oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nSentyabr oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")


@dp.callback_query_handler(text="oktyabr")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '10'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '10' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '10' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Oktyabr oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nOktyabr oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")


@dp.callback_query_handler(text="noyabr")
async def dekabr(request: types.CallbackQuery):
    info = cur.execute("SELECT name, start FROM clients WHERE strftime('%m', start) = '11'").fetchall()
    priced = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '11' AND price LIKE "%$%" """).fetchall()
    prices = cur.execute("""SELECT price FROM clients WHERE strftime('%m', start) = '11' AND price LIKE "%So'm%" """).fetchall()
    dpr = [pr[0] for pr in priced]
    spr = [sr[0] for sr in prices]
    dollar_pay = []
    som_pay = []
    for dp in dpr:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))
    for sp in spr:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
    sumdp = int(sum(dollar_pay))
    sumsp = int(sum(som_pay))
    if not info:
        await request.message.answer(text=f"Noyabr oyida mijoz topilmadi")
        return
    withindex = [(index + 1, name, date) for index, (name, date) in enumerate(info)]
    info_text = "\n".join([f"{index}. {name}-{date}" for index, name, date in withindex])
    await request.message.answer(
        text=f" ```js \nNoyabr oyi hisoboti\n\n{info_text}\nBu oy chiqarilgan Telefonlar summasi:\n{sumdp}$ va {sumsp}So'm ``` ",
        parse_mode="MARKDOWN")
