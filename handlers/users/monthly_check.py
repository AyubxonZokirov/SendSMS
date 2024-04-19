import datetime
import re
from aiogram import types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from data.config import ADMINS
from loader import dp, bot
import sqlite3 as sq
from utils.db_api import database as db
from utils.db_api.eskiz_api import send_sms, format_phone_number

db1 = sq.connect('sendSMS.db')
cur = db1.cursor()
scheduler = AsyncIOScheduler()
async def check_clients_yesterday():
    today = datetime.datetime.today().date().strftime("%Y-%m-%d")
    before_today = datetime.datetime.strptime(str(today), "%Y-%m-%d") - datetime.timedelta(days=1)
    # print(before_today)
    users = await db.select_clients(time=before_today.date())
    # print(users)
    for user in users:
        # print(user[0])
        u = cur.execute("SELECT tel FROM clients WHERE name == ?", (user[0],)).fetchall()
        addeds = cur.execute("SELECT added_users_id FROM accounts").fetchall()
        admins = [add[0] for add in addeds if add[0] is not None]
        print(admins)
        tel = [t[0] for t in u]
        for admin in admins:
            print(admin)
            await bot.send_message(chat_id=admin, text=f"Eslatib o'tamiz!!!\n\nErtaga {user[0]}ning to'lov kuni\nTel: {tel[0]}")
            try:
                usser = cur.execute("SELECT permonth_price FROM clients WHERE name == ?", (user[0],))
                usr = [us[0] for us in usser]
                numb = format_phone_number(str(tel[0]))
                text = f"Assalomu Alekum, Xurmatli mijoz eslatib o'tamiz ertaga sizning telefoningizni to'lo'v kuni, agar to'lo'v amalga oshirilmasa telefoningiz bloklanishi mumkn! To'lov Summasi: {usr[0]}"
                await send_sms(numb, text)
                cur.execute("UPDATE accounts SET total_sms = total_sms + 1")
                db1.commit()
            except Exception as ex:
                print(ex)
async def check_clients_today():
    today = datetime.datetime.today().date().strftime("%Y-%m-%d")
    users = await db.select_clients(time=today)
    # print(users)
    for user in users:
        # print(user[0])
        u = cur.execute("SELECT tel FROM clients WHERE name == ?", (user[0],)).fetchall()
        len = cur.execute("SELECT length FROM clients WHERE name == ?", (user[0],)).fetchall()
        tot_len = cur.execute("SELECT total_length FROM clients WHERE name == ?", (user[0],)).fetchall()
        addeds = cur.execute("SELECT added_users_id FROM accounts").fetchall()
        admins = [add[0] for add in addeds if add[0] is not None]
        tel = [t[0] for t in u]
        length = [l[0] for l in len]
        total_len = [tl[0] for tl in tot_len]
        # print(length[0])
        # print(total_len[0])
        if not length[0] == total_len[0]:
            for admin in admins:
                cur.execute("UPDATE clients SET total_length = total_length + 1 WHERE name = ?",
                            (user[0],))
                db1.commit()
                await bot.send_message(chat_id=admin, text=f"Eslatib o'tamiz!!!\n\nBugun {user[0]}ning to'lov kuni\nTel:{tel[0]}")
                await bot.send_message(admin, text=f"{user[0]} ni to\'lo\'vi qabul qilingan bo\'lsa\n\n"
                                                   f"`/tolandi {user[0]}` komandasini yuboring!", parse_mode="MARKDOWN",)
                try:
                    usser = cur.execute("SELECT permonth_price FROM clients WHERE name == ?", (user[0],))
                    usr = [us[0] for us in usser]
                    numb = format_phone_number(str(tel[0]))
                    text = f"Assalomu Alekum, Xurmatli mijoz eslatib o'tamiz bugun sizning telefoningizni to'lo'v kuni, agar to'lo'v amalga oshirilmasa telefoningiz bloklanishi mumkn! To'lov Summasi: {usr[0]}"
                    await send_sms(numb, text)
                    cur.execute("UPDATE accounts SET total_sms = total_sms + 1")
                    db1.commit()
                except Exception as ex:
                    print(ex)
                try:
                    cur.execute("UPDATE clients SET current_status = ? WHERE name = ?",
                                (f"To'lo'v qilinmagan", user[0]))
                    cur.execute("UPDATE clients SET payment = '0' WHERE name == ?", (user[0],))
                except sq.Error as err:
                    print('Error occurred:', err)
                finally:
                    db1.commit()
        else:
            cur.execute("UPDATE clients SET overall_status = 'Qarz uzildi' WHERE name == ?", (user[0], ))
            pass

async def scheduler_jobs():
    trigger = CronTrigger(hour=8, minute=0)
    trigger2 = CronTrigger(hour=8, minute=30)
    try:
        scheduler.add_job(check_clients_yesterday, trigger=trigger)  # 'interval' trigger=10
        scheduler.add_job(check_clients_today, trigger=trigger2)  # 'interval' trigger=10
        pass
    except Exception as ex:
        print(ex)
        with open('text.txt', 'a') as file:
            file.write(f"{ex} xatolik \n")

@dp.message_handler(commands=['tolandi'])
async def monthly_payment(message: types.Message):
    chatid = message.chat.id
    user_name = message.get_args()
    # print(user_name)
    if user_name:
        try:
            cur.execute("UPDATE clients SET current_status = ? WHERE name = ?",
                        (f"To'landi", user_name))
        except sq.Error as err:
            print('Error occurred:', err)
        finally:
            db1.commit()
            # print(f"{user_name}ni qazlari qolmadi")
    else:
        await bot.send_message(chat_id=chatid, text="/tolandi komandasidan song isim kiriting\n\nMisol: (/tolandi Baxrom)")
    try:
        per_pr = cur.execute("SELECT permonth_price FROM clients WHERE name == ?", (user_name,)).fetchall()
        tot_pay = cur.execute("SELECT total_payment FROM clients WHERE name == ?", (user_name,)).fetchall()
        per_price = [pp[0] for pp in per_pr]
        total_pay = [tp[0] for tp in tot_pay]
        # raqamdan tashqari belgilarni ajratb olish ($, So'm)
        icon = re.findall(r' [^\d]+', per_price[0])[0]
        # print(icon)
        per_price2 = re.findall(r'\d+', per_price[0])
        total_pay2 = re.findall(r'\d+', total_pay[0])
        total = f"{int(total_pay2[0])+int(per_price2[0])}{icon}"
        # print(f"{per_price}\n{total_pay}\n{per_price2}\n{total_pay2}")
        # print(per_price[0])
        cur.execute(f"UPDATE clients SET payment = ? WHERE name == ?", (str(per_price[0]), user_name))
        cur.execute(f"UPDATE clients SET total_payment = ? WHERE name == ?", (total, user_name, ))
        await bot.send_message(chat_id=chatid, text=f"{user_name}ning to'lovi muvafaqiyatli qabul qilindi✅")
        db1.commit()
    except Exception as ex:
        await bot.send_message(chat_id=chatid, text=f"Bunday mijoz tolimadi!")
        print(ex)


