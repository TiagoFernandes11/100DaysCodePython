import Constants, random


def chooseRandomWord():
    return Constants.words[random.randint(0, len(Constants.words)-1)]

def generateBoard(word):
    s = ''
    for i in range(len(word)):
        s += '_ '
    return s

word = chooseRandomWord()

board = generateBoard(word)

print(Constants.logo)
print(word)
print(generateBoard(word))

