from project.food import Fruit, Meat, Seed, Vegetable
from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.preffered_foods = [Fruit, Vegetable]
        self.weight_increase = 0.10
    
    def make_sound(self):
        return "Squeak"

class Dog(Mammal):
    def __init__(self, name, weight, living_region):       
        super().__init__(name, weight, living_region)
        self.preffered_foods = [Meat]
        self.weight_increase = 0.40
    
    def make_sound(self):
        return "Woof!"

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.preffered_foods = [Meat, Vegetable]
        self.weight_increase = 0.30
    
    def make_sound(self):
        return "Meow"

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.preffered_foods = [Meat]
        self.weight_increase = 1
    
    def make_sound(self):
        return "ROAR!!!"