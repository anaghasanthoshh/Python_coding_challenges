import Plymorphism as pl

class Vehicles:
    def __init__(self,name,model,id):
        self.name=name
        self.model=model
        self.id=id
        self.works=True

    def properties(self):
        return f"This is a {self.name} and its model is {self.model}"

obj=Vehicles("Car","2020.0",12)
#print(obj.works)
#print(obj.properties())
class Car(Vehicles):
    def __init__(self,name,model,id,color):
        super().__init__(name,model,id)
        self.color=color

    def colorprint(self):
        return f"The Color is {self.color}"


    def properties(self):
        return '123'


obje=Car("Audi","1234",34,"red")
print(obje.colorprint())
print(obje.properties())

rect=pl.Rectangle(1,2)
print(rect.Area())








