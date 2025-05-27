import math

def is_perfect(n):
    root = math.isqrt(n)
    # print(root)
    return root * root == n

num = int(input('Enter a Number :'))
if is_perfect(num):
    print('Perfect Sqaure')
else:
    print('Not a Perfect Square')