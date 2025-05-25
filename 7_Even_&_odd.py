num = 5

if num % 2 == 0:
    print('Even :', num)
else:
    print('Odd :', num)
    
# Even odd from range 1 to 100
even = []
odd = []

def even_or_odd(number):
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

for i in range(1, 100):
    even_or_odd(i)

print('Even :', even)
print('Odd', odd)
