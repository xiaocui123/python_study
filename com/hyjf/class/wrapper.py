class Wrapper:
    def __init__(self,object):
        self.wrapped=object

    def __getattr__(self, item):
        print('Trace:',item)
        return getattr(self.wrapped,item)

if __name__ == '__main__':
    a=[1,2,3,4]
    wrapper=Wrapper(a)
    wrapper.append(5)
    print(a)

    wrapper.reverse()
    print(a)
