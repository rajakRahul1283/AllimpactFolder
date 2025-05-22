num = int(input())
arr = list(map(int, input().split()))

left = 0
right = num - 1


while left < right:

    if arr[left] % 2 == 0:
        left += 1
    elif arr[right] % 2 != 0:
        right -= 1
    else:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


print("Array after Segregation")
for num in arr:
    print(num, end=' ')
