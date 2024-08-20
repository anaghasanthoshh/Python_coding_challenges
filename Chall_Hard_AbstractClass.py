from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def type(self):
        return print("Its an animal")

class Dog(Animal):
    def sound(self):
        print('woof')

obj=Dog()
obj.sound()