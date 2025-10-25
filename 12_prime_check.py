# Program to check if a number is prime or not
try:
    n = int(input("Enter any number:- "))
except ValueError:
    print("Please enter a valid integer")
    raise

if n <= 1:
    print("Not Prime")
else:
    # only need to check up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        # loop completed without finding a divisor
        print("Prime") 


# Optimized version
n = int(input())
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):   # only need to check up to sqrt(n)
        if n % i == 0:
            return False
    return True
if isprime(n):
    print("Prime")  
else:
    print("Not Prime")