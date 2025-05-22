num = int(input("Enter your number: "))     
square = num * num                          

n = num
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10
reversed_square = reversed_num * reversed_num
temp = reversed_square
final_reverse = 0
while temp > 0:
    digit = temp % 10
    final_reverse = final_reverse * 10 + digit
    temp = temp // 10
if final_reverse == square:
    print("Adam number")
else:
    print("Not an Adam number")
