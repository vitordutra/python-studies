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
        self.payment = int(self.payment * Employee.raise_amount)


emp_1 = Employee("João", "Dutra", 200)
emp_2 = Employee("Capeta", "Júnior", 66669)

print(Employee.number_of_employees)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)
