class Animal():
    def __init__(self, name, age): #initialisae - fancy function that runs  every time you creat an object. SOmetimes known as CONSTRUCTOR
        #self give the object individuality
        """
        Models an animal within the program
        """
        self.name = name
        self.age = age
    
    def get_desc(self):
        return f"My name is {self.name} and I am {self.age} years old"
        """
        Returns a detailed description of the animal
        """