# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    n = int(input())  # Read the integer input
    
    result = 0        # To store the number with zeros moved to the end
    place = 1         # To keep track of the digit's place value (units, tens, etc.)
    count = 0         # To count the number of zeros
    
    # Process digits one by one (from last to first)
    while n > 0:
        digit = n % 10     # Get the last digit
        if digit == 0:
            count += 1     # Count zero
        else:
            result += digit * place
            place *= 10    # Move to the next place
        n //= 10           # Remove the last digit
    
    # Append all zeros to the end by multiplying by 10^count
    result *= (10 ** count)
    
    # Print the result
    print(result)
