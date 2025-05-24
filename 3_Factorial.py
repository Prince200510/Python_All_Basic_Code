def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1) 

print(fact(5))

def without_recursive_fact(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(without_recursive_fact(5))