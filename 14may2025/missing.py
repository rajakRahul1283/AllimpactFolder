n = int(input())

a = list(map(int, input().split()))
positive_nums = []
for i in range(n):
    if a[i] > 0:
        positive_nums.append(a[i])
i = 1
while True:
    if i not in positive_nums:
        print(i)
        break
    i += 1
