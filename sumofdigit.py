n=int(input("enter your number:"))
sum=0

while n > 0:
    sum += n % 10  
    n //= 10       

print(sum)