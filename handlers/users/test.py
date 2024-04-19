# import datetime
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.cron import CronTrigger
# from dateutil.relativedelta import relativedelta
# from data.config import ADMINS
# from loader import dp, bot
# import sqlite3 as sq
# from utils.db_api import database as db
#
# db1 = sq.connect('sendSMS.db')
# cur = db1.cursor()
# scheduler = AsyncIOScheduler()
# sql1 = """
#         SELECT
#           name
#         FROM
#           payments_duration
#     """
# users1 = cur.execute(sql1).fetchall()
# # for n in users1:
#     # print(n)
# async def check_clients_yesterday():
#     today = datetime.datetime.today().date().strftime("%Y-%m-%d")
#     before_today = datetime.datetime.strptime(str(today), "%Y-%m-%d") - datetime.timedelta(days=1)
#     print(before_today)
#     users = await db.select_clients(time=before_today.date())
#     print(users)
#     for user in users:
#         print(user[0])
#         u = cur.execute("SELECT tel FROM clients WHERE name == ?", (user[0],)).fetchall()
#         tel = [t[0] for t in u]
#         for admin in ADMINS:
#             await bot.send_message(chat_id=admin, text=f"Eslatib o'tamiz!!!\n\nErtaga {user[0]}ning to'lov kuni\nTel: {tel[0]}")
# async def check_clients_today():
#     today = datetime.datetime.today().date().strftime("%Y-%m-%d")
#     users = await db.select_clients(time=today)
#     print(users)
#     for user in users:
#         print(user[0])
#         u = cur.execute("SELECT tel FROM clients WHERE name == ?", (user[0],)).fetchall()
#         tel = [t[0] for t in u]
#         for admin in ADMINS:
#             await bot.send_message(chat_id=admin, text=f"Eslatib o'tamiz!!!\n\nBugun{user}ning to'lov kuni\nTel:{u}")
#
# async def scheduler_jobs():
#     trigger = CronTrigger(hour=8)
#     trigger2 = CronTrigger(hour=9)
#     try:
#         scheduler.add_job(check_clients_yesterday, trigger=trigger)  # 'interval' trigger=10
#         scheduler.add_job(check_clients_today, trigger=trigger2)  # 'interval' trigger=10
#         pass
#     except Exception as ex:
#         print(ex)
#         with open('text.txt', 'a') as file:
#             file.write(f"{ex} xatolik \n")
