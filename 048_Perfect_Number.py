def perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

number = int(input('Enter a number :'))

if perfect(number):
    print('Perfect Number')
else:
    print('Not a perfect number')