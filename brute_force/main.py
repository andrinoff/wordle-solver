import numpy as np

class Brute_Force:
    def __init__(self):
        self.words = np.loadtxt("words.txt", dtype=str)
        self.yellow = []
        self.green =  []
        self.last_guess = ""
        self.grey = []

    def start(self):
        for i in range(0,5):
            # Ask what word the user used and the letter marks
            self.last_guess = input("What word did you use? ")
            for i in range(0,4) :
                yellow_letter = input("What is the yellow letter? 0 for none ")
                if yellow_letter != "0":
                    self.yellow.append(yellow_letter)
                else :
                    break
            for i in range(0,4) :
                green_letter = input("What is the green letter? 0 for none ")
                if green_letter != "0":
                    self.green.append(green_letter)
                else :
                    break
            for letter in self.last_guess:
                if letter not in self.yellow and letter not in self.green:
                    self.grey.append(letter)
            self.deleteGreys()
            self.deleteGreens(self.last_guess)
            print(self.words)
            if len(self.words) <= 2:
                break

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





    def test(self, word):
        print(self.words[word])

solution1 = Brute_Force()
solution1.start()