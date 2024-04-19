from PIL import Image, ImageDraw, ImageFont, ImageFilter
from handlers.users.new_memb import bir, iki, uch

org = Image.open('Hisobot.png')
img = org.filter(ImageFilter.DETAIL)

font = ImageFont.truetype(font='arial.ttf', size=72)
draw = ImageDraw.Draw(img)

a = ['asd', 'sda', 'dsa']
b = [4,4,4]
c = [3, 3, 3]

all1 = 0
for o in bir:
    all1 += o

total1 = sum(map(int, b)) #listdagilarni qoshb umumi summani beryabti
total2 = sum(map(int, c))

als = str(all1)
alstr = str(total1)
allstr = str(total2)
draw.text(xy=(1050, 175), text=als, font=font, fill='white')
draw.text(xy=(1050, 315), text=alstr, font=font, fill='white')
draw.text(xy=(1050, 455), text=allstr, font=font, fill='white')
# draw.text(xy=(1050, 590), text=summa4, font=font, fill='white')
# draw.text(xy=(1050, 730), text=summa5, font=font, fill='white')

img.save('Report.png')
img.show()
# sum1 = all1
# two = (for t in iki)
# three = (for th in uch)


