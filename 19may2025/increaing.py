n=int(input())
nums = list(map(int, input().split()))
count = 0  
for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        count += 1
        if count > 1:
            break
        if i == 1 or nums[i] >= nums[i - 2]:
            nums[i - 1] = nums[i]  
        else:
            nums[i] = nums[i - 1]  

print("true" if count <= 1 else "false")
