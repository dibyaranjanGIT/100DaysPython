# Reborg's World Python code
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump_huddle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# while not at_goal():
#     jump_huddle()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_huddle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if not front_is_clear():
        jump_huddle()
    else:
        move()

