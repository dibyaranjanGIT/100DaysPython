# print(123_345.67)
#
# num_char = "123"
#
# print(type(num_char))
#
# # How to do the type casting
# print(type(int(num_char)))


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi =int( weight / (height ** 2))
print(f"The BMI is {bmi}")
