def factor(n):
    fact = []
    for i in range(1, n + 1):
        if n % i == 0:
            fact.append(i)
    return fact

number = int(input('Enter a number :'))
print('Factors :', factor(number))