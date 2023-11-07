def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


operations = {"+": add, "-": sub, "*": mult, "/": div}


def caclulator():
    num1 = int(input("Enter first number\n"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick Operation from the above line:")
        num2 = int(input("Enter next number\n"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2}={answer}")
        # num3 = int(input("what is the next nubmer?: "))
        # calculation_function = operations[operation_symbol]
        # secanswer = calculation_function(answer, num3)
        # print(f"{answer} {operation_symbol} {num3}={secanswer}")
        if (
            input(
                "type 'y' to continue calualting with {answer}, or type 'x' to exit: "
            )
            == "y"
        ):
            num1 = answer
        else:
            should_continue = False
            caclulator()


caclulator()
