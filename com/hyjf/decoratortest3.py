from functools import wraps

class logit(object):

    def __init__(self,logname="out1.log"):
        self.logname=logname

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            print(func.__name__+" was called")

            with open(self.logname,'a') as opened_file:
                opened_file.write("logging....................")

            self.notify()

            return func(*args,**kwargs)

        return wrapped_function

    def notify(self):
        pass

@logit()
def myfun():
    pass

if __name__ == '__main__':
    myfun()