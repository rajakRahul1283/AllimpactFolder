#sum of three the digit 
n=int(input("enter your no:"))
first=n//100
second=(n//10)%10
third=n%10
sum=first+second+third
print(sum)