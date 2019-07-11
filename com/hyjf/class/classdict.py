class super:
    def hello(self):
        self.data1='spam'

class sub(super):
    def hola(self):
        self.data2='eggs'

if __name__ == '__main__':
    # x=sub()
    # print(x.__dict__)
    #
    # print(x.__class__)
    #
    # print(sub.__bases__)
    #
    # print(super.__bases__)
    #
    # print('*'*50)

    Y=sub()
    Y.hola()
    Y.hello()
    print(Y.__dict__)

    print(sub.__dict__.keys())

    print(super.__dict__.keys())
