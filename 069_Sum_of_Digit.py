def sum_of_digit(n):
    return sum(int(digit) for digit in str(n))

number = int(input('Enter a number :'))
print('Sum of Digit :', sum_of_digit(number))

# Second way
def sum_of_digit_1(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

number1 = int(input('Enter a number :'))
print('Sum of Digit :', sum_of_digit_1(number1))