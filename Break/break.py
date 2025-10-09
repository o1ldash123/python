word = input("Enter a word: ")

for i in word :
    if i.lower() == 'a' :
        print("The letter 'a' was found in the word.")
        break   
    else:
        print('a not found')