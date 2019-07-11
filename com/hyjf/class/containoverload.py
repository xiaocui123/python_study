class Iters:
    def __init__(self,value):
        self.data=value

    def __getitem__(self, item):
        print('get[%s]:' %item, end=' ')
        return self.data[item]

    def __iter__(self):
        print('item=〉', end=' ')
        self.ix = 0
        return self

    def __next__(self):
        print('next:',end=' ')
        if self.ix ==len(self.data):
            raise StopIteration
        item=self.data[self.ix]
        self.ix+=1
        return item
    def __contains__(self, item):
        print('contains:',end=' ')
        return item in self.data

if __name__ == '__main__':
    X=Iters([1,2,3,4,5])

    print(3 in X)

    for i in X:
        print(i,end=' | ')

    print()
    print([i**2 for i in X])
    #
    print(list(map(bin,X)))
    #
    I=iter(X)
    while True:
        try:
            print(next(I),end=' @ ')
        except StopIteration:
            break
    #
