n=int(input())
binary=0
base=1
while n> 0:
     rem=n%2
     binary=rem*base+binary
     n=n//2
     base=base*10
     
print(binary)
