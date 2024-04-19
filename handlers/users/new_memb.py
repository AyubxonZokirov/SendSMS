import re
import datetime
import sqlite3 as sq

from aiogram import types
from loader import dp
from keyboards.inline.main_buttons import main_button, cancel_button, type_price, home_button
from aiogram.types import CallbackQuery
from states.nmemb_state import Nmemb_state
from aiogram.dispatcher import FSMContext
from utils.db_api import database as db
from utils.db_api.database import users
from utils.db_api.eskiz_api import send_sms, format_phone_number

db1 = sq.connect("sendSMS.db")
cur = db1.cursor()

@dp.callback_query_handler(text='yangi_mijoz')
async def new_memb(request: CallbackQuery):
    await request.message.answer(text=f"👤Yangi foydalanuvchini Ismini kiriting!", parse_mode="MARKDOWN", reply_markup=cancel_button)
    await Nmemb_state.Add_Uname.set()
    await request.answer()

@dp.message_handler(state=Nmemb_state.Add_Uname)
async def name_memb(message: types.Message, state: FSMContext):
    name = message.text
    for user in users:
        if name == user[0]:
            await message.answer(text=f'Bunday mijoz oldin ro\'yxatdan o\'tkazilgan!\n\nIltimos boshxa nom kiriting', reply_markup=cancel_button)
            return
        # else:
    memb = message.text
    await state.update_data(name=message.text)
    await Nmemb_state.next()
    await message.answer(text=f"📞Yangi foydalanuvchining Telefon raqamni quydagi ko'rinishda kiriting\n\n+998901234567", reply_markup=cancel_button)
            # return

@dp.message_handler(state=Nmemb_state.Add_Unumb)
async def tel_memb(message: types.Message, state: FSMContext):
    numb = message.text
    # n = str(numb)
    # try:
    #     int_numb = int(numb)
    if re.match(r'^\+998\d{9}$', numb):
        await state.update_data(tel=numb)
        await Nmemb_state.next()
        await message.answer(text=f"📱Telefon Modeli\\Nomini kiriting\n\nMisol:iPhone 15 pro", reply_markup=cancel_button)
    else:
        await message.answer(text="🆘Raqam kiritishda xatolik bor!🆘 \n\nQaytadan urinib koring", reply_markup=cancel_button)
    # except ValueError:
    #     await message.answer(text="Raqam kiritishda xatolik bor! \n\nQaytadan urinib koring", reply_markup=cancel_button)

@dp.message_handler(state=Nmemb_state.Add_Tname)
async def name_item(message: types.Message, state: FSMContext):
    tname = message.text
    await state.update_data(tname=tname)
    await Nmemb_state.next()
    await message.answer(text=f"🆔Telefoning IMEI raqamini kiriting")

@dp.message_handler(state=Nmemb_state.Add_IMEI)
async def items_imei(message: types.Message, state: FSMContext):
    imei = message.text
    # try:
    #     tel_imei = int(imei)
    # if re.match(r'^\d{15}$', imei):
    #quyda: imeini raqamligini tekshirib va uni uzunligini tekshirmoqda
    if imei.isdigit() and len(imei) == 15:
        await state.update_data(imei=imei)
        await Nmemb_state.next()
        await message.answer(text=f"💵Telefon narxini kiriting!")
    else:
        await message.answer(text=f"🆘Telefon IMEIsi kiritilishda xatolik bo'ldi!🆘\n\nIMEI raqami 15 tadan iborat bo'lishi"
                                  f" kerak. Iltimos tekshirib qaytadan urunb ko'ring")
    # except ValueError:
    #     await message.answer(text=f"Telefon IMEIsi kiritilishda xatolik bo'ldi!\n\nIMEI raqami 15 tadan iborat bo'lishi"
    #                               f" kerak. Iltimos tekshirib qaytadan urunb ko'ring")

@dp.message_handler(state=Nmemb_state.Add_Tprice)
async def sum_item(message: types.Message, state: FSMContext):
    summa = message.text
    try:
        int_summa = int(summa)
        # Ma'lumotlarni olish
        await state.update_data(summa=summa)
        await Nmemb_state.next()
        await message.answer(text=f"Asl summa muvafaqiyatli qabul qilindi!\n\nEndi summa turini tanglang", reply_markup=type_price)
    except ValueError:
        await message.answer(text="🆘Summani kiritishda xatolik bor!🆘\n\nQaytadan urinib koring", reply_markup=cancel_button)

@dp.callback_query_handler(text='dollar', state=Nmemb_state.Add_Twoprice)
async def dollar_price(request: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    summ = user_data.get('summa')
    dollars_p = summ
    await state.update_data(icon=' $')
    await state.update_data(dollar=dollars_p)
    await Nmemb_state.next()
    await request.message.answer(text=f"Summa turi qabul qilindi!\n\nEndi esa kelishuv ustamasini kiriting,"
                                      f" yani kredit uchun qo'shiladigan ustama foizi.\n\nNamuna (5, 10, 15, 20, ....)")


@dp.callback_query_handler(text='som', state=Nmemb_state.Add_Twoprice)
async def dollar_price(request: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    summ = user_data.get('summa')
    dollars_p = summ
    await state.update_data(icon=' So\'m')
    await state.update_data(dollar=dollars_p)
    await Nmemb_state.next()
    await request.message.answer(text=f"Summa turi qabul qilindi!\n\nEndi esa kelishuv ustamasini kiriting,"
                                      f" yani kredit uchun qo'shiladigan ustama foizi.\n\nNamuna (5, 10, 15, 20, ....)")

@dp.message_handler(state=Nmemb_state.Add_Percent)
async def length(message: types.Message, state: FSMContext):
    per = message.text
    await state.update_data(percent=int(per))
    user_date = await state.get_data()
    suma = user_date.get('dollar')
    perp = (int(suma)/100)*int(per)
    perprice = int(suma)+int(perp)
    await Nmemb_state.next()
    await state.update_data(perprice=perprice)
    await message.answer(text=f"Summa ustamasi qabul qilindi!\n\nEndi esa kelishuv muddatini kiriting,"
                              f" yani kredit necha oy uchun.\n\nNamuna (3, 6, 12, 24, ....)")

@dp.message_handler(state=Nmemb_state.Add_Length)
async def length(message: types.Message, state: FSMContext):
    leng = message.text
    await state.update_data(month=int(leng))
    user_date = await state.get_data()
    suma = user_date.get('perprice')
    permonth = int(suma)/int(leng)
    await state.update_data(permonth=permonth)
    name = user_date.get('name')
    tel = user_date.get('tel')
    tname = user_date.get('tname')
    timei = user_date.get('imei')
    summ = user_date.get('summa')
    icon = user_date.get('icon')
    length = user_date.get('month')
    yillik = str(suma)
    oyiga = int(permonth)
    status = "To'langan"
    start_t = datetime.datetime.now().date()
    await state.finish()
    await message.answer(f"```js \n👤Yangi foydalanuvchi: {name}\n\n📞Telefon raqami: {tel}\n\n📱Maxsulot nomi: {tname}\n\n"
                         f"🆔Telefon IMEI raqami: {timei}\n\n💵Maxsulot asl narxi: {summ} {icon}\n\n💰Maxsulotning {str(leng)} oylik"
                         f" kredit narxi: {yillik} {icon}\n\n💵Oylik to'lovi: {oyiga} {icon} ``` ", parse_mode="MARKDOWN")
    # await message.answer(f'{", ".join(str(item) for item in bir)}, {", ".join(str(item) for item in iki)}, {", ".join(str(item) for item in uch)}')
    await message.answer(text=f'Yangi mijoz muvafaqiyatli royxatga qo\'shildi✅', reply_markup=home_button)
    await db.add_client_db(str(name), str(tel), str(tname), str(timei), str(summ + icon), str(yillik + icon), str(str(oyiga) + icon), str(start_t), int(length), total_len=0, total_pay=0)
    await db.add_status_db(status, str(name))
    def add_months(some_datetime, months):
        month = some_datetime.month - 1 + months
        year = some_datetime.year + month // 12
        month = month % 12 + 1
        day = min(some_datetime.day, [31, 29 if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else 28,
                                      31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
        return datetime.datetime(year, month, day)
    sikl = 1
    while length >= sikl:
        next_dates = add_months(datetime.datetime.strptime(str(start_t), "%Y-%m-%d"), sikl)
        # print(next_dates.date())
        sikl += 1
        await db.add_payment_dur(str(name), str(next_dates.date()))
        # await db.add_payment_dur2(str(next_dates.date()))
    # print(length)
    try:
        numb = format_phone_number(str(tel))
        summa = f"{oyiga}{icon}"
        text = f"Xurmatli Mijoz tabriklaymiz {tname} qurulmasini {leng} oyga bo'lib to'lashka xarid qildingiz oylik to'lo'vi {summa}! Bizni tanlaganingizdan xursandmiz"
        await send_sms(numb, text)
        cur.execute("UPDATE accounts SET total_sms = total_sms + 1 WHERE tg_id == ?", (964031372, ))
        db1.commit()
    except Exception as ex:
        print(ex)

@dp.callback_query_handler(text='cancel', state=Nmemb_state.Add_Uname)
async def cancel(request: CallbackQuery, state: FSMContext):
    await request.message.answer(text=f"Assalom alaykum! Nima xizmat?", reply_markup=main_button)
    await state.finish()
@dp.callback_query_handler(text='cancel', state=Nmemb_state.Add_Unumb)
async def cancel(request: CallbackQuery, state: FSMContext):
    await request.message.answer(text=f"Assalom alaykum! Nima xizmat?", reply_markup=main_button)
    await state.finish()

# @dp.callback_query_handler(text='home')
# async def cancel(request: types.CallbackQuery):
#     await request.message.answer(text=f"Assalom alaykum! Nima xizmat?",reply_markup=main_button)
    # await Nmemb_state.set()