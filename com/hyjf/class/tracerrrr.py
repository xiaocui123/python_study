def tracer(func):
    calls=0
    def onCall(*args,**kwargs):
        nonlocal calls
        calls+=1
        print('call %s to %s' %(calls,func.__name__))
        return func(*args,**kwargs)

    return onCall

@tracer
def spam(a,b,c):
    print(a+b+c)

class Person:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    @tracer
    def giveRaise(self,percent):
        self.pay*=(1+percent)
    @tracer
    def lastName(self):
        return self.name.split()[-1]

if __name__ == '__main__':
    print('method........')
    bob=Person('Bob Smith',50000)
    sue=Person('Sue Jones',100000000)

    print(bob.name,sue.name)

    sue.giveRaise(.10)
    print(sue.pay)
    print(bob.lastName(),sue.lastName())

