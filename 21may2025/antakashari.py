words = []
used_words = set()
while True:
    w = input().strip()
    if w == "####":
        break
    words.append(w)
if len(words) == 0:
    pass
else:
    print(words[0])       
    used_words.add(words[0])
    
    for i in range(1, len(words)):
        prev_word = words[i-1]
        curr_word = words[i]
        if curr_word[0] == prev_word[-1] and curr_word not in used_words:
            print(curr_word)
            used_words.add(curr_word)
        else:
            break
