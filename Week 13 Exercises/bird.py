from animal import Animal
from abilities import Can_Fly
    
class Bird(Animal, Can_Fly):#Bird inherits from Animal. Bird can fly  and Dog is a Animal
    def __init__(self, name, age):
        super().__init__(name, age)