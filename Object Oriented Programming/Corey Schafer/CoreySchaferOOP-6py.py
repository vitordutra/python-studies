# Python Object-Oriented Programming


class Employee:

    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

        Employee.number_of_employees += 1

    # unambiguous representation of the object
    # should be used for debugging, logging, etc
    # meant to be seen by other developers
    def __repr__(self):
        return "Employee('{0.first_name}', '{0.last_name}', '{0.payment})".format(self)

    # Readable representation of an object
    # Meant to be used as a display to the end-user
    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)

    def __add__(self, other):
        return self.payment + other.payment

    def __len__(self):
        return len(self.first_name) + len(self.last_name)

    def fullName(self):
        return "{0.first_name} {0.last_name}".format(self)

    def apply_raise(self):
        self.payment = int(self.payment * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Alternative constructor (From String of Employee)
    @classmethod
    def from_string(cls, employee_string):
        first, last, pay = employee_string.split('-')
        # cls is the class: ->Employee<- in this case
        # it instatiates the object with first, last and pay as arguments
        # ==Employee(John, Doe, 70000)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if (day.weekday() == 5) or (day.weekday() == 6):
            return False
        return True


emp_1 = Employee("Zezinho", "Funkeiro", 5)
emp_2 = Employee("MC", "Ricão", 500000)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(emp_1 + emp_2)

print(len(emp_1))
print(len(emp_2))
