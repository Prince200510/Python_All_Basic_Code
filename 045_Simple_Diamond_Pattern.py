n = 5
for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)