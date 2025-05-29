def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

n = 10
print('Fibonnacci :', fibonacci(n))