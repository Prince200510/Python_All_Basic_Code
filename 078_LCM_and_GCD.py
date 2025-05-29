def lcm(x, y):
    lcm1 = (x * y) // gcd(x, y)
    return lcm1
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

num1 = int(input('Enter the first number  :'))
num2 = int(input('Enter the second number :'))
print('LCM : ', lcm(num1, num2))
print('GCD : ', gcd(num1, num2))