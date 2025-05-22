n=int(input())
capacity=list(map(int,input().split()))
capacity.sort()
left=0
right=n-1
while left < right:
     print(capacity[right], capacity[left])
     left+=1
     right-=1
if left==right:
     print(capacity[left],0)