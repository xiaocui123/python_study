from PIL import  Image

if __name__ == '__main__':
    im=Image.open('g:/desktop.jpg')
    w,h=im.size
    print('原始图片大小“%s*%s' %(w,h))

    im.thumbnail((w//3,h//3))
    im.save('thumbnail.jpg','jpeg')
