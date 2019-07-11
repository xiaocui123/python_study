from collections import namedtuple,deque

def testNametuple():
    Point=namedtuple("Point",['x','y'])
    p=Point(1,2)
    print('x=%d,y=%d' %(p.x,p.y))
    print(isinstance(p,tuple))

def testDeque():
    q=deque(['a','b','c'])
    q.append('x')
    q.appendleft('y')
    print(q)


if __name__ == '__main__':

    testNametuple()
    testDeque()