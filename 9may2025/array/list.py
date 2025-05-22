user_input = input("Enter numbers separated by commas: ")

num_list = list(map(int, user_input.split(',')))

divisible_by_2 = []


for num in num_list:
    if num % 2 == 0:
        divisible_by_2.append(num)

# Print the result
print("Numbers divisible by 2:", divisible_by_2)
