from tracer import tracer

class Person:

    def __init__(self,name,job,pay = 0):
        self.name=name
        self.job=job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    @tracer
    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))

    def __str__(self):
        return 'Person %s, %s,%s' %(self.name,self.job,self.pay)



if __name__ == '__main__':
    bob=Person('bob smith',job='doctor',pay=1000000)

    print(bob.lastName())

    bob.giveRaise(0.1)
    print(bob)
    print(dir(bob))