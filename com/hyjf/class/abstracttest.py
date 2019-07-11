from abc import ABCMeta,abstractmethod

class Super(ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass

class Sub(Super):
    def action(self):
        print('sub action')


