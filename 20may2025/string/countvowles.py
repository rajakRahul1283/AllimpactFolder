string =input()
vowels = "aeiouAEIOU"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1

print("The number of vowels in '" + string + "' is: " + str(vowel_count))
