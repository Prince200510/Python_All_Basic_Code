def binary(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
result = binary(arr, target)

if result != -1:
    print('Element found at index :', result)
else:
    print('Element not found')