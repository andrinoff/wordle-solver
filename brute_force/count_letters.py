import numpy as np
words = np.loadtxt("words.txt", dtype=str)
letters = np.loadtxt("letters.txt", dtype=str)
word_count = {}

for letter in letters:
    for word in words:
        if letter in word:
            if letter in word_count:
                word_count[letter] += 1
            else:
                word_count[letter] = 1
sorted_letters = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_letters)

