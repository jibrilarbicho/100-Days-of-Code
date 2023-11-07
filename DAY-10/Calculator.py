def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {"+": add, "-": sub, "*": mult, "/": div}
num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick Operation from the above line:")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2}={answer}")
num3 = int(input("what is the next nubmer?: "))
calculation_function = operations[operation_symbol]
secanswer = calculation_function(answer, num3)
print(f"{answer} {operation_symbol} {num3}={secanswer}")
