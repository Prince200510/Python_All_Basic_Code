def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

print(Fibonacci(10))

def without_recursive_Fibonacci(n):
    a, b = 0, 1
    for i  in range(n):
        a, b = b, a + b
    return a

print(without_recursive_Fibonacci(10))