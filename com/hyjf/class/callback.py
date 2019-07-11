class Callback:
    def __init__(self,color):
        self.color=color

    def __call__(self, *args, **kwargs):
        print('turn',self.color)

class Button:
    def __init__(self,command):
        self.command = command

    def press(self):
        self.command()


if __name__ == '__main__':

    cb1=Callback('red')
    cb2=Callback('yellow')

    btn1=Button(cb1)
    btn1.press()
    btn2=Button(cb2)
    btn2.press()

