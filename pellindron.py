n=int(input("enter your no:"))
rev=0
x=n
while n>0:
     rev=rev*10+n%10
     n//10
if n==rev:
     print("pellinderom")
else:
     print("not pellinderon")