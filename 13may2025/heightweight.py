n = int(input())  
arr = list(map(int, input().split()))

max_height = arr[0]
max_weight = arr[1]
max_height_index = 0
max_weight_index = 0

for i in range(n):
    height = arr[2 * i]
    weight = arr[2 * i + 1]

    if height > max_height:
        max_height = height
        max_height_index = i

    if weight > max_weight:
        max_weight = weight
        max_weight_index = i

print("Max height:", max_height, "belongs to person number", max_height_index + 1) 
print("Max weight:", max_weight, "belongs to person number", max_weight_index + 1)
