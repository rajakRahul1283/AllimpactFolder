arr1 = [5, 2 ]  
arr2 = [5, 8, 3] 

rev1 = 0
rev2 = 0

for i in range(len(arr1)):
    rev1 = rev1 * 10 + arr1[len(arr1) - 1 - i]

for i in range(len(arr2)):
    rev2 = rev2 * 10 + arr2[len(arr2) - 1 - i]

print("Reversed number 1:", rev1)  
print("Reversed number 2:", rev2)  
total = rev1 + rev2
print("Sum:", total)  
rev_sum_arr = []

if total == 0:
    rev_sum_arr.append(0)
else:
    while total > 0:
        digit = total % 10
        rev_sum_arr.append(digit)
        total //= 10

print("Reversed sum as array:", rev_sum_arr)  
