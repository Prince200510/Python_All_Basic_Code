n = int(input('Enter a number :'))
sum = 0
for i in range(1, n + 1):
    sum += i
print('Sum :', sum)

# without for loop

total = n * (n + 1) // 2
print('Sum :', sum)