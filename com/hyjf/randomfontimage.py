from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random

def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

if __name__ == '__main__':
    width=60*4
    height=60
    image=Image.new('RGB',(width,height),(255,255,255))

    # 创建Font对象:
    font=ImageFont.truetype('c://Windows//Fonts//Arial.ttf',36)

    #创建Draw对象
    draw=ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColor())

    for t in range(width):
        draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

    image=image.filter(ImageFilter.BLUR)
    image.save('code.jpg','jpeg')
