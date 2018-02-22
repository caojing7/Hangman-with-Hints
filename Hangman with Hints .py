# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:29:50 2018

@author: 晶格
"""

# Hangman game



import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():

    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):

    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    for i in secretWord:  
        if (i in lettersGuessed) == False:  
            return False  
    return True


def getGuessedWord(secretWord, lettersGuessed):

    guessWord = ""  
    for i in secretWord:  
        if (i in lettersGuessed) == True:  
            guessWord += i  
        else:  
            guessWord += "_ "  
    return guessWord  


def getAvailableLetters(lettersGuessed):

    retStr = ("") 
    for i in string.ascii_lowercase:  
        if (i in lettersGuessed) == False:  
            retStr += i  
    return retStr



def matchWithGaps(my_word, other_word):

    count = 0
    match = False
    my_word_wo_spaces = ''.join(my_word.split())
    if len(my_word_wo_spaces) == len(other_word):
      for index, char in enumerate(my_word_wo_spaces):
        if char == other_word[index] or char == '_':
          count += 1
          if count == len(other_word):
            match = True
            break
    return match


def showPossibleMatches(my_word):

    possibleMatches = ''
    for word in wordlist:
      if matchWithGaps(my_word, word):
        possibleMatches += word + " "
    if len(possibleMatches) == 0:
      return 'No possible matches found.'
    else:
      return possibleMatches

def hangman(secretWord):

    print ("Welcome to the game, Hangman!")  
    print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long.") 
    print("You have 3 warnings.")
    print ("-------------") 
  
    chance = 6 
    number = 3
    unique = 0
    lettersGuessed = []
    vowels = ['a','e','i','o','u']
    while (chance > 0 and isWordGuessed(secretWord, lettersGuessed) == False):  
        print ("You have " + str(chance) + " guesses left.")
        print ("Available letters: "),  
        print (getAvailableLetters(lettersGuessed))  
        ch = input("Please guess a letter: ")  
        ch = ch.lower() 
        if ch == '*':
          print(showPossibleMatches(getGuessedWord(secretWord, lettersGuessed)))
        else:
          #check if letter is valid
          if ch in string.ascii_lowercase and ch != '':
            #has letter been guessed?
            if ch not in lettersGuessed:
              lettersGuessed.append(ch)
              #is letter in secret word?
              if ch in secretWord:
                print('Good guess:', end = ' ')
                unique += 1
              elif ch in vowels:
                print ("Oops! That letter is not in my word: " , end = ' ')
                chance -= 2
              else:
              #subtract guess for incorrect guess
                chance -= 1
                print("Opps! That letter is not in my word:", end = ' ')
            
            else:
            #subtract warning for guessing the samething again
              number -= 1
              if number >= 0:
                print("Oops! You've already guessed that letter. You have", number , 'warnings left:', end = ' ')
              else: 
                chance -= 1
                print("Oops! You've already guessed that letter. You have no warnings left.\nso you lose one guess:")
          else:
          #subtract a warning for a non-letter/word
            number -= 1
            if number >= 0:
              print("Opps! That is not a valid letter. You have", number, 'warnings left:', end = ' ')
            else: 
              chance -= 1
              print("Oops! You've already guessed that letter. You have no warnings left.\nso you lose one guess:")
        print(getGuessedWord(secretWord, lettersGuessed))
        print ("-------------")  
    
    #winner message
    if isWordGuessed(secretWord, lettersGuessed):  
        print ("Congratulations, you won!")
        print ("your total score in this is:" + str(chance * unique))
    #loser message
    else:  
        print ("Sorry, you ran out of guesses. The word was:" , secretWord)



if __name__ == "__main__":
    
    secretWord = chooseWord(wordlist).lower()  
    hangman(secretWord) 