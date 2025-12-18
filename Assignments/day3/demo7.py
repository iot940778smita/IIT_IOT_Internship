def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)

n = int(input("Enter a number for factorial: "))
print("Factorial:", factorial(n))

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print("Power:", power(base, exponent))