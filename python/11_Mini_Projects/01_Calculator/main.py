def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    
    print("======================= CALCULATOR =================================")
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("invalid input.")
        continue
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    try:
        choice = int(input('enter your choice between(1 to 5):'))
    except ValueError:
        print("invalid choice.")
        continue

    
    if choice == 1:
        try:
            addition = add(a,b)
            print(addition)
        except Exception as e:
            print(e)
    elif choice == 2:
        try:
            subtraction = sub(a,b)
            print(subtraction)
        except Exception as e:
            print(e)
    elif choice == 3:
        try:
            Multiplication = multi(a,b)
            print(Multiplication)
        except Exception as e:
            print(e)
       
    elif choice == 4:
        try:
            divide = div(a,b)
            print(divide)
        except ZeroDivisionError:
            print("Cannot divide by zero!")

        except ValueError:
            print("Please enter valid numbers.")

        except Exception as e:
            print("Error:", e)
    elif choice == 5:
        print("Calculator closed.")
        break
    else:
        print("Enter wrong input.")      