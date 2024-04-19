from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, bot


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    text2 = ("Admin Buyuruqlari: ",
             "/add_user (id) - Botdan foydalanish imkonini berish",
             "/delete_user (id) - Botdan foydalanish imkoni berlgan foydalanuvchini o'chirish",
             "/get_users - Foydalanuvchilar ro'yxati",
             "/get_db - Bazani tashlab beradi",
             "/get_total_sms - Barcha jo'natilgan smslar ro'yxati")
    await bot.send_message(chat_id=964031372, text="\n".join(text2))
    await message.answer("\n".join(text))
