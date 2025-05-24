import numpy as np
import random
import time
import os

# For local testing
from dotenv import load_dotenv
load_dotenv()


class Brute_Force:
    def __init__(self):
        self.words = np.loadtxt("words.txt", dtype=str)
        self.yellow = []
        self.green =  []
        self.last_guess = ""
        self.grey = []
        self.random = os.getenv("RANDOM")





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

    def simulate(self):
        target = random.choice(self.words)
        print(f"[DEBUG] Target word: {target}")
        for _ in range(5):  # 5 Wordle attempts
            if _ == 0 and self.random == "False":
                self.last_guess = "arose"
            elif len(self.words) == 0:
                print("No words left to guess.")
                break
            else:
                self.last_guess = random.choice(self.words)

            if len(self.words) == 0:

                print("No words left to guess.")
                return False
                break

            print(f"Guess: {self.last_guess}")
            self.generate_feedback(self.last_guess, target)
            for letter in self.last_guess:
                if letter not in self.green and letter not in self.yellow:
                    self.grey.append(letter)
            self.deleteGreys()
            self.deleteGreens(self.last_guess)
            if self.last_guess == target:
                print("Solved!")
                return True
                break
        else:
            return False
            print("Failed to solve.")

    def generate_feedback(self, guess, target):
        self.green = []
        self.yellow = []
        for i, letter in enumerate(guess):
            if target[i] == letter:
                self.green.append(letter)
            elif letter in target and letter not in self.green:
                self.yellow.append(letter)




    def test(self, word):
        print(self.words[word])
test_runs = os.getenv("RUNS")
success = 0
fail = 0
for i in range (0, int(test_runs)):
    solution1 = Brute_Force()
    result = solution1.simulate()
    if result:
        success+=1
    else:
        fail+=1
print("Successfull attempts: " + success)
print("Failed attempts: " + fail)