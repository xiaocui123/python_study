class ListInstance:
    def __attrnames(self):
        result=''
        for attr in sorted(self.__dict__):
            result+='\tname %s = %s\n' % (attr,self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instantce of %s, address %s :\n%s>' %(self.__class__.__name__,id(self),self.__attrnames())

class splam(ListInstance):
    def __init__(self,value):
        self.data1=value

if __name__ == '__main__':
    x=splam('food')

    print(x)