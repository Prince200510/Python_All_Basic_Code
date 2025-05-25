# String
def palindrome(num):
    return num == num[::-1]

if palindrome('madam'):
    print('Is a Palindrome')
else:
    print('Is not a palindrome')

# Numbers
def palindromes(number):
    return str(number) == str(number)[::-1]

if palindromes(101):
    print('Is a Palindrome')
else:
    print('Is not a palindrome')