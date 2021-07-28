from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0
        self.preffered_foods = []
        self.weight_increase = 0 

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food):
        if type(food) in self.preffered_foods:
            self.weight += food.quantity * self.weight_increase
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        self.wing_size = wing_size
        super().__init__(name, weight)

    
    def __repr__(self): 
     return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        self.living_region = living_region
        super().__init__(name, weight)

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"