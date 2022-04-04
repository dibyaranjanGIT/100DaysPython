# import another_module
# print(another_module.num)

# from turtle import Turtle, Screen
#
# tom = Turtle()
# tom.shape("turtle")
# tom.color("red")
# tom.forward(100)
# print(tom)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = "l"

print(table)
