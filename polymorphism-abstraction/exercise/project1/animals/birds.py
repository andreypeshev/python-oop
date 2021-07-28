from project.food import Fruit, Meat, Seed, Vegetable
from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.preffered_foods = [Meat]
        self.weight_increase = 0.25
    
    def make_sound(self):
        return "Hoot Hoot"

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.preffered_foods = [Meat, Fruit, Vegetable, Seed]
        self.weight_increase = 0.35
    
    def make_sound(self):
        return "Cluck"
    

