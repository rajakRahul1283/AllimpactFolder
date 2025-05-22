'''karpekar no example 45 square 2025 than the sum 20+25=45 than compare 
n value which you take the first value '''
n=int(input("enter your no:"))
square=n*n
d=0
temp=n
while temp>0:
    temp=temp//10
    d+=1
divisor=1                                      
i=0
while d>i:
    divisor*=10
    i+=1
    
right=square % divisor
left= square // divisor
if right+left==n:
    print("karpekar number")
else:
    print("not a karpekar number")
