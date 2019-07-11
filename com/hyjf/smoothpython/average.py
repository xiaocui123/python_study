class Average:
    def __init__(self):
        self.series=[]

    def __call__(self, newvalue):
        self.series.append(newvalue)
        return sum(self.series)/len(self.series)

def make_average():
    series=[]

    def average(newvalue):
        series.append(newvalue)
        return sum(series)/len(series)
    return average

def make_average_():
    count=0
    total=0

    def average(newvalue):
        nonlocal count,total
        count+=1
        total+=newvalue
        return total/count
    return average

if __name__ == '__main__':
    # average=Average()
    # print(average(10))
    # print(average(11))
    # print(average(12))

    average=make_average()
    print(average(10))
    print(average(11))
    print(average(12))

    av=make_average_()
    print(av(10))
    print(av(11))
    print(av(12))
    print(av(13))
