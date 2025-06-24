class Entity():

    def __init__(self, health):
        self.health = health

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        return self.health