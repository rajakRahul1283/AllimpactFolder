arr = [10, 5, 3, 12, 8]

if not arr:
    print("Array is empty")
else:
    min_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
    print("Minimum element:", min_element)