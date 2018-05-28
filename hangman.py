import random
import re





def chooseword(wordlist, finder):
    return finder(wordlist)

def getWordStateForPrint(wordList):
    blankOrHash = [letter if letter in guessLetters else '_' for letter in wordList]
    return ' '.join(blankOrHash)


fruitwords = ['apple', 'banana', 'pineapple']

word = chooseword(fruitwords, random.choice)



attemptsLeft = 7
guessLetters = set(['$'])
gameActive = True



while gameActive == True:

    attemptsLeft = attemptsLeft - 1



    print getWordStateForPrint(list(word))
    if attemptsLeft > 0:
        print 'Attempts left: ' + str(attemptsLeft)
    else: 
        print 'GAME OVER MAN GAME OVER'


    correctInput = False
    while correctInput == False:
        newletter = str(input('Guess a letter: '))
        if len(newletter) > 1:
            print 'One letter please!'
        elif re.match('[a-z]',newletter) == True:
            guessLetters.update(newletter)
            correctInput = True
        else:
            print 'That\'s not a lowercase letter'

    

        
    if attemptsLeft == 0:
        gameActive = False
        



# if attemptsLeft == 0:
#     print '               '
#     print '|_________     '
#     print '|         |    '
#     print '|         O    '
#     print '|        /|\   '
#     print '|        / \   '
#     print '|              '
#     print '               '
# elif attemptsLeft == 1:
#     print '               '
#     print '|_________     '
#     print '|         |    '
#     print '|         O    '
#     print '|        /|\   '
#     print '|              '
#     print '|              '
#     print '               '
# elif attemptsLeft == 2:
#     print '               '
#     print '|_________     '
#     print '|         |    '
#     print '|         O    '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '               '
# elif attemptsLeft == 3:
#     print '               '
#     print '|_________     '
#     print '|         |    '
#     print '|          \   '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '               '
# elif attemptsLeft == 4:
#     print '               '
#     print '|_________     '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '               '
# elif attemptsLeft == 5:
#     print '               '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '               '
# elif attemptsLeft == 6:
#     print '               '
#     print '               '
#     print '               '
#     print '               '
#     print '|              '
#     print '|              '
#     print '|              '
#     print '               '
# elif attemptsLeft == 7:
#     print '               '
#     print '               '
#     print '               '
#     print '               '
#     print '               '
#     print '               '
#     print '               '
#     print 'o              '
    
    