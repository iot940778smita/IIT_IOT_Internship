def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 5:
        break
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    if ch == 1:
        print("Result:", add(x, y))
    elif ch == 2:
        print("Result:", sub(x, y))
    elif ch == 3:
        print("Result:", mul(x, y))
    elif ch == 4:
        print("Result:", div(x, y))
    else:
        print("Invalid choice")