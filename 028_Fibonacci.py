def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        print(a, end = ' ')
        a,b = b, a + b

number = int(input('Enter the number of terms :'))
print('Fibonacci Series :')
fibonacci(number)