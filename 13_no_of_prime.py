# Program to count number of prime numbers between 1 and n

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    count = 0
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):
            count += 1
            prime_list.append(num)
    return count, prime_list

n = int(input('Enter a number: '))
if n < 1:
    print('Please enter a number greater than 0')
else:
    prime_count, primes = count_primes(n)
    print(f'Number of primes between 1 and {n}: {prime_count}')
    print(f'Prime numbers: {primes}')
