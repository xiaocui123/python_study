class PrivateExc(Exception):
    pass

class Privacy:

    def __setattr__(self, key, value):
        if key in self.privates:
            raise PrivateExc
        else:
            self.__dict__[key] = value

class Test1(Privacy):
    privates=['age']


class Test2(Privacy):
    privates=['name','pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    X=Test1()

    Y=Test2()

    X.name = 'zhangsan'
    # Y.name = 'lisi'

    # X.age = 40
    Y.age=100


