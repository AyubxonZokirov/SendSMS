from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

months_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❄️Dekabr", callback_data='dekabr'),
            InlineKeyboardButton(text="❄️Yanvar", callback_data='yanvar'),
            InlineKeyboardButton(text="❄️Fevral", callback_data='fevral')
        ],
        [
            InlineKeyboardButton(text="🌤Mart", callback_data='mart'),
            InlineKeyboardButton(text="️🌤Aprel", callback_data='aprel'),
            InlineKeyboardButton(text="🌤May", callback_data='may')
        ],
        [
            InlineKeyboardButton(text="☀️Iyun", callback_data='iyun'),
            InlineKeyboardButton(text="☀️Iyul", callback_data='iyul'),
            InlineKeyboardButton(text="☀️Avgust", callback_data='avgust')
        ],
        [
            InlineKeyboardButton(text="🌧Sentyabr", callback_data='sentyabr'),
            InlineKeyboardButton(text="🌧Oktyabr", callback_data='oktyabr'),
            InlineKeyboardButton(text="️🌧Noyabr", callback_data='noyabr')
        ]
    ]
)