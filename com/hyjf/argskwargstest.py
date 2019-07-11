def test_var_args(f_arg,*argv):
    print("first args is %s" % f_arg)
    for var in argv:
        print("another arg through *argv:",var)

def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0}=>{1}".format(key,value))


mydict={
    "zhangsan":90,
    "lisi":80,
    "wangwu":100,
    "zhaoliu":60
}

if __name__ == '__main__':
    test_var_args("zhangsan","lishi","wangwu","zhaoliu")

    greet_me(**mydict)

    greet_me(zhangsan=100,lisi=90,wangwu=98,zhaoliu=98)