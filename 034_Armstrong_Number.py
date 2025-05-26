def is_armstrong(n):
    order = len(str(n))
    temp = n
    sum = 0
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
        
    return n == sum

number = int(input('Enter a Number :'))

result = 'Armstrong Number' if is_armstrong(number) else 'Not an Armstrong Number'
print(result)

# From Range 1 to 200
armstrong_number = []
for i in range(1, 200):
    if is_armstrong(i):
        armstrong_number.append(i)

print(armstrong_number)

# Examples:
# 🔹 3-digit Armstrong Numbers:
# 153 → 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
# 370 → 3³ + 7³ + 0³ = 27 + 343 + 0 = 370
# 371 → 3³ + 7³ + 1³ = 27 + 343 + 1 = 371
# 407 → 4³ + 0³ + 7³ = 64 + 0 + 343 = 407

# 4-digit Armstrong Numbers:
# 1634 → 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1 + 1296 + 81 + 256 = 1634
# 8208 → 8⁴ + 2⁴ + 0⁴ + 8⁴ = 4096 + 16 + 0 + 4096 = 8208
# 9474 → 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474

# 🔹 1-digit Armstrong Numbers:
# All 1-digit numbers (0–9) are Armstrong numbers, because:
# 5 → 5¹ = 5