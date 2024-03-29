import random
class BingoCage:
    def __init__(self,items):
        self._items=list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == '__main__':
    bingoCage=BingoCage(range(3))

    print(bingoCage.pick())

    print(bingoCage())

    print(callable(bingoCage))
