from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.main_buttons import main_button
from aiogram import types
from loader import dp
from utils.db_api import database as db
import sqlite3 as sq

db1 = sq.connect("sendSMS.db")
cur = db1.cursor()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.chat.id
    try:
        addeds = cur.execute("SELECT added_users_id FROM accounts").fetchall()
        addedss = [add[0] for add in addeds]
        # print(addedss)
        for added in addedss:
            if chat_id == added:
                await db.cmd_start_db(message.from_user.id)
                await message.answer(text=f"Assalom alaykum, {message.from_user.full_name}! Nima xizmat?", reply_markup=main_button)
                break
        else:
            await message.answer("Afsuski sizda botdan foydalanish xuquqi yo'q. Botdan foydalanish uchun adminga murojat qiling!\n\nAdmin: @Ayubxon_Zokirov")
    except Exception as ex:
        print(ex)
        await message.answer('Xatolik yuz berdi. Iltimos, keyinroq urinib ko\'ring.')

