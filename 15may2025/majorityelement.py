nums =[1, 1, 1, 1, 1, 1, 3, 2, 2, 2, 2, 2, 2]
count = 0
carry = 0


for num in nums:
    if count == 0:
        carry = num
    if num == carry:
        count += 1
    else:
        count -= 1

print(carry)


