################### Scope ####################

enemies = 1
PI = 3.14159


# Don't modify a Global variable.
def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")


# Instead of modifying we are returning the variable.
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    enemies += 2
    return enemies


# You can define a constant which will never going to change as global
def global_pi():
    global PI
    print(PI)
