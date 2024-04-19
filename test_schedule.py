# async def check_student():
#     today = datetime.today().strftime("%Y-%m-%d")
#     students = base.select_students_via_deadline(deadline=today)
#     for student in students:
#         chanel_id = student[1]
#         user_id = student[2]
#         chanel = base.select_course(id=chanel_id)
#         user = base.select_user(id=user_id)
#         tg_chanel_id = chanel[5]
#         user_tg_id = user[3]
#         check = await tekshirish1(user_id=user_tg_id, kanal_link=tg_chanel_id)
#         if check:
#             await bot.kick_chat_member(chat_id=tg_chanel_id, user_id=user_tg_id)
#
#
# async def check_student_three_day():
#     today = datetime.today().strftime("%Y-%m-%d")
#     three_day = datetime.strptime(str(today), '%Y-%m-%d').date() + relativedelta(days=3)
#     students = base.select_students_via_deadline(deadline=three_day)
#     for student in students:
#         chanel_id = student[1]
#         user_id = student[2]
#         chanel = base.select_course(id=chanel_id)
#         user = base.select_user(id=user_id)
#         tg_chanel_id = chanel[5]
#         user_tg_id = user[3]
#         check = await tekshirish1(user_id=user_tg_id, kanal_link=tg_chanel_id)
#         if check:
#             await bot.send_message(chat_id=user_tg_id, text=f" {chanel[1]} kursi uchun to'lov qilishni unutmang!!")
#
#
# async def scheduler_jobs():
#     try:
#         scheduler.add_job(check_student, 'interval', seconds=86400)
#         scheduler.add_job(check_student_three_day, 'interval', seconds=86400)
#         pass
#     except Exception as x:
#         print(x)
#         with open("text.txt", 'a') as file:
#             file.write(f"{x}   xatolik  \n")