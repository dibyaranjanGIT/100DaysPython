programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary['Bug'])

# Adding a new item in dictionary
programming_dictionary["Hello"] = "Hello World"

# Loop through dictionary
for kye, values in programming_dictionary.items():
    print(values)

# Nesting Dictionary
travle_log={
    "Fance":{"Cities_visited":["Paris","Lille","Dijon"]},
    "Germany":["Berlin","Hamburg"]
}