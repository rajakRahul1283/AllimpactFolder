print("Enter the size of the array:")
n = int(input())

print("Enter the elements of the array:")
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

max_sum = arr[0]
current_sum = arr[0]

i = 1
while i < n:
    if current_sum < 0:
        current_sum = arr[i]
    else:
        current_sum = current_sum + arr[i]

    if current_sum > max_sum:
        max_sum = current_sum

    i = i + 1

print("Largest subsequence sum is:", max_sum)
