#Taylor Howard
#11-01-2020
#CIS2348-14654
#Zylab 11.22

words = input().split()
for word in words:
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(word, count)