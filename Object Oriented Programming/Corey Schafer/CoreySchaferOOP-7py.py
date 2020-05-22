# Python Object-Oriented Programming


class Employee:

    def __init__(self, first_name, last_name, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment

    @property
    def fullname(self):
        return "{0.first_name} {0.last_name}".format(self)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"


emp_1 = Employee("Zezinho", "Funkeiro", 5)
emp_2 = Employee("MC", "Ricão", 500000)

# emp_1.first_name = "Lukinhas"

emp_1.fullname = "Lukinhas Loko"

print(emp_1.first_name)
# This happens because the constructor (or dunder init method) only runs ONCE!
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
print(emp_1.last)
