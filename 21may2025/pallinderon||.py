s = "abca"
left = 0
right = len(s) - 1
while left < right:
    if s[left] == s[right]:
        left += 1
        right -= 1
    else:
        removed_left = s[:left] + s[left+1:]   
        removed_right = s[:right] + s[right+1:] 
        is_valid = (removed_left == removed_left[::-1]) or (removed_right == removed_right[::-1])
        break
else:
    is_valid = True

print("Valid after removing at most one character:", is_valid)


