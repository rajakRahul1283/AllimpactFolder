n=int(input())
nums=list(map(int, input().split()))
found=False
for i in range(len(nums)):
     temp=nums[:i]+nums[i+1:]
     increase=True
     for j in range(len(temp)-1):
          if temp[j]>=temp[j+1]:
               increase=False
               break
     if increase:
          found=True
          break
print("true" if found else "false")
               