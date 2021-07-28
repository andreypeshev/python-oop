class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        cust = list(filter(lambda x: x.id == customer_id, self.customers))
        dvd = list(filter(lambda x: x.id == dvd_id, self.dvds))
        if dvd[0] in cust[0].rented_dvds:
            return f"{cust[0].name} has already rented {dvd[0].name}"
        elif cust[0].age < dvd[0].age_restriction:
            return f"{cust[0].name} should be at least {dvd[0].age_restriction} to rent this movie"
        elif cust[0].age >= dvd[0].age_restriction and not dvd[0].is_rented:
            cust[0].rented_dvds.append(dvd[0])
            dvd[0].is_rented = True
            return f"{cust[0].name} has successfully rented {dvd[0].name}"
        else:
            return "DVD is already rented"

    def return_dvd(self, customer_id, dvd_id):
            for customer in self.customers:
                if customer.id == customer_id:
                    for dvd in customer.rented_dvds:
                        if dvd.id == dvd_id:
                            dvd.is_rented = False
                            customer.rented_dvds.remove(dvd)
                            return f"{customer.name} has successfully returned {dvd.name}"
                    return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result_cust = '\n'.join([repr(cust) for cust in self.customers])
        result_dvd = '\n'.join([repr(dvd) for dvd in self.dvds])
        return f"{result_cust}\n{result_dvd}"




