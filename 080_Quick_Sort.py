def quick(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick(left) + middle + quick(right)

arr = [23, 45, 66, 10, 5]
sorted_array = quick(arr)
print('Sorted Array :', sorted_array)