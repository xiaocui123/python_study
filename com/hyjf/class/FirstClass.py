class FirstClass:

    def setdata(self,value):
        self.data=value

    def getdata(self):
        print(self.data)

class SecondClass(FirstClass):
    def getdata(self):
        print('Second getdata method: %s' % self.data)

class thridClass(SecondClass):
    def __init__(self,value):
        self.data=value

    def __add__(self, other):
        return thridClass(self.data+other)
    def __str__(self):
        return '[thridClass：%s]' % self.data

    def mul(self,other):
         self.data *= other

if __name__ == '__main__':
    firstClass=FirstClass()
    firstClass.setdata("cuiguangqiang")
    firstClass.getdata()

    secondClass=SecondClass()
    secondClass.setdata("cuiguangqiang")
    secondClass.getdata()

    thridClasss=thridClass("abc")
    thridClasss.getdata()

    cc=thridClasss+'xyz'
    thridClasss.getdata()

    cc.getdata()

    cc.mul(3)
    print(cc)

    print(cc.__class__)
    print(thridClass.__dict__.keys())

    print(list(cc.__dict__.keys()))

    print(thridClass.__bases__)

    print(FirstClass.__bases__)
