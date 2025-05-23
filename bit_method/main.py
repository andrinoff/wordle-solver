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
            feedback = self.generate_feedback(guess, word)
            # Calculate probability of this feedback
            # This is a simplification; a full implementation would need to count how many words produce this feedback
            p = 1 / len(self.tempWords)
            print (p)
            print (word+guess)
            self.tempWords = self.words
            total_entropy += self.calculate_entropy(p)
        return total_entropy

    def generate_feedback(self, guess, target): # target would be any word, guess would be... every word too??
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
        for word in self.words:
            print (word + " checking")
            for l in grey:
                if l in word:
                    print ("Deleting " + word )
                    word_index = np.where(self.words == word)
                    self.tempWords = np.delete(self.words, word_index)
        return (green, yellow)
    def deleteGreys(self):
        for letter in self.grey:
            for word in self.words:
                # If none found -- delete
                word_index = np.where(self.words == word)
                if letter in word:
                    self.words = np.delete(self.words, word_index)
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
bob.ALotOfPrints()