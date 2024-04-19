import aiofiles
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from utils.db_api.database import add_user_db, del_user_db
import sqlite3 as sq

db = sq.connect("sendSMS.db")
cur = db.cursor()

@dp.message_handler(commands=['add_user'])
async def add_user_id(message: types.Message):
    chat_id = message.chat.id
    user_id = message.get_args()
    print(user_id)
    if user_id and chat_id == 964031372:
        try:
            # cur.execute("INSERT INTO accounts (added_users_id) VALUES (?)", (int(user_id), ))
            await add_user_db(user_id)
            await message.answer(f"({user_id}) id egasiga botdan foydalanishga ruxsat berildi!")
        except Exception as ex:
            print(ex)
    else:
        await message.answer("/add_user komandasi dan so'ng id yuborishingiz kerak")

@dp.message_handler(commands=['delete_user'])
async def delete_user_id(message: types.Message):
    chat_id = message.chat.id
    user_id = message.get_args()
    print(user_id)
    if user_id and chat_id == 964031372:
        try:
            # cur.execute("DELETE FROM accounts WHERE added_users_id = ?", (int(user_id),))
            await del_user_db(user_id)
            await message.answer(f"({user_id}) id egasi muvafaqiyatli foydalanuvchilar royxatidan o'chirildi!")
        except Exception as ex:
            print(ex)
    else:
        await message.answer("/delete_user komandasidan so'ng id yuborishingiz kerak")

@dp.message_handler(commands=['get_users'])
async def get_users(message: types.Message):
    chat_id = message.chat.id
    if chat_id == 964031372:
        usid = cur.execute("SELECT tg_id FROM accounts").fetchall()
        added = cur.execute("SELECT added_users_id FROM accounts").fetchall()
        users_id = [usr[0] for usr in usid]
        addeds = [add[0] for add in added]
        # users = "\n".join(str(user_id) for user_id in users_id if user_id is not None)
        # added_users = "\n".join(str(added) for added in addeds if added is not None)
        user_links = [f'<a href="tg://user?id={user_id}">{user_id}</a>' for user_id in users_id if user_id is not None]
        users_text = "\n".join(user_links)
        addeds_links = [f'<a href="tg://user?id={added}">{added}</a>' for added in addeds if added is not None]
        addeds_text = "\n".join(addeds_links)
        await message.answer(f""" Botdagi jami azolar: \n{users_text} """, parse_mode="HTML")
        await message.answer(f"Botdagi jami foydalanuvchilar: \n{addeds_text}")
    else:
        await message.answer("Bu komanda faqat bot admini tarafidan ishlatiladi")

@dp.message_handler(commands=['get_total_sms'])
async def total_sms(message: types.Message):
    chat_id = message.chat.id
    if chat_id == 964031372:
        smss = cur.execute("SELECT total_sms FROM accounts").fetchall()
        ss = [s[0] for s in smss]
        await message.answer(f"Jami ishlatilgan SMS lar soni: {ss[0]}")
    else:
        await message.answer("Bu komanda faqat bot admini tarafidan ishlatiladi")

@dp.message_handler(commands=['get_db'])
async def get_base(message: types.Message):
    chat_id = message.chat.id
    if chat_id == 964031372:
        try:
            # Ma'lumotlar bazasini ochish
            async with aiofiles.open('sendSMS.db', mode='rb') as db_file:
                # Ma'lumotlar bazasini yuborish
                await message.answer_document(db_file)
        except FileNotFoundError:
            # Agar ma'lumotlar bazasi topilmagan bo'lsa, xabar yuborish
            await message.answer("Ma'lumotlar bazasi topilmadi.")
        except Exception as e:
            # Boshqa xatoliklar uchun xabar yuborish
            await message.answer(f"Xatolik yuz berdi: {e}")