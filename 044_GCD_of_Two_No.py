def gcd(a,b):
    while b:
        a,b = a, a % b
    return a

num1 = 20
num2 = 15
print('GCD :',gcd(num1, num2))