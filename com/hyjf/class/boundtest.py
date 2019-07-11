def square(arg):
    return arg**2

class Sum:
    def __init__(self,value):
        self.value=value
    def __call__(self, arg):
        return self.value+arg

class Product:
    def __init__(self,value):
        self.value=value

    def method(self,arg):
        return self.value*arg

if __name__ == '__main__':
    sobject=Sum(2)
    pobject=Product(3)
    actions=[square,sobject,pobject.method]
    for action in actions:
        print(action(5))

