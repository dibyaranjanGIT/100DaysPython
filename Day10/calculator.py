import art
def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "*": multiply,
    "/": divide,
    "-": substract
}

print(art.logo)
num1 = float(input("What's the first number ? : "))
continue_calculation = True

def calculator():
    global answer, num1, continue_calculation

    for symbol in operations:
        print(symbol)

    while continue_calculation:

        user_operation = input("What is the operation you want ? ")
        num2 = float(input("What's the second number ? : "))

        for keys, operation in operations.items():
            if user_operation == keys:
                answer = operation(num1, num2)
        print(f"Output : {answer}")
        user_choice = input(f"Type 'y' to continue with {answer} else type 'n' ").lower()
        if user_choice == 'y':
            num1 = answer
            calculator()
        else:
            continue_calculation = False


calculator()

print("** End **")
