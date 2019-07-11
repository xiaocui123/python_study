class NextClass:
    def printer(self,value):
        self.message=value
        print(self.message)

if __name__ == '__main__':

    x=NextClass()

    NextClass.printer(x,"instance call")

    x.printer('instance call')

    NextClass.printer(x,'test')