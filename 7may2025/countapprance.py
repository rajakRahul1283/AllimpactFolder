'''sumof number divisible the number of sum'''
n = int(input("Enter your number: "))
original_n = n
sum_digit = 0

while n != 0:
    rem = n % 10
    sum_digit += rem
    n = n // 10

if original_n % sum_digit == 0:
    print("Yes")
else:
    print("No")

