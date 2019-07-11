# def squal(x):
#     return x*x
#
# print(list(map(squal,[1,2,3,4])))
#
# print(list(map(lambda x:x*x,range(10))))

#  还能应用于列表函数
def multiply(x):
    return x*x

def add(x):
    return x+x

funcs=[multiply,add]

for i in range(10):
    print(list(map(lambda x:x(i),funcs)))