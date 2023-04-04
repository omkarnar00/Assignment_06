class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def Description(self):
        print(self.name)
        print(self.age)

    def getinfo(self):
        print(self.coat_color)
            
class JackRussellTerrier(Dog):
    def info(self):
        print(f"the coat color of jackrussellterrier is {self.coat_color}")

    def name(self):
        print(f"the name of jackrussellterrier  is {self.name}")  

class BullDog(Dog):
    def info(self):
        print(f"the coat color of bulldog is {self.coat_color}")

    def name(self):
        print(f"the name of bulldog  is {self.name}")              
        
d=BullDog("panther",12,"brown")        
print(d.Description)