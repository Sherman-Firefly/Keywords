word=input("Input a word: ")
for i in word:
    if (i=="A") or (i=="E") or (i=="I") or (i=="O") or (i=="U"):
        print("Vowel found")
        break
    else:
        print("Vowel is not found")