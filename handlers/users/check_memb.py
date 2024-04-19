from aiogram import types
from utils.db_api.database import users
from loader import dp
from utils.db_api import database as db
import sqlite3 as sq
# from utils.db_api.database import
from aiogram.types import CallbackQuery
from keyboards.inline.main_buttons import main_button, cancel_button, home_button

db2 = sq.connect('sendSMS.db')
cur = db2.cursor()
# @dp.callback_query_handler(text='mijoz_tekshir')
# async def check_member(request: types.CallbackQuery):
#     userss = cur.execute("SELECT name FROM clients").fetchall()
#     all_users = [user[0] for user in userss]
#     formatted_users = [f"`/client {user}`" for user in all_users]
#     all_users_name = "\n".join(formatted_users)
#     await request.message.answer(text=f'Tekshirmoxchi bo\'lgan mijozingizni ismini kiriting!\n\n{all_users_name}', parse_mode="MARKDOWN", reply_markup=home_button)
#     await request.answer()


TOTAL_MEMBERS_PER_PAGE = 20  # Sahifadagi a'zolar soni

@dp.callback_query_handler(text='mijoz_tekshir')
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
    memb_info = cur.execute("SELECT name FROM clients LIMIT ? OFFSET ?", (TOTAL_MEMBERS_PER_PAGE, offset)).fetchall()

    # Sahifadagi ma'lumotlarni formatlash
    message_text = "\n".join([f"{index}. `/clients {name[0]}`" for index, name in enumerate(memb_info, start=offset + 1)])

    # Keyboard tugmalarini yaratish
    keyboard = types.InlineKeyboardMarkup()
    if page_number > 1:
        keyboard.insert(types.InlineKeyboardButton("Orqaga", callback_data=f"mijoz_tekshir&page={page_number - 1}"))

        # "Keyingi" tugmasini qo'shish
    if len(memb_info) == TOTAL_MEMBERS_PER_PAGE:
        keyboard.insert(types.InlineKeyboardButton("Keyingi", callback_data=f"mijoz_tekshir&page={page_number + 1}"))

    # Xabarni jo'natish
    await request.message.answer(text=f"\n{message_text}\n", parse_mode="MARKDOWN", reply_markup=keyboard)
    await request.message.answer(text=f'Tekshirmoxchi bo\'lgan mijozingizni ismini quydagi ko\'rinishda kiriting!\n\nMisol: (/clients Xusan)',
                                 reply_markup=home_button)
    await request.answer()


@dp.callback_query_handler(lambda query: query.data.startswith('mijoz_tekshir&page='))
async def handle_pagination(callback_query: types.CallbackQuery):
    # Sahifadagi ma'lumotlarni yuklash, sahifa raqamini aniqlash, va qo'shimcha qadamlarni o'tkazish kabi
    # kerakli qadamlarni bajaring
    await memb_list(callback_query)


# all_users = [user[0] for user in users]
@dp.message_handler(commands=['clients'])
async def check_user(message: types.Message):
    user_name = message.get_args()
    if user_name:
        # user_name = message.text.split(maxsplit=1)[1]
        userss = cur.execute("SELECT name FROM clients").fetchall()
        all_users = [user[0] for user in userss]
        if user_name in all_users:
            # all_users_name = "\n".join(all_users)
            details = await db.users_details_db(user_name)
            await message.answer(f"```js \n👤Mijoz: {user_name}\n\n📞Tel: {details[0]}\n\n📱Qurilma: {details[1]}\n\n💰Jami to\'lanishi"
                                 f" kerak: {details[2]}\n\n💵Oyiga to\'lanishi kerak: {details[3]}\n\n💲Jami to\'langan:"
                                 f" {details[4]}\n\n📆Bu oy: {details[5]} ``` ", parse_mode="MARKDOWN", reply_markup=home_button)
        else:
            await message.answer(f'Kechirasiz bunday mijoz topilmadi')
    else:
        # elif message.text == '/cancel':
        await message.answer(f'/cancel comandasidan song mijoz ismini kiritishingiz kerak!\n\nMisol: (/cancel Baxrom)')

# @dp.callback_query_handler(text='home')
# async def cancel(request: types.CallbackQuery):
#     await request.message.answer(text=f"Assalom alaykum! Nima xizmat?", reply_markup=main_button)