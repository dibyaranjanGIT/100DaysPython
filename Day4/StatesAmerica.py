import random

# import my_module

print(random.randint(1, 100))
random_float = random.random()
print(random_float * 5)  # To generate a random float number between 0 and 5

# print(my_module.pi)
state_list = []
infile = open('States', 'r')
for state in infile:
    state_list.append(state)

infile.close()

state_list=[state.replace('\n', '') for state in state_list]
print(state_list[:4])
