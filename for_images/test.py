import schedule
from datetime import datetime, timedelta
import datetime


date = datetime.datetime.today()
date2 = datetime.datetime.today().date()
date3 = datetime.datetime.now()
date4 = datetime.datetime.now().date()

print(f'{date}\n{date2}\n{date3}\n{date4}\n')

# Quydagi kod bir sanani kelasi oylarini olshka yordam beradi
# def add_months(some_datetime, months):
#     month = some_datetime.month - 1 + months
#     year = some_datetime.year + month // 12
#     month = month % 12 + 1
#     day = min(some_datetime.day, [31,
#                                   29 if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else 28,
#                                   31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
#     return datetime.datetime(year, month, day)

# sana = '2024-08-30'
# oy = 7
# sikl = 1
# while oy >= sikl:
#             next_date = add_months(datetime.datetime.strptime(sana, "%Y-%m-%d"), sikl)
#             print(next_date.strftime("%Y-%m-%d"))
#             sikl += 1

# for date in dates:
#     for oy in duration:
#         sikl = 1
#         print(oy)
#         while int(oy) >= sikl:
#             next_date = add_months(datetime.datetime.strptime(date, "%Y-%m-%d"), sikl)
#             print(next_date.strftime("%Y-%m-%d"))
#             sikl += 1


        # print("\n")  # Yangi sana to'g'risida ma'lumotlar ketishini ajrating
        # # 1 marta qo'shilgan ma'lumotlarni o'chirish
        # if duration.index(oy) == 0:
        #     del dates[0]
        #     del duration[0]


# sana = '2024-04-06'
# oy = 6
# sikl = 1
# while oy >= sikl:
#     # next = datetime.datetime.strptime(sana, "%Y-%m-%d") + datetime.timedelta(days=30 * sikl)
#     next = datetime.datetime.strptime(sana, "%Y-%m-%d") + datetime.timedelta(months=sikl)

#     print(next.strftime("%Y-%m-%d"))
#     sikl += 1




# def aniqlash(bir_sana, kelsa_san):
#     # kelsa_sanani hisoblash
#     kelsa_san = bir_sana + timedelta(days=kelsa_san*30)
#     return kelsa_san
#
# # Test uchun
# bugun = datetime.now().date()
# bir_sana = datetime(2024, 4, 6).date()  # Maqsad sana
# kelsa_san = 5  # Necha oyligi kelsa
#
# kelsa_san = aniqlash(bir_sana, kelsa_san)
# print("Kelgan san:", kelsa_san)


# # Foydalanuvchidan ismini so'raymiz
# user_name = input("Ismingizni kiriting: ")
#
# # Joriy sana va vaqt
# current_datetime = datetime.datetime.now()
# toda = datetime.datetime.today()
# #
# # Boshlang'ich sana
# start_date = current_datetime.date()
#
# print(current_datetime, start_date, toda)
#
# # Siz o'zingiz tugash sanangizni tanlaysiz
# # Masalan, 30 kun qo'ymoqchi bo'lsangiz
# end_date = start_date + datetime.timedelta(seconds=5)
#
# # Natijani chiqaramiz
# print(f"Assalomu alaykum, {user_name}!")
# print(f"Sizning xar oy ismingiz: {end_date.strftime('%B')}")
# print(f"Sizning tugash sanangiz: {end_date}")

# until = [5]
# cycle = 1
# while cycle<=until[0]:
#     print(f"bu {cycle}chi xabar")
#     cycle += 1

# day = 4
# day2 = 5
# now = datetime.datetime.now()
# delta = now - datetime.timedelta(days=1)
# today = now.day
# delta_day = delta.day
# hour = now.hour
#
# if day2 == today:
#     print(f"Today {today}-April")
# if day == delta_day:
#     print(f"Today {delta_day}-April")

# now = datetime.datetime.now()
# current_time = now.time()
#
# schedule.every(10).seconds.do(print('10 sek'))
# schedule.run_pending()
