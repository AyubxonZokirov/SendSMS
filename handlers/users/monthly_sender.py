# import asyncio
# from aiogram import types
# import sqlite3 as sq
# from keyboards.inline.main_buttons import monthly_request
# from data.config import ADMINS
# from loader import dp, bot
# import datetime
#
# db = sq.connect('sendSMS.db')
# cur = db.cursor()
#
#
# async def monthly_send():
#     now = datetime.datetime.now()
#     today = now.day
#     hour = datetime.datetime.now().hour
#     register_time = cur.execute("SELECT start, name, length FROM clients").fetchall()
#     for reg_time in register_time:
#         duration = 1
#         dd = datetime.datetime.strptime(str(reg_time[0]), "%Y-%m-%d")
#         day = dd.day
#         message_sent_count = 0
#         while duration <= reg_time[2] and message_sent_count < 1:
#             if today == day and hour == 8 and now.minute == 11:
#                 for admin in ADMINS:
#                     await bot.send_message(admin, text=f'ESLATMA❗️❗️❗️\n\nBugun {reg_time[1]}ning to\'lov kuni',)
#                     await bot.send_message(admin, text=f"{reg_time[1]} ni to\'lo\'vi qabul qilingan bo\'lsa\n\n"
#                                                        f"`/tolandi {reg_time[1]}` komandasini yuboring!", parse_mode="MARKDOWN",
#                                            reply_markup=monthly_request)
#                     try:
#                         cur.execute("UPDATE clients SET current_status = ? WHERE name = ?",
#                                     (f"to'lo'v qilinmagan", reg_time[1]))
#                     except sq.Error as err:
#                         print('Error occurred:', err)
#                     finally:
#                         db.commit()
#                 # await monthly_request_handler(reg_time[1])
#                 if duration == reg_time[2]:
#                     cur.execute("UPDATE clients SET overall_status = ? WHERE name = ?",
#                                 (f"Qarz uzildi", reg_time[1]))
#                     db.commit()
#
#                 # @dp.message_handler(commands=['tolandi'])
#                 # async def monthly_payment(message: types.Message):
#                 #     user_name = message.get_args()
#                 #     print(user_name)
#                 #     if user_name:
#                 #         try:
#                 #             db2 = sq.connect('sendSMS.db')
#                 #             cur2 = db2.cursor()
#                 #             cur.execute("UPDATE clients SET current_status = ? WHERE name = ?",
#                 #                         (f"to'landi", user_name))
#                 #         except sq.Error as err:
#                 #             print('Error occurred:', err)
#                 #         finally:
#                 #             db.commit()
#                 #             # db.commit()
#                 #             print(f"{user_name}ni qazlari qolmadi")
#
#             message_sent_count += 1
#             duration += 1
#             await asyncio.sleep(1)
#
#         # if duration == reg_time[2]:
#         #     cur.execute("INSERT INTO clients (overall) VALUES (payed)")
#
#         if today > day or today < day:
#             pass
#
#
# @dp.message_handler(commands=['tolandi'])
# async def monthly_payment(message: types.Message):
#     user_name = message.get_args()
#     print(user_name)
#     if user_name:
#         try:
#             db2 = sq.connect('sendSMS.db')
#             cur2 = db2.cursor()
#             cur.execute("UPDATE clients SET current_status = ? WHERE name = ?",
#                         (f"to'landi", user_name))
#             # db2.commit()
#         except sq.Error as err:
#             print('Error occurred:', err)
#         finally:
#             db.commit()
#         # db.commit()
#             print(f"{user_name}ni qazlari qolmadi")
#
# asyncio.run(monthly_send())
#
# # register_time = cur.execute("SELECT start, name, length FROM clients").fetchall()
# # register_tim = [reg_time[0] for reg_time in register_time]
# # names = [name[1] for name in register_time]
#
# # for d_n in register_time:
# #     dd = datetime.datetime.strptime(str(d_n[0]), "%Y-%m-%d")
# #     day = dd.day
# #     print(day, d_n[0], d_n[1])
# # for i in names:
# #     cycle = cur.execute("SELECT length FROM clients WHERE name = ?", (i, )).fetchall()
# #     for c in cycle:
# #         print(c[0])