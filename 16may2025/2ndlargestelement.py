arr = [35, 35, 1, 10, 35, 1]

if len(arr) < 2:
    print("Not enough elements")
else:
    if arr[0] > arr[1]:
        largest = arr[0]
        second_largest = arr[1]
    else:
        largest = arr[1]
        second_largest = arr[0]

    for i in range(2, len(arr)):
        num = arr[i]
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if largest == second_largest:
        print("-1")
    else:
        print("Second largest element:", second_largest)
