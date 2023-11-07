# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression

import time
import math

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50]) 
    loop = True 
    while loop: 
        # Print Menu
        print("\nMain Menu")
        print("1. Spell Check a Word (Linear Search)") 
        print("2. Spell Check a Word (Binary Search)") 
        print("3. Spell Check Alice in Wonderland (Linear Search)") 
        print("4. Spell Check Alice in Wonderland (Binary Search)")   
        print("5. Exit") 

        # Get Menu Selection from User
        selection = input("Enter Selection (1-5): ") 

        if selection == "1":  
            wordInput = input("Enter a word: ") 
            startTime = time.time()
            if linearSearch(dictionary, wordInput) == -1:
                endTime = time.time() 
                timeElapsed = endTime - startTime
                print("Word could not be found. (" + str(timeElapsed) + " seconds)") 
            else:
                endTime = time.time() 
                timeElapsed = endTime - startTime 
                print("Word was found at position " + str(linearSearch(dictionary, wordInput)) + ". (" + str(timeElapsed) + " seconds)")
        elif selection == "2": 
            word = input("Enter a word: ") 
            startTime = time.time()
            if binarySearch(dictionary, word) == -1: 
                endTime = time.time() 
                timeElapsed = endTime - startTime
                print("Word could not be found. (" + str(timeElapsed) + " seconds)")
            else:
                endTime = time.time() 
                timeElapsed = endTime - startTime 
                print("Word was found at position " + str(binarySearch(dictionary, word)) + ". (" + str(timeElapsed) + " seconds)") 
        elif selection == "3": 
            notWords = 0
            startTime = time.time()
            for i in range(len(aliceWords)): 
                if linearSearch(dictionary, aliceWords[i].lower()) == -1: 
                    endTime = time.time() 
                    timeElapsed = endTime - startTime 
                    notWords += 1 
            print("Number of words not found in the dictionary: " + str(notWords) + " (" + str(timeElapsed) + " seconds)")
        elif selection == "4":
            notWords = 0
            startTime = time.time()
            for i in range(len(aliceWords)): 
                if binarySearch(dictionary, aliceWords[i].lower()) == -1: 
                    endTime = time.time() 
                    timeElapsed = endTime - startTime 
                    notWords += 1 
            print("Number of words not found in the dictionary: " + str(notWords) + " (" + str(timeElapsed) + " seconds)")
        elif selection == "5":
            loop = False

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()    
# Linear Search Function
def linearSearch(anArray, item):
    for i in range((len(anArray))):
        if anArray[i] == item:
            return i 
    return -1 
# Binary Search Function
def binarySearch(anArray, item):
    lowDex = 0
    highDex = len(anArray) - 1

    while lowDex <= highDex:
        middleDex = math.floor((highDex + lowDex) / 2) 
        if (item == str(anArray[middleDex])):
            return middleDex 
        elif (item < str(anArray[middleDex])):
            highDex = middleDex - 1
        else:
            lowDex = middleDex + 1 
    return -1 
# Call main() to begin program
main() 
