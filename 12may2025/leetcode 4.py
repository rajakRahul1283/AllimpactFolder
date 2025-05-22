nums1 = [1, 3, 5, 7]
nums2 = [2, 9, 8, 10,11]
i = 0
j = 0
merged = []

while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        merged.append(nums1[i])
        i += 1
    else:
        merged.append(nums2[j])
        j += 1

while i < len(nums1):
    merged.append(nums1[i])
    i += 1

while j < len(nums2):
    merged.append(nums2[j])
    j += 1

print("Final merged array:", merged)

n = len(merged)
if n % 2 != 0:
    median = merged[n // 2]
    print("Median element:", median)
else:
    mid1 = merged[n // 2 - 1]
    mid2 = merged[n // 2]
    median = (mid1 + mid2) / 2
    print("Median elements:", mid1, "and", mid2)
