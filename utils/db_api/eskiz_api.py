import requests
import asyncio
from loader import bot
# import aiohttp

#sms jo'natish
from pprint import pprint
# from eskiz.client import SMSClient
#
#
# client = SMSClient(
#     api_url="https://notify.eskiz.uz/api/",
#     email="ayubxonzokirov.2005@gmail.com",
#     password="HKe9o6HYSCfz6sTsulXohyTayo3Vg8ukLOhnsugm",
# )
#
# async def send_sms(phone_number: str, message: str):
#     resp = client._send_sms(phone_number=phone_number, message=message)
#     print(phone_number)
#     print(message)
#     pprint(resp)
#     return resp

# org versia
# resp = client._send_sms(
#     phone_number="998911100418",
#     message="Это тест от Eskiz"
# )
# pprint(resp)

# + belgisini olb tashlash uchun funksya
def format_phone_number(phone_number):
    # Barcha belgilarni o'chirib tashlash
    phone_number = phone_number[1:]
    return phone_number

# Misol: +998909009090 raqamini + belgisiz ko'rsatish
# phone_number = "+998909009090"
# formatted_phone_number = format_phone_number(phone_number)
# print(formatted_phone_number)

#sms jo'natish
async def send_sms(phone_number: str, message: str):
    url = "https://notify.eskiz.uz/api/message/sms/send"

    payload = {'mobile_phone': phone_number,
               'message': message,
               'from': '4546',
               'callback_url': None}
    files = [

    ]
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTYwNzg0NTQsImlhdCI6MTcxMzQ4NjQ1NCwicm9sZSI6InVzZXIiLCJzaWduIjoiOTM3YzQ2NmUzZTdhODM1NWI5ZWUyODJjNDAwN2JlOTEwYmNhODNjZDU0NGM3ZGY3ZTE4YzliYWY5ZjhmNGNjZiIsInN1YiI6IjEwMTgifQ.SmY0F_nrB_nlCaRdQrmRhS0YeqUgt7qYV-5Aoc0Whys'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    pprint(response.text)
    return response
