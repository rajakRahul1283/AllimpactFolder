n, m = map(int, input().split())
groups = list(map(int, input().split()))

buses = 0
current_capacity = 0

for group in groups:
    if current_capacity + group > m:
        buses += 1
        current_capacity = group
    else:
        current_capacity += group

if current_capacity > 0:
    buses += 1

print("maximun no of bus required:",buses)
