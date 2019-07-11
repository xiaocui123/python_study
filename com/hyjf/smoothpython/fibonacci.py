from com.hyjf.smoothpython.timeelapsedcount import clock
import functools
import html

@functools.lru_cache()
@clock
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

def htmlize(obj):
    content=html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


if __name__ == '__main__':
    # print(fibonacci(30))
    # pass
    print(htmlize({1,2,3}))

    print(htmlize(abs))










