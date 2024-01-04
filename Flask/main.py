def divide(n1, n2):
    return n1 / n2


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def sub(n1, n2):
    return n1 - n2


# First-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 2, 3)
print(result)


# Nested Functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()
