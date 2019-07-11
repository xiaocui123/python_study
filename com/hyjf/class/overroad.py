class Indexer:
    def __getitem__(self, item):
        return item*2

class Indexerr:
    data=[5,6,7,8,9]
    def __getitem__(self, item):
        print("getitem:",item)
        return self.data[item]


class Number:
    def __init__(self,start):
        self.data=start
    def __sub__(self, other):
        return Number(self.data-other)

class Squares:
    def __init__(self,start,stop):
        self.value=start-1
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value+=1
        return self.value**2


if __name__ == '__main__':
    index=Indexer()
    print(index[9])

    indexx=Indexerr()
    print(indexx[::2])


    a=Number(100)
    b=a-9
    print(b.data)

    iterr=Squares(1,5)

    print(next(iterr))
    print(next(iterr))
    print(next(iterr))
    print(next(iterr))
    print(next(iterr))

    print(list(iterr))

    print([c for c in Squares(1,3)])