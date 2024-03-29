from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args,**kwargs)
    return decorated

@decorator_name
def fun():
    return ("Funciton is running")

can_run=True
print(fun())

can_run=False
print(fun())
