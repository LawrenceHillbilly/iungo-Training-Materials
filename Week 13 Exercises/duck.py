from animal import Animal
from abilities import Can_Fly
from abilities import Can_Swim

class Duck(Animal, Can_Fly, Can_Swim):#Bird inherits from Animal. Bird can fly  and Dog is a Animal
    def __init__(self, name, age):
        super().__init__(name, age)
    def quack(self):
        return "QUACK"