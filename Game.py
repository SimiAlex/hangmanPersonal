
import random
import os

#main

clear = lambda: os.system('clear')
WordsList = ['alfabet', 'schizofrenie', 'biblioteca',
             'pneumonie', 'extraterestu', 'bibliografie',
             'biologie', 'master', 'ipocrit', 'temperatura',
             'enciclopedie', 'temperament', 'bufnita', 'papusel',
             'sarcastic', 'intrebari', 'raspunsuri', 'caracatita',
             'romantic', 'romance', 'sarman', 'inteligenta', 'zgarie',
             'apocaliptic', 'apocalipsa']

word_to_guess = WordsList[int(random.random()*len(WordsList))]
word_to_guess =  word_to_guess.upper()
tempWord = len(word_to_guess)*'_'
print()
for i in tempWord:
        print(i,end=' ')
print()        
lives = 7
badLetters = ''

#function

def tempFunction():
    tempString = ''
    marker = 0

    for i in range(len(word_to_guess)):
        if letterInput != word_to_guess[i]:
            if word_to_guess[i] == tempWord[i]:
                tempString += word_to_guess[i]
            else:
                tempString += '_'
        else:
            marker = 1
            tempString += letterInput
    
    if marker == 0:
        global badLetters 
        badLetters += letterInput + ' '
        global lives
        lives -= 1 
    return tempString

#game loop

print()
while (word_to_guess != tempWord and lives > 0):
    letterInput = input("Choose a letter : ")
    letterInput =  letterInput.upper()
    if letterInput in badLetters:
        continue
    clear()
    print()
    tempWord = tempFunction()
    for i in tempWord:
        print(i,end=' ')
    print("\n\nYou have " + str(lives) +" lives remaining"+ ' | '+badLetters)
    print("\n====================================================================\n")
    

 #the message at the end off the game    

if word_to_guess == tempWord:    
    print("YOU ARE A WINNER!\n")
else:
    print("YOU LOST SUCKER!\n"+"The word was "+word_to_guess+'\n')        



