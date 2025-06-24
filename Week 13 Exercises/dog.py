from animal import Animal
from abilities import Can_Swim

class Dog(Animal, Can_Swim):#Dog inherits from Animal. Dog is  a DOg and Dog is a Animal
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_age_in_dog_years(self):
        return self.age * 7