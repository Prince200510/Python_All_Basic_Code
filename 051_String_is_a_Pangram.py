import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return set(s.lower()) >= alphabet

string1 = input('Enter a String :')
if is_pangram(string1):
    print('Pangram')
else:
    print('Not a Pangram')