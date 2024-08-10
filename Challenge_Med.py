#Create classes Person and Address. Each Person object should have a name
# and an address (an instance of the Address class).
# Implement a method in Person that prints the person’s details.

class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address


    def Details(self):

        return f"Name is {self.name} and address is {self.address} "


class Address:
    def __init__(self,FlatNo,Building,City):
        self.FlatNo=FlatNo
        self.Building=Building
        self.City=City
        self.address=f'{self.FlatNo},{self.Building},{self.City}'

addr=Address('86/7','Spalding','Hatfield')
per=Person('Anu',addr.address)
print(per.Details())
