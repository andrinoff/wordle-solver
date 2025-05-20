import numpy as np

class Brute_Force:
    def __init__(self):
        self.words = np.loadtxt("words.txt", dtype=str)
        self.letter1 = ""
        self.letter2 = ""
        self.letter3 = ""
        self.letter4 = ""
        self.letter5 = ""
        self.yellow = []
        self.green =  []
        self.last_guess = ""

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
            self.deleteYellows()
            self.deleteGreens(self.last_guess)
            print(self.words)
            if len(self.words) <= 2:
                break

    def deleteYellows(self):
        for letter in self.yellow:
            for word in self.words:
                # If none found -- delete
                word_index = np.where(self.words == word)
                if letter not in word:

                    # TODO: add delete here
                    self.words = np.delete(self.words, word_index)
                # Second round, deleting where the letter would be green
                else:
                    index = self.getPositionOfTheLetter(self.last_guess, letter)
                    if list(word)[index] == letter:
                        self.words = np.delete(self.words, word_index)
        self.yellow = [l for l in self.yellow if l != letter]

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