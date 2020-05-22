my_list = [1, 2, 3, 4, 5, 6]

# Non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("That index does not exist")

# Pythonic

try:
    print(my_list[5])
except IndexError:
    print("That index does not exist")
