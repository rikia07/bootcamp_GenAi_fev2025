user_word=inpu("enter a word: ")
indice_word = {}
for index, letter in enumerate(word):
    if letter not in letter_indices:
        letter_indices[letter] = [] 
    indice_word[letter].append(index)

print(indice_word)