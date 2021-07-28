
class Trainer:
    _id = 1

    def __init__(self, name) -> None:
        self.name = name
        self.id = Trainer._id
        Trainer._id += 1
           
    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"
    
    @staticmethod
    def get_next_id():
        return Trainer._id