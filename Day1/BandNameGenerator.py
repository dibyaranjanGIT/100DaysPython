#1. Create a greeting for your program.
print("Welcome to the GAME !")

#2. Ask the user for the city that they grew up in.
city = input("In which city did you grow up ?\n")

#3. Ask the user for the name of a pet.
pet_name = input("Name of your pet ?\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = pet_name + " " + city

#5. Make sure the input cursor shows on a new line, see the example at:
print(f"Your band name is {band_name}")