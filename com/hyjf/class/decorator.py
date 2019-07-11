def decorator(cls):
    class Wrapper:
        def __init__(self,*args):
            self.wrapped=cls(*args)

        def __getattr__(self, name):
            print('*'*10,'decorator','*'*10)
            return getattr(self.wrapped,name)

    return Wrapper

@decorator
class C:
    def __init__(self,x,y):
        self.attr='spam'

if __name__ == '__main__':
    x=C(3,4)
    print(x.attr)