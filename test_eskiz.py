# import requests
#
# #token olish
#
# url = "http://notify.eskiz.uz/api/auth/login"
#
# payload={'email': 'ayubxonzokirov.2005@gmail.com',
#          'password': 'HKe9o6HYSCfz6sTsulXohyTayo3Vg8ukLOhnsugm'}
# files=[
#
# ]
# headers = {}
#
# response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
# print(response.text)

#sms jo'natish
# url = "https://notify.eskiz.uz/api/message/sms/send"
#
# payload = {'mobile_phone': '998911100418',
#            'message': 'Это тест от Eskiz',
#            'from': '4546',
#            'callback_url': None}
# files = [
#
# ]
# headers = {
#     'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU2NDI1MjYsImlhdCI6MTcxMzA1MDUyNiwicm9sZSI6InRlc3QiLCJzaWduIjoiZTUyNGZlYTYyYmRiMzlhZTJhMTNlYzEyZTAxOGJkZDY3NDk5NTMzNGUxNTNmMTUwNzMwOTZlY2Y0NmI5NTZlNCIsInN1YiI6IjcwMTQifQ.jkGkcS_05rcdeSUTkW90l5iGNKJJX0MLklIU_t5iVTo'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
# print(response.text)

#body
# {
#   "id": "59bf10a2-aba8-4694-8fd5-0be20102a580",
#   "message": "Waiting for SMS provider",
#   "status": "waiting"
# }


"""jonatishka mani testim (omadsz)"""
# async def send_sms(numb: str, message: str) -> dict:
#     url = "https://notify.eskiz.uz/api/message/sms/send"
#     headers = {
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTU2NDI1MjYsImlhdCI6MTcxMzA1MDUyNiwicm9sZSI6InRlc3QiLCJzaWduIjoiZTUyNGZlYTYyYmRiMzlhZTJhMTNlYzEyZTAxOGJkZDY3NDk5NTMzNGUxNTNmMTUwNzMwOTZlY2Y0NmI5NTZlNCIsInN1YiI6IjcwMTQifQ.jkGkcS_05rcdeSUTkW90l5iGNKJJX0MLklIU_t5iVTo'
#     }
#     data: dict = {
#         'method': "POST",
#         'headers': headers,
#         'api_path': "send_message",
#         'data': {
#             'mobile_phone': f'{numb}',
#             'message': f'{message}',
#             'from': '4546',
#             'callback_url': None}}
#     files = [
#
#     ]
#
#     response = requests.request("POST", url, headers=headers, data=data, files=files)
#
#     if response.status_code == 200:
#         await bot.send_message(chat_id=964031372, text='SMS yuborildi!')
#     else:
#         await bot.send_message(chat_id=964031372, text='SMS yuborishda xatolik!!')
#     print(response.text)
    # return response
