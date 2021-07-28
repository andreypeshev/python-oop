import datetime

class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        date_list = date.split(".")[1:]
        creat_month, creat_year = date_list
        creat_year = int(creat_year)
        month_obejct = datetime.datetime.strptime(creat_month, "%m")
        full_month_name = month_obejct.strftime("%B")
        return cls(name, id, creat_year, full_month_name, age_restriction)

    def __repr__(self):
        if self.is_rented:
            rented = 'rented'
        else:
            rented = 'not rented'
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented}"
