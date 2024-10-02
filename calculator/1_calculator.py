while True:
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    operation = input("Wybierz działanie:\n + dodawanie\n - odejmowanie\n * mnożenie\n / dzielenie:\n % reszta z dzielenia\n")

    if operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '*':
        print(a * b)
    elif operation == '/':
        if b == 0:
            print("Nie można dzielić przez zero.")
        else:
            print(a / b)
    else:
        print("Złe działanie\n")

    again = input("Czy chcesz rozpocząć następne działanie? (Tak): ")
    if again == 'Tak':
        continue
    else:
        break
