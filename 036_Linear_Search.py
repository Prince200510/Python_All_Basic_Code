def linar_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [45, 67, 66, 10, 20]
target = 10

result = linar_search(arr, target)
if result != -1:
    print('Element found a index ', result)
else:
    print('Element not found')