def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 2
if prime(n):
    print("It is a prime number", n)
else:
    print("It is not a prime number", n)
    
# Finding a prime number from range 1 to 100

def primes(n):
    if n <= 1:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True

for i in range(2, 100):
    if primes(i):
        print("It is a prime number", i)
    else:
        print("It is not a prime number", i)

# Appending all prime and Non prime numbers in a list
prime_numbers = []
non_prime_number = []
for i in range(2, 100):
    if primes(i):
        prime_numbers.append(i)
    else:
        non_prime_number.append(i)

print(prime_numbers)
print(non_prime_number)