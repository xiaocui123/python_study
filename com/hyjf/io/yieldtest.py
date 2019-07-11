def gen_func():

    try:
        yield "http://www.baidu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return 'bobby'

if __name__ == '__main__':
    gen=gen_func()
    print(next(gen))
    print(gen.throw(Exception,'download error'))
    print(next(gen))

