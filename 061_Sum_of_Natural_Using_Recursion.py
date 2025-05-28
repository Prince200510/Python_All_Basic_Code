def sum_of_natural(n):
    if n <= 1:
        return n
    else: 
        return n + sum_of_natural(n - 1)

num = int(input('Enter a Number :'))
print('Sum of Natural Number :', sum_of_natural(num))