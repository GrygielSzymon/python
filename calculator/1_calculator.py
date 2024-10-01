a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation: (+, -, *, /, %, **) ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero!")
elif c == "%":
    print(a % b)
elif c == "**":
    print(a ** b)
else:
    print("This is not a valid operator")

input("Press Enter to exit...")
