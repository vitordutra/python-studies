# Duck Typing
# Easier to Ask Forgiveness than Permission

# Duck Typing
# You assume: if an object walks like a Duck and talks like a Duck then it's a duck

# You don't care with the type of the object
# You only care if the object do what you ask it to do


class Duck:
    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flap, flap!")


class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def fly(self):
        print("I'm flapping my arms!")


# def quack_and_fly(thing):
#     # Not Duck-Typed(Non-Pythonic)
#     if isinstance(thing, Duck):
#         # We check if the object is an instance of Duck
#         # This will ensure that we can use all of the methods and attributes that we want to use
#         thing.quack()
#         thing.fly()
#     else:
#         print("This has to be a Duck!")
#     print

# def quack_and_fly(thing):
#     # Duck Typed
#     # It doesn't care about the type of the object
#     # It cares about what the objects can do
#     thing.quack()
#     thing.fly()
#     print()

# Look before you leap (LBYL) (Non-Pythonic)
# Example of "Ask for permission"
# def quack_and_fly(thing):
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack):
#             thing.quack()
#     if hasattr(thing, 'fly'):
#         if callable(thing.fly):
#             thing.fly()

# Easier to Ask Forgiveness than Permission (EAFP)
# Let's try do do something
# If it doesn't work then we'll handle it
# A lot more readable
# If it works -> great
# If not -> then just handle that error
def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        # When python tries to run bark() that doesn't exist
        # it threw the AttributeError and print it out to the screen
        thing.bark()
    except AttributeError as e:
        print(e)


"-----------------------------------------------------------------"
d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)
