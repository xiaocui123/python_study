class tracer:
    def __init__(self,func):
        self.calls=0
        self.func=func

    def __call__(self, *args):
        self.calls+=1
        print('call %s to %s' %(self.calls,self.func.__name__))
        self.func(*args)

def decorator(F):
    def wrapper(* args):
        print('call %s' %F)
        F(*args)
    return wrapper

@tracer
def spam(a,b,c):
    print(a,b,c)

if __name__ == '__main__':
    spam(1,2,3)
    spam('a','b','c')
    spam(1,2,3)