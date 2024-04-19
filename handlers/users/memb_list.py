from aiogram import types
from aiogram.utils.callback_data import CallbackData
from loader import dp, bot
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.main_buttons import main_button, cancel_button, home_button
import sqlite3 as sq

db = sq.connect('sendSMS.db')
cur = db.cursor()

# @dp.callback_query_handler(text='mijoz_royxat')
# async def memb_list(request: types.CallbackQuery):
#     memb_info = cur.execute("SELECT name, tel FROM clients").fetchall()
#     memb_data = [(index + 1, name, tel) for index, (name, tel) in enumerate(memb_info)]
#     message_text = "\n".join([f"{index}. {name} - {tel}" for index, name, tel in memb_data])
#     await request.message.answer(text=f"```js {message_text}```", parse_mode="MARKDOWN", reply_markup=home_button)
#     # print(message_text)


@dp.callback_query_handler(text='home')
async def cancel(request: types.CallbackQuery):
    await request.message.answer(text=f"Assalom alaykum! Nima xizmat?", reply_markup=main_button)

TOTAL_MEMBERS_PER_PAGE = 20  # Sahifadagi a'zolar soni

@dp.callback_query_handler(text='mijoz_royxat')
async def memb_list(request: types.CallbackQuery):
    # Sahifani aniqlash
    data = request.data  # Callback ma'lumotini olish
    # Sahifa raqamini aniqlash
    page_number = 1
    for item in data.split('&'):
        if item.startswith('page='):
            page_number = int(item.split('=')[1])
            break

    # Offsetni aniqlash
    offset = (page_number - 1) * TOTAL_MEMBERS_PER_PAGE

    # Ma'lumotlar bazasidan a'zolarni olish
    memb_info = cur.execute("SELECT name, tel FROM clients LIMIT ? OFFSET ?", (TOTAL_MEMBERS_PER_PAGE, offset)).fetchall()

    # Sahifadagi ma'lumotlarni formatlash
    message_text = "\n".join([f"{index}. {name} - {tel}" for index, (name, tel) in enumerate(memb_info, start=offset + 1)])

    # Keyboard tugmalarini yaratish
    keyboard = types.InlineKeyboardMarkup()
    if page_number > 1:
        keyboard.insert(types.InlineKeyboardButton("Orqaga", callback_data=f"mijoz_royxat&page={page_number - 1}"))

        # "Keyingi" tugmasini qo'shish
    if len(memb_info) == TOTAL_MEMBERS_PER_PAGE:
        keyboard.insert(types.InlineKeyboardButton("Keyingi", callback_data=f"mijoz_royxat&page={page_number + 1}"))

    # Xabarni jo'natish
    await request.message.answer(text=f"```js\n{message_text}\n```", parse_mode="MARKDOWN", reply_markup=keyboard)
    await request.answer()

@dp.callback_query_handler(lambda query: query.data.startswith('mijoz_royxat&page='))
async def handle_pagination(callback_query: types.CallbackQuery):
    # Sahifadagi ma'lumotlarni yuklash, sahifa raqamini aniqlash, va qo'shimcha qadamlarni o'tkazish kabi
    # kerakli qadamlarni bajaring
    await memb_list(callback_query)

