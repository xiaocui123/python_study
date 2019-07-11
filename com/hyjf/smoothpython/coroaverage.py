def average():
    total=0
    count=0
    average=None
    while True:
        term=yield average
        total+=term
        count+=1
        average=total/count

if __name__ == '__main__':
    average=average()
    next(average)

    print(average.send(10))

    print(average.send(20))

    print(average.send(30))

    print(average.send(5))