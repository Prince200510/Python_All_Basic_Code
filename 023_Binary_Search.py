def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

array = [45, 67, 23, 60, 10]
array.sort()
target = 45
result = binary_search(array, target)

if result != -1:
    print('Element found at index', result)
else:
    print('Element not found')