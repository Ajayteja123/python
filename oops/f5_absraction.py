from abc import ABC, abstractmethod


class Cal(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def add(self):
        pass

    def sub(self):
        pass

# if we create a object for this class it throws errors because every method which is abstract class should be present in child class


class A(Cal):
    def add(self):
        print(self.value+100)


class B(A):
    def sub(self):
        print(self.value-10)

    # def drink(self):
    #     print('it drink water')


obj = B(100)
obj.add()
obj.sub()
