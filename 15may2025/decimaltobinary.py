n = int(input("Enter a binary number: "))

decimal = 0  
base = 1     


while n > 0:   
    rem = n % 10         
    decimal = rem * base  + decimal   
    n=n//10              
    base =base * 2                  

print(decimal)
