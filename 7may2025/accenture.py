Num = int(input("Enter your number: "))
m = int(input("Enter the multiple: "))

q = Num // m  
lower = q * m
upper = (q + 1) * m

d1 = (Num - lower)
d2 = (upper - Num)

if d1 < d2:
    print(lower)
else:
    print(upper)



     