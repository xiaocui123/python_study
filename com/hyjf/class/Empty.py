class Empty:
    xyz = 'abc'
    def __getattr__(self, item):
        if item == 'age':
            return 40
        else:
            raise AttributeError
    def __setattr__(self, key, value):
        if key == 'name':
            self.__dict__[key] = value
        else:
            raise AttributeError

if __name__ == '__main__':
    X= Empty()

    print(X.xyz)
    print(X.age)
    X.name = 'zhangsan'
    print(X.name)
    


