array = list(map(int, input("Enter the numbers in the list: ").split()))
add = 0

for num in array:
    add=add + num

print("Sum of the list:", add)
