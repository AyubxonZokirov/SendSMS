import sqlite3 as sq
import os
# os.chdir('SendSMS/date/')

db = sq.connect('sendSMS.db')
cur = db.cursor()

#new
async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER, "
                "cart_id TEXT)")
    #Bu kod "accounts" jadvaliga yangi bir ustun qo'shadi, bu ustun "tg_id" deb ataladi va uning turu INTEGER bo'ladi.
    # Ustun qo'shishning bu usuli mavjud ustunlarga yangi ma'lumotlarni qo'shish uchun juda qulay. Agar yana savollar
    # bo'lsa, menga yozing!
    # cur.execute("ALTER TABLE accounts ADD COLUMN sendSMS_id INTEGER")
    # cur.execute("ALTER TABLE accounts ADD COLUMN added_users_id INTEGER")
    # cur.execute("ALTER TABLE accounts ADD COLUMN added_users_name TEXT")
    # cur.execute("ALTER TABLE accounts ADD COLUMN total_sms INTEGER")

    cur.execute("CREATE TABLE IF NOT EXISTS clients("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name TEXT, "
                "tel TEXT, "
                "brand TEXT, "
                "imei TEXT, "
                "first_price TEXT, "
                "price TEXT, "
                "permonth_price TEXT, "
                "payment TEXT, "
                "total_payment TEXT)")

    cur.execute("CREATE TABLE IF NOT EXISTS payments_duration("
                "i_id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name TEXT, "
                "duration TEXT)")

    # cur.execute("ALTER TABLE clients ADD COLUMN status TEXT")
    # cur.execute("ALTER TABLE clients ADD COLUMN current_status TEXT")
    # cur.execute("ALTER TABLE clients ADD COLUMN overall_status TEXT")
    # cur.execute("ALTER TABLE clients ADD COLUMN start_time INTEGER")
    # cur.execute("ALTER TABLE clients ADD COLUMN length INTEGER")
    # cur.execute("ALTER TABLE clients ADD COLUMN next_payments INTEGER")
    # cur.execute("ALTER TABLE clients ADD COLUMN total_length INTEGER")

    # cur.execute("ALTER TABLE clients DROP COLUMN status")
    # cur.execute("ALTER TABLE clients DROP COLUMN next_payments")
    # cur.execute("ALTER TABLE accounts DROP COLUMN added_users_name")

    db.commit()

async def cmd_start_db(chat_id):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=chat_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=chat_id))
        db.commit()

async def add_user_db(chat_id):
    user = cur.execute("SELECT * FROM accounts WHERE added_users_id == {key}".format(key=chat_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (added_users_id) VALUES ({key})".format(key=chat_id))
        db.commit()

async def del_user_db(chat_id):
    cur.execute("DELETE FROM accounts WHERE added_users_id == ?", (chat_id,))
    db.commit()

async def add_client_db(name, tel, brand, imei, f_price, price, per_price, start_t, length, total_len, total_pay):
    name_check = cur.execute("SELECT * FROM clients WHERE name == ?", (name,)).fetchone()  #.format(key=name)).fetchone() eski uslub
    if not name_check:
        try:
            cur.execute("INSERT INTO clients (name, tel, brand, imei, first_price, price, permonth_price, start, length, total_length, total_payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (name, tel, brand, imei, f_price, price, per_price, start_t, length, total_len, total_pay))
        except sq.Error as err:
            print('Error occurred:', err)
        finally:
            db.commit()

async def add_payment_dur(name, date):
    try:
        cur.execute(
            "INSERT INTO payments_duration (name, duration) VALUES (?, ?)",
            (name, date))
    except sq.Error as err:
        print('Error occurred:', err)
    finally:
        db.commit()

async def add_status_db(monthly_status, whose):
    try:
        cur.execute("UPDATE clients SET current_status = ? WHERE name = ?",
                    (monthly_status, whose))
    except sq.Error as err:
        print('Error occurred:', err)
    finally:
        db.commit()

async def select_clients(time):
    try:
        user = cur.execute("SELECT name FROM payments_duration WHERE duration = ?",
                    (time, )).fetchall()
        return user
    except sq.Error as err:
        print('Error occurred:', err)
    finally:
        db.commit()


users = cur.execute("SELECT name FROM clients").fetchall()
db.commit()
# for user in users:
#     print(f'ed','\n'.join(user))

async def users_details_db(user_name):
    cur.execute("SELECT tel, brand, price, permonth_price, total_payment, current_status FROM clients WHERE name = ?",
                (user_name,))
    user_info = cur.fetchone()
    # print("1", user_info)
    return user_info
db.commit()

# async def get_credit_db()

# credit_price = cur.execute("SELECT first_price FROM clients WHERE first_price LIKE '%$%'").fetchall()
# credit_with_per = cur.execute("SELECT price FROM clients WHERE price LIKE '%$%'").fetchall()
# credit_price2 = cur.execute("""SELECT first_price FROM clients WHERE first_price LIKE "%So'm%" """).fetchall()
# credit_with_per2 = cur.execute("""SELECT price FROM clients WHERE price LIKE "%So'm%" """).fetchall()
# cr_pr = [(cr_pr[0]) for cr_pr in credit_price]
# cr_pr_per = [(cr_prr[0]) for cr_prr in credit_with_per]
# cr_pr2 = [(cr_prrr[0]) for cr_prrr in credit_price2]
# cr_pr_per2 = [(cr_prrrr[0]) for cr_prrrr in credit_with_per2]
# print(credit_price)
# print(cr_pr_per)

# register_time = cur.execute("SELECT start, name FROM clients").fetchall()
# print(register_time)