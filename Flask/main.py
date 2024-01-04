from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "BYE"


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)

# def divide(n1, n2):
# #     return n1 / n2


# # def add(n1, n2):
# #     return n1 + n2


# # def mul(n1, n2):
# #     return n1 * n2


# # def sub(n1, n2):
# #     return n1 - n2


# # # First-class objects, can be passed around as arguments e.g. int/string/float etc.
# # def calculate(calc_function, n1, n2):
# #     return calc_function(n1, n2)


# # result = calculate(add, 2, 3)
# # print(result)


# # # Nested Functions
# # def outer_function():
# #     print("I'm outer")

# #     def nested_function():
# #         print("I'm inner")

# #     nested_function()


# # outer_function()
# import time


# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(5)

#         # Do something before
#         function()

#     return wrapper_function


# @delay_decorator
# def say_hello():
#     print("Hello")


# @delay_decorator
# def say_bye():
#     print("Bye")


# def say_greeting():
#     print("How are you?")


# say_greeting()
# say_bye()
# say_hello()
