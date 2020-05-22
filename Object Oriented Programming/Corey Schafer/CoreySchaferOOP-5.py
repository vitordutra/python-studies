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

# Em Java:
# Class Developer extends Employee{}


class Developer(Employee):

    raise_amount = 1.1

    def __init__(self, first_name, last_name, payment, programming_language):
        super().__init__(first_name, last_name, payment)
        self.programming_language = programming_language


class Manager(Employee):

    raise_amount = 1.2

    def __init__(self, first_name, last_name, payment, employees=None):
        super().__init__(first_name, last_name, payment)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print('-->', employee.fullName())


dev_1 = Developer("João", "Dutra", 200, "Python")
dev_2 = Developer("Capeta", "Júnior", 66669, "C++")


class SeniorDeveloper(Developer):
    pass

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

# print(dev_1.payment)
# dev_1.apply_raise()
# print(dev_1.payment)

# print(dev_1.programming_language)


roberto = Manager("Roberto", "Duque", 90000)

# print(roberto.email)

# roberto.print_employees()

# roberto.add_employee(dev_1)

# roberto.add_employee(dev_2)

# roberto.print_employees()

# roberto.remove_employee(dev_1)

# roberto.print_employees()

corey = SeniorDeveloper("Corey", "Schafer", 100000, "Python")

print(issubclass(SeniorDeveloper, Employee))
