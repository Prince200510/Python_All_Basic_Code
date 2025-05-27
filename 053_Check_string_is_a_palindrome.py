def is_palindrome(s):
    return s == s[::-1]

string = input('Enter a String :')
if is_palindrome(string):
    print('Palindrome')
else:
    print('Not a Palindrome')
