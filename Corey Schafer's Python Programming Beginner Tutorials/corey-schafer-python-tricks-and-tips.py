# 1. Ternary operators
def ternary_operator():
    condition = False
    x = 1 if condition else 0
    print(x)


# 2. underscores for large numbers
def underscores_for_large_numbers():
    num1 = 10_000_000_000
    num2 = 100_000_000

    total = num1 + num2  # Addition will be performed as usual

    print(f"{total:,}")  # f string formatting to separate the digits by commas


# 3. Context managers
def context_manager_with():
    with open("text.txt", "r") as f:
        file_contents = f.read()
    words = file_contents.split(" ")
    word_count = len(words)
    print(word_count)


# enumerate function
# keeps track of the index of an iterable, no need to manually attribute an index
def enumerate_example():
    names = ["Corey", "Chris", "Dave", "Travis"]
    for index, name in enumerate(names, start=1):
        print(index, name)


# Zip function -> loop over two (or more) lists at once
# Return both values of the list at once
# Shortest list
# There's a function called zip_longest()
def zip_example():
    names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
    heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
    universes = ["Marvel", "DC", "Marvel", "DC"]

    for name, hero, universe in zip(names, heroes, universes):
        print(f"{name} is actually {hero} from {universe}")


def unpacking_examples():
    a, b = (
        1,
        2,
    )  # Usual unpacking -> no of variables and items of the tuple is the same
    a, _ = (
        1,
        2,
    )  # The _ means that we don't want to use this item of the tuple anywhere else in the code
    # a, b = (1,2,3) -> error
    # a, b, c = (1, 2) -> error
    a, b, *c = (1, 2, 3, 4, 5)  # -> a = 1, b = 2 and c = (3, 4, 5)


if __name__ == "__main__":
    zip_example()
    enumerate_example()
