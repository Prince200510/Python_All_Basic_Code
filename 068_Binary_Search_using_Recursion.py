def binary_search(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1

arr = [2, 3, 10, 20, 66, 70]
target = 66
result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print('Element found at index :', result)
else:
    print('Element not found')