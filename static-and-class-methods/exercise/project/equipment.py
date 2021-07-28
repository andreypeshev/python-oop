import itertools

class Equipment:
    _id = 1

    def __init__(self, name) -> None:
        self.name = name
        self.id = Equipment._id
        Equipment._id += 1
            
    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
    
    @staticmethod
    def get_next_id():
        return Equipment._id