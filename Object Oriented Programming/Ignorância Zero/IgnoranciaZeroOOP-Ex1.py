class Square:
    def __init__(self, size):
        self.size = size

    def change_size(self, new_size):
        self.size = new_size

    def return_size(self):
        return self.size

    def area(self):
        return self.size**2


q1 = Square(12.1)

print(q1.size)

q1.change_size(25)

print(q1.size)

size_of_q1 = q1.return_size()

print(size_of_q1)

print(q1.area())
