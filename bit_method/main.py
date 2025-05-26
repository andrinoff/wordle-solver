import numpy as np
import math


class Bit_Method:
    def __init__(self):
        self.words = np.loadtxt("words.txt", dtype=str)
        self.yellow = []
        self.green =  []
        self.last_guess = ""
        self.grey = []
        self.tempWords = self.words

    def calculate_entropy(self, p):
        if p == 0:
            return 0
        return -math.log2(p)
    def calculate_expected_entropy(self, guess):
        print ("made it to calculate expected entropy")
        
        total_entropy = 0 
        for word in self.words:
            self.tempList(guess, word)
            if len(self.tempWords) != 0:
                p = 1 / len(self.tempWords)
            else: 
                p = 1
            entropy = self.calculate_entropy(p)
            total_entropy+= entropy
            print(str(p), str(entropy), guess, word, str(len(self.tempWords)))
            self.tempWords = self.words
        return total_entropy/len(self.words)

    def tempList(self, guess, target): # target would be any word, guess would be... every word too??
        green = []
        yellow = []
        grey = []
        for i, letter in enumerate(guess):
            if target[i] == letter:
                green.append(letter)
            elif letter in target and letter not in green:
                yellow.append(letter)
            else:
                grey.append(letter)
        filtered_words = []
        for letter in green:
            position_green = self.getPositionOfTheLetter(guess, letter)
            for word in self.tempWords:
                if list(word)[position_green] != letter:
                    word_index = np.where(self.tempWords == word)
                    self.tempWords = np.delete(self.tempWords, word_index)
      
                        
                
        for l in grey:
            for word in self.tempWords:
                if l in list(word):
                    index = np.where(self.tempWords == word)
                    self.tempWords = np.delete(self.tempWords, index)
        return
   
    def getPositionOfTheLetter(self, guess, letter):
        return list(guess).index(letter)

# Caution: will ONLY work the the said letter repeats only once for now
    def deleteGreens(self, guess):
        for letter in self.green:
            position_green = self.getPositionOfTheLetter(guess, letter)
            for word in self.words:
                if list(word)[position_green] != letter:
                    word_index = np.where(self.words == word)
                    self.words = np.delete(self.words, word_index)
        self.green = [l for l in self.green if l != letter]

    def ALotOfPrints(self):
        for word in self.words:
            ex = self.calculate_expected_entropy(word)
            print(word, ex)


bob = Bit_Method()
final_result = bob.calculate_expected_entropy("which")

print(final_result)