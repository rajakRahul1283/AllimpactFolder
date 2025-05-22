# s = "Rahul"// using the ascii value for the smallest missing number character
# present = [0] * 26
# i = 0
# while i < len(s):
#     ch = s[i]
#     ascii_value = ord(ch) 
#     if ascii_value >= 65 and ascii_value <= 90:
#         ascii_value += 32  
#     if ascii_value >= 97 and ascii_value <= 122:
#         index = ascii_value - 97
#         present[index] = 1
#     i += 1
# i = 0
# while i < 26:
#     if present[i] == 0:
#         missing_char = chr(i + 97)
#         print("Smallest missing char:", missing_char)
#         break
#     i += 1

alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
s="rahul"
for i in alphabet:
    if i not in s:
        print("the missing number is:",i)
        break