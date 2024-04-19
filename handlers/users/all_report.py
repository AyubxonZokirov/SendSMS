import re
from aiogram import types
from loader import dp, bot
from keyboards.inline.main_buttons import main_button, type_price, home_button
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from utils.db_api import database as db
import sqlite3 as sq

db1 = sq.connect("sendSMS.db")
cur = db1.cursor()

# print(total_payments1)
# baza None va str qytarsa olmasin
# total_paymentss = 0
# for total in total_payments:
#     if total[0] is not None and not isinstance(total[0], str):
#         total_paymentss += int(total[0])
#     else:
#         pass
# print(total_paymentss)

@dp.callback_query_handler(text='hisobot')
async def all_report(request: types.CallbackQuery):
    await request.message.answer(f"Mijozlarni bir qismi $ da qolgan qismi esa So\'mda xarid qilishkani sabab Hisobotni"
                                 f" ikkiga bo\'ldik\n\nKerakli Hisobotni tanlash uchun quydagi tugmalardan birini bosing", reply_markup=type_price)

@dp.callback_query_handler(text='dollar')
async def dollar_rep(request: types.CallbackQuery):
    credit_price = cur.execute("SELECT first_price FROM clients WHERE first_price LIKE '%$%'").fetchall()
    credit_with_per = cur.execute("SELECT price FROM clients WHERE price LIKE '%$%'").fetchall()
    total_payments2 = cur.execute("""SELECT total_payment FROM clients WHERE total_payment LIKE "%$%" """).fetchall()

    cr_pr = [cr_pr[0] for cr_pr in credit_price]
    cr_pr_per = [cr_prr[0] for cr_prr in credit_with_per]
    total_payments02 = [total_payments[0] for total_payments in total_payments2]
    dollar_len = len(cr_pr)

    org = Image.open('C:/Users/User/PycharmProjects/SendSMS/for_images/Hisobot.png')
    img = org.filter(ImageFilter.DETAIL)

    font = ImageFont.truetype(font='arial.ttf', size=72)
    draw = ImageDraw.Draw(img)

    total_credits = []
    for tc in cr_pr_per:
        total_credit = re.findall(r'\d+', tc)
        total_credits.append(int(total_credit[0]))
        # total_credits += int(tc)

    first_price = []
    for fp in cr_pr:
        f_price = re.findall(r'\d+', fp)
        first_price.append(int(f_price[0]))

    dollar_pay = []
    for dp in total_payments02:
        d_pay = re.findall(r'\d+', dp)
        dollar_pay.append(int(d_pay[0]))

    first = int(sum(total_credits))
    second = int(sum(dollar_pay))
    # print(second)
    # thirst = str(total_second)
    fourth = int(sum(first_price))
    fifth = str(first-fourth)
    # print(f'{total_credits}\n{first}')
    draw.text(xy=(1050, 167), text=f"{str(first)} $", font=font, fill='white')
    draw.text(xy=(1050, 305), text=f"{str(dollar_len)} ta", font=font, fill='white')
    draw.text(xy=(1050, 445), text=f"{str(second)} $", font=font, fill='white')
    draw.text(xy=(1050, 582), text=f"{str(fourth)} $", font=font, fill='white')
    draw.text(xy=(1050, 717), text=f"{fifth} $", font=font, fill='white')
    img.save('C:/Users/User/PycharmProjects/SendSMS/for_images/Report.png')
    chat_id = request.message.chat.id
    with open("C:/Users/User/PycharmProjects/SendSMS/for_images/Report.png", 'rb') as photo:
        await bot.send_photo(chat_id, photo)
        await request.message.answer(text=f' ```js \nJami Summa: {first} $\n\nJami sotuvlar soni: {dollar_len} ta\n\n'
                                          f'Jami to\'langan summa: {second} $\n\nJami tikilgan summa: {fourth} $\n\n'
                                          f'Jami foyda: {fifth} $ ``` ', parse_mode="MARKDOWN", reply_markup=home_button)

@dp.callback_query_handler(text='som')
async def dollar_rep(request: types.CallbackQuery):
    credit_price2 = cur.execute("""SELECT first_price FROM clients WHERE first_price LIKE "%So'm%" """).fetchall()
    credit_with_per2 = cur.execute("""SELECT price FROM clients WHERE price LIKE "%So'm%" """).fetchall()
    total_payments1 = cur.execute("""SELECT total_payment FROM clients WHERE total_payment LIKE "%So'm%" """).fetchall()

    cr_pr2 = [cr_prrr[0] for cr_prrr in credit_price2]
    cr_pr_per2 = [cr_prrrr[0] for cr_prrrr in credit_with_per2]
    total_payments01 = [total_payments1[0] for total_payments1 in total_payments1]
    som_len = len(cr_pr2)

    org = Image.open('C:/Users/User/PycharmProjects/SendSMS/for_images/Hisobot.png')
    img = org.filter(ImageFilter.DETAIL)

    font = ImageFont.truetype(font='arial.ttf', size=62)
    draw = ImageDraw.Draw(img)

    total_credits = []
    for tc in cr_pr_per2:
        total_credit = re.findall(r'\d+', tc)
        total_credits.append(int(total_credit[0]))
        # total_credits += int(tc)

    first_price = []
    for fp in cr_pr2:
        f_price = re.findall(r'\d+', fp)
        first_price.append(int(f_price[0]))

    # print(total_payments1)
    som_pay = []
    for sp in total_payments01:
        s_pay = re.findall(r'\d+', sp)
        som_pay.append(int(s_pay[0]))
        # print(som_pay)

    first = int(sum(total_credits))
    second = int(sum(som_pay))
    # print(second)
    # thirst = str(total_second)
    fourth = int(sum(first_price))
    fifth = str(first-fourth)
    # print(f'{total_credits}\n{first}')
    draw.text(xy=(850, 175), text=f"{str(first)} So'm", font=font, fill='white')
    draw.text(xy=(850, 315), text=f"{str(som_len)} ta", font=font, fill='white')
    draw.text(xy=(850, 455), text=f"{str(second)} So'm", font=font, fill='white')
    draw.text(xy=(850, 590), text=f"{str(fourth)} So'm", font=font, fill='white')
    draw.text(xy=(850, 725), text=f"{fifth} So'm", font=font, fill='white')
    img.save('C:/Users/User/PycharmProjects/SendSMS/for_images/Report.png')
    chat_id = request.message.chat.id
    with open("C:/Users/User/PycharmProjects/SendSMS/for_images/Report.png", 'rb') as photo:
        await bot.send_photo(chat_id, photo)
        await request.message.answer(text=f' ```js \nJami Summa: {first} so\'m\n\nJami sotuvlar soni: {som_len} ta\n\n'
                                          f'Jami to\'langan summa: {second} so\'m\n\nJami tikilgan summa: {fourth} '
                                          f'so\'m\n\nJami foyda: {fifth} so\'m ``` ',
                                     parse_mode="MARKDOWN", reply_markup=home_button)

@dp.callback_query_handler(text='home')
async def cancel(message: types.CallbackQuery):
    await message.message.answer(text=f"Assalom alaykum! Nima xizmat?", reply_markup=main_button)



