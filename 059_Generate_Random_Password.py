import random 
import string
def password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for _ in range(length))
    return password

length = 12
print('Generated password :', password(length))