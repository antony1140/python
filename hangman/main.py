# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    word = secretWord
    for i in word:
        if i not in lettersGuessed:
            return False
    return True


def getAvailableLetters(lettersGuessed):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    for i in lettersGuessed:
        if i in letters:
            letters.remove(i)
    available = ' '.join(letters)
    print('letters remaining: ' + available)
    return available


def getGuessedWord(secretWord, lettersGuessed):
    currentWord = []
    for i in secretWord:
        if i in lettersGuessed:
            currentWord.append(i)
        else:
            currentWord.append('_')
    stringify = ' '.join(currentWord)
    print(stringify)


def hangman(secretWord):
    # currentWord = []
    # for i in secretWord:
    #     currentWord.append("_")
    print('the secret word contains ' + str(len(secretWord)) + ' letters')
    # print('\nyour current standing: ')
    # print(' '.join(currentWord))

    lettersGuessed = []
    getGuessedWord(secretWord, lettersGuessed)
    guesses = 8

    cont = 1
    while (cont == 1 and guesses > 0):
        print('Guesses remaining: ', guesses, '\n')
        getAvailableLetters(lettersGuessed)
        letter = input('select a letter from above: ').lower()

        if letter in lettersGuessed:
            print('letter already guessed. No guesses lost')
            continue

        elif letter in secretWord:
            print('\ngood guess!')
            lettersGuessed.append(letter)
            # for i in range(len(secretWord)):
            #     if secretWord[i - 1] == letter:
            #         currentWord[i - 1] = letter

        else:
            print('\nsorry, that letter does not appear in the word. One guess lost')
            lettersGuessed.append(letter)
            guesses -= 1
            if guesses == 0:
                print('Out of guesses! Play again.')
                break

        if isWordGuessed(secretWord, lettersGuessed):
            print('you win!')
            break
            cont = 0

        print('current standing: ')
        # print(' '.join(currentWord))
        getGuessedWord(secretWord, lettersGuessed)

    print('Secret Word: ')
    print(secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()


# secretWord = 'multimillionaire'
hangman(secretWord)
