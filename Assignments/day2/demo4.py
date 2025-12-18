
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            print(i, end=' ')

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print_primes_in_range(start, end)