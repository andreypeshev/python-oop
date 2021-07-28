from project1.caretaker import Caretaker
from project1.cheetah import Cheetah
from project1.keeper import Keeper
from project1.lion import Lion
from project1.tiger import Tiger
from project1.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.name = name
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        if self.workers:
            for worker in self.workers:
                if worker.name == worker_name:
                    self.workers.remove(worker)
                    return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):

        # more pythonistic than a for-loop:
        total_salaries = sum(map(lambda worker: worker.salary, self.workers))

        # for worker in self.workers:
        #     total_salaries += worker.salary

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):

        total_care_costs = sum(map(lambda animal: animal.money_for_care, self.animals))

        if total_care_costs <= self.__budget:
            self.__budget -= total_care_costs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [f"{animal.__repr__()}" for animal in self.animals if type(animal).__name__ == 'Lion']
        tigers = [f"{animal.__repr__()}" for animal in self.animals if type(animal).__name__ == 'Tiger']
        cheetahs = [f"{animal.__repr__()}" for animal in self.animals if type(animal).__name__ == 'Cheetah']
        nl = "\n"

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{nl.join(lions)}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{nl.join(tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{nl.join(cheetahs)}"

    def workers_status(self):
        keepers = [f"{worker.__repr__()}" for worker in self.workers if type(worker).__name__ == 'Keeper']
        caretakers = [f"{worker.__repr__()}" for worker in self.workers if type(worker).__name__ == 'Caretaker']
        vets = [f"{worker.__repr__()}" for worker in self.workers if type(worker).__name__ == 'Vet']
        nl = "\n"

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{nl.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{nl.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{nl.join(vets)}"











