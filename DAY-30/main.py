# height = float(input("'Enter your Height"))
# weight = int(input("Enter your Weight"))
# if height > 3:
#     raise ValueError("The height is not graeter than 3m")
# bmi = weight / height**2
# print(bmi)
fruits = ["Apple", "Orange", "Mango"]


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit)
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + "pie")


make_pie(0.9)
