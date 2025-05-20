import numpy as np

class Brute_Force:
    def __init__(self):
        self.words = np.loadtxt("../words.txt", dtype=str)
        self.letter1 = ""
        self.letter2 = ""
        self.letter3 = ""
        self.letter4 = ""
        self.letter5 = ""
        self.yellow = []
        self.green =  []
        self.first_guess = ""

    def start(self):
        # Ask what word the user used and the letter marks
        self.first_guess = input("What word did you use? ")
        for i in range(0,5) :
            yellow_letter = input("What is the yellow letter? n for none ")
            if yellow_letter != "n":
                self.yellow.append(yellow_letter)
            else :
                break
        for i in range(0,5) :
            green_letter = input("What is the green letter? n for none ")
            if green_letter != "n":
                self.green.append(green_letter)
            else :
                break
        self.deleteYellows()

    def deleteYellows(self,):
        for word in self.words:
            for letter in self.yellow:
                if letter in word:
                    word_index = np.where(self.words == word)
                    print(self.words[word_index])

    def test(self, word):
        print(self.words[word])

solution1 = Brute_Force()
solution1.start()