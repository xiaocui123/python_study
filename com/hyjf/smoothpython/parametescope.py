def f1(a):
    global b
    print(a)
    print(b)
    b=9

if __name__ == '__main__':
    b=10
    f1(3)