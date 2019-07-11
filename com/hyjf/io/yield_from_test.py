from itertools import chain

my_list=[1,2,3]
my_dict={
    "bobby1":"http://projectedu.com",
    "bobby2":"http://www.imoc.com"
}

def my_chain(*args,**kwargs):
    for my_iterable in args:
        yield from my_iterable


for value in my_chain(my_list,my_dict,range(5,10)):
    print(value)