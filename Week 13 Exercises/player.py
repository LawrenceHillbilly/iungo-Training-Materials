from entity import Entity

class Player(Entity):
    def __init__(self, name, health):
        super().__init__(health)
        self.name = name
    
    def get_character_desc(self):
        return f"{self.name} has {self.health} health"