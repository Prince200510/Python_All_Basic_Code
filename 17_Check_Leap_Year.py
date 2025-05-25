def is_leap_year(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    return False

n = 2025
if is_leap_year(n):
    print('It is a leap year :', n)
else:
    print('It is not a leap year :', n)