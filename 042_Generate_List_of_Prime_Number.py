def is_prime(start, end):
    prime = []
    
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                prime.append(num)
    return prime

start = int(input('Enter a first prime number :'))
end = int(input('Enter a second number :'))
print('Prime number are :', is_prime(start, end))