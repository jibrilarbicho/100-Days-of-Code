import anotherModule

from prettytable import PrettyTable

# Rest of your script...

# print(anotherModule.another_variable)
from turtle import Turtle, Screen

timmy = Turtle()
timmy.color("coral")
timmy.forward(100)
screen = Screen()
# print(screen.canvheight)
# screen.exitonclick()
table = PrettyTable()
# print(table)
table.add_column("Pokemoon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Fire", "Water"])
print(table)
