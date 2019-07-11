def generator_fun():
    for i in range(10,100):
        yield i

def fibon(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b


if __name__ == '__main__':

    # for x in fibon(100):
    #     print(x)

    str="Yahoo"
    iteratorr=iter(str)
    for ch in iteratorr:
        print(ch)