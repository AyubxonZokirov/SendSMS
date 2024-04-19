from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='👤Yangi mijoz', callback_data='yangi_mijoz'),
            InlineKeyboardButton(text='🔎Mijozlarni tekshirish', callback_data='mijoz_tekshir')
        ],
        [
            InlineKeyboardButton(text='📈Hisobot', callback_data='hisobot')
        ],
        [
            InlineKeyboardButton(text='📋Mijozlar Ro\'yxati', callback_data='mijoz_royxat')
        ],
        [
            InlineKeyboardButton(text='📊Oy bo\'yicha hisobot', callback_data='oylik_hisobot')
        ]
    ]
)  #Vergul qoysang qolin sinsn
cancel_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Bekor qilish❌', callback_data='cancel')
        ]
    ]
)
type_price = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Dollar💲', callback_data='dollar'),
            InlineKeyboardButton(text="So'm💶", callback_data='som')
        ]
    ]
)
home_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔙 Bosh Menuga qaytish', callback_data='home')
        ]
    ]
)
monthly_request = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Xa✅', callback_data='albatta')
        ]
    ]
)
# type_price_forrep = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Dollar💲', callback_data='dollar2'),
#             InlineKeyboardButton(text="So'm💶", callback_data='som2')
#         ]
#     ]
# )