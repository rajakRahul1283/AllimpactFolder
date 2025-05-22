def find_middle_digit(number):
 
    num_digits = 0
    temp = number
    while temp > 0:
        temp = temp // 10
        num_digits += 1
    
    digits_to_remove = (num_digits - 1) // 2
    

    for _ in range(digits_to_remove):
        number = number // 10
    
    middle_digit = number % 10
    return middle_digit


number = 42857
result = find_middle_digit(number)
print(f"The middle digit of {number} is: {result}")  