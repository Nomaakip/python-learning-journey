def redo():
    print("Please enter a number:")
    number = input()
    print("What do you want to do with " ,number,"?")
    print("1. Addition (+)  2. Substract (-)  3. Multiply (*)  4. Divide (/)")
    operation = input()
    print("Please enter a second number")
    number2 = input()
    if (operation == "+"):
        add = int(number) + int(number2)
        print(add)
    if (operation == "-"):
        sub = int(number) - int(number2)
        print(sub)
    if (operation == "*"):
        mult = int(number) * int(number2)
        print(mult)
    if (operation == "/"):
        q = int(number) / int(number2)
        print(q)
def calc():
    print("Welcome to swagcalculator.Please enter a number:")
    number = input()
    print("What do you want to do with " ,number,"?")
    print("1. Addition (+)  2. Subtract (-)  3. Multiply (*)  4. Divide (/)")
    operation = input()
    print("Please enter a second number")
    number2 = input()
    if (operation == "+"):
        add = int(number) + int(number2)
        print(add)
    if (operation == "-"):
        sub = int(number) - int(number2)
        print(sub)
    if (operation == "*"):
        mult = int(number) * int(number2)
        print(mult)
    if (operation == "/"):
        q = int(number) / int(number2)
        print(q)
print("Would you like to do another operation? y/n")

answer = input()
if (answer == "y"):
    redo()
else:
    print("okay! closing now..")
