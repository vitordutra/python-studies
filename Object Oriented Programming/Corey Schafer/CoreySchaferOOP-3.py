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


emp_1 = Employee("João", "Dutra", 200)
emp_2 = Employee("Capeta", "Júnior", 66669)

# print(Employee.number_of_employees)
Employee.set_raise_amount(1.05)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

# print(emp_1.__dict__)
# print(Employee.__dict__)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Peter-Parker-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
