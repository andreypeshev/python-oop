class Gym:
    def __init__(self) -> None:
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []
    
    def add_customer(self, customer):
        if not customer in self.customers:
            self.customers.append(customer)
        
    def add_trainer(self, trainer):
        if not trainer in self.trainers:
            self.trainers.append(trainer)
    
    def add_equipment(self, equipment):
        if not equipment in self.equipment:
            self.equipment.append(equipment)
    
    def add_plan(self, plan):
        if not plan in self.plans:
            self.plans.append(plan)
    
    def add_subscription(self, subscription):
        if not subscription in self.subscriptions:
            self.subscriptions.append(subscription)
    
    def subscription_info(self, subscription_id):
        result = []
        for i in [self.subscriptions, self.customers, self.trainers, self.equipment, self.plans]:
            result.append(repr(i[subscription_id - 1]))
        return "\n".join(result)
        


