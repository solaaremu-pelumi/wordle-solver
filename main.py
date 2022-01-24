from asyncio import gather
import os
import random
from tracemalloc import start
from turtle import pos


def startApp():
    possible_options = []

    invalid_letters = set()

    right_positions = []  # example [("A", 1)]

    wrong_positions = []  # example [("A", 1)]

    def updateInValidLetters(invalid_letters, invalid):
        for item in invalid:
            if item != '':
                invalid_letters.add(item)

    def readValidWords():
        with open("words_alpha.txt", "r") as file:
            for line in file:
                line = line.rstrip()
                line = line.lstrip()
                if len(line) == 5:
                    possible_options.append(line)

    def updatePossibleOptions():
        new_check = possible_options.copy()
        for item in new_check:
            if not checkRules(item):
                possible_options.remove(item)

    def checkRules(item):
        for letter in invalid_letters:
            if letter in item:
                return False
        for right in right_positions:
            if right[0] == item[right[1]]:
                pass
            else:
                return False
        for wrong in wrong_positions:
            if wrong[0] == item[wrong[1]]:
                return False
            elif wrong[0] not in item:
                return False
        return True

    def gatherInvalidLetters(invalid_letters):
        invalid = input(
            "Input a list of invalid letters seperated by comma")
        invalid = invalid.split(',')
        updateInValidLetters(invalid_letters, invalid)

    def gatherPositions(positions, type):
        not_found = True
        while not_found:
            entry = input(
                f"Enter the valid letter followed by the {type} position in the format 'e,2'")
            if entry == 'q':
                return
            entry = entry.split(',')
            entry_letter = entry[0].lower()
            entry_position = int(entry[1])
            positions.append((entry_letter, entry_position))

    def initiateApp():
        not_found = True
        readValidWords()
        while not_found:
            print(
                f"The amount of possible choices are: {len(possible_options)}")
            print("Input this word")
            print(random.choice(possible_options))
            gatherInvalidLetters(invalid_letters)
            gatherPositions(wrong_positions, "wrong")
            gatherPositions(right_positions, "right")
            updatePossibleOptions()
    initiateApp()


startApp()
