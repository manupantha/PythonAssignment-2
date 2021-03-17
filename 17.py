while True:
    try:
        input1 = int(input("enter 1st number: "))
        break
    except ValueError:
        print("enter valid number ")
while True:
    try:
        input2 = int(input("enter 2nd number: "))
        break
    except ValueError:
        print("enter valid number ")
while True:
    operator = input("enter the operator: ")
    if operator == '+':
        print("sum = ", input1 + input2)
        break
    elif operator == '-':
        print("Difference = ", abs(input1 - input2))
        break
    elif operator == '*':
        print("Multiplication = ", input1 * input2)
        break
    elif operator == '/':
        try:
            print("Division = ", input1 / input2)
        except ZeroDivisionError:
            print("Cannot divide number by zero ")
        break
    else:
        print("Please insert the valid operator ")
