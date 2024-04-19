import asyncio
from aiogram import executor
from utils.db_api import database as db
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.monthly_check import scheduler_jobs, scheduler
# from handlers.users.test import scheduler_jobs, scheduler


async def on_startup(dispatcher):
    # Bazani yurgizish
    await db.db_start()
    print('Bot successfully started!')

    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)
    await scheduler_jobs()

if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
