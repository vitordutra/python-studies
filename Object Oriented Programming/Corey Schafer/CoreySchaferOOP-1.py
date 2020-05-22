# Python Object-Oriented Programming


class Employee:
    def __init__(self, first_name, last_name, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment
        self.email = f"{first_name.lower()}.{last_name.lower()}@company.com"

    def fullName(self):
        return "{0.first_name} {0.last_name}".format(self)


emp_1 = Employee("João", "Dutra", 2)
emp_2 = Employee("Capeta", "Júnior", 66669)

print(emp_1)
print(emp_2)

# emp_1.first = 'João'
# emp_1.last = "Dutra"
# emp_1.email = "João.Dutra@company.com"
# emp_1.pay = 50000

# emp_2.first = 'Capeta'
# emp_2.last = "Júnior"
# emp_2.email peta.Júnior@company.com"
# emp_2.pay = 66669

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullName())

print(Employee.fullName(emp_1))
