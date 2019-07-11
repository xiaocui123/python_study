from functools import wraps

def logit(logname="out.log"):

    def loggingdecorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):

            print(func.__name__+" was called")

            with open(logname,'a') as opened_file:
                opened_file.write("logging....................")

            return func(*args,**kwargs)

        return wrapped_function

    return loggingdecorator

def fun1():
    pass

if __name__ == '__main__':

    wrapper=logit()(fun1)
    wrapper()