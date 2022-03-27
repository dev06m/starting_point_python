

def typeGuessedLetter(word, guessedLetters, guessedWord):
    print(guessedword)
    line = ''
    for x in range(len(word)):
        for y in range(1):
            # print(x)
            if word[x] in guessedLetters:
                line = line + guessedLetters[y] + ' '
            else:
                line = line + '_ '
            print(line)
    return line
# result = typeGuessedLetter('application', ['c'])
# print(f'bu {result}')


words = ['application', 'drawing', 'opportunity', 'nation', 'insect', 'exam', 'psychology', 'tea', 'bread', 'disease']
theWord = 'ananas'#words[random.randint(0, len(words)-1)]
isCorrect = True
right = len(theWord) - 1
letters = []
guessedword = ''
def guessWord():
    while right != 0:
        print(f'right: {right} isCorrect: {isCorrect} \n\n')
        guessedword = typeGuessedLetter(theWord, letters, guessedword)
        print(guessedword)
        guess = input('\nDo you have any guess? if not just tap enter\n')
        if (guess == theWord):
            right = 0
            break
        letter = input('type a letter --> ')
        letters.append(letter)
        right = right - 1
        print(f'\n***remaning right is {right}***\n')


    if  right > 0: 
        print(f'bitch, you lost the word was {theWord}') 
    else: 
        print(f'bitch, you win, congrats')


def printSome():
    print('hey')