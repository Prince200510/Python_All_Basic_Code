def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    
    return lcm

number1 = int(input('Enter a First number :'))
number2 = int(input('Enter a Second number :'))

print('LCM :', lcm(number1, number2))