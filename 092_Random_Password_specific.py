import random
import string

def password(length, include_digits = True, include_special_chars = True):
    char = string.ascii_letters
    
    if include_digits:
        char += string.digits
    if include_special_chars:
        char += string.punctuation
    passwords = "".join(random.choice(char) for _ in range(length))
    return passwords

password_length = 12
print('Generated Password :', password(password_length))