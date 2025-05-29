import re

def is_valid_email(email):
    return bool(re.match(r'[^@]+@[^@]+\.[^@]+', email))

email = input('Enter a email id :')

if is_valid_email(email):
    print('Valid Email Address')
else:
    print('Invalid Email Address')