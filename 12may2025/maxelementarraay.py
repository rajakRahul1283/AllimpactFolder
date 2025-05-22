arr = [10, 5, 3, 12, 8]

if not arr:
    print("Array is empty")
else:
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    print("Maximum element:", max_element)
