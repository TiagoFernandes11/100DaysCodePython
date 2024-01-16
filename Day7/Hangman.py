import Constants, random

lives = 6
tryedLetters = []

def chooseRandomWord():
    return Constants.words[random.randint(0, len(Constants.words)-1)]

def renderBoard(word, letter_list):
    print(Constants.stages[lives])
    s = ''
    for i in range(len(word)):
        if word[i] in letter_list:
            s += word[i] + " "
        else:
            s += '_ '
    print(s + "\n")

def addUserLetterInput():
    global lives, word
    inputLetter = input("Guess a letter: ")
    if len(inputLetter) > 1:
        print("Only one letter")
    else:
        tryedLetters.append(inputLetter)
        if word.find(inputLetter) < 0:
            lives -= 1

word = chooseRandomWord()

print(Constants.logo)

def game():
    while lives > 0:
        renderBoard(word, tryedLetters)
        addUserLetterInput()
        if lives == 0:
            print(Constants.stages[0])
            print("Game over")


game()

