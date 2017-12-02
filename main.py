#xkcd password generator, with special characters
#link to original xkcd:
#https://xkcd.com/936/
#made by: Lachi Balabanski
import random
def getWordArray():
    wordArray = []
    fi = open('uncommonwords.txt','r')
    for i in fi:
        wordArray.append(i)
    temp = wordArray[0]
    realWordArray = temp.split(',')
    return realWordArray
def getRandWordsArray(wordArray,numWords):
    randWords = []
    for i in range(0,numWords):       
        randWords.append(wordArray[random.randint(0,len(wordArray) - 1)])
    return randWords
def modifyPassArray(wordArray,otherArray):
    wordstr = ''.join(wordArray)
    specialChar = otherArray[random.randint(0,len(otherArray) - 1)]
    position = random.randint(0,len(wordArray))
    return(wordstr[:position] + specialChar + wordstr[position:])
specialChars = ['!','@','#','$','%','^','&','*','_','-','=','+','/','?','.','~',"'",'"']
words = getWordArray()
numWords = input("How many words would you like in your password? reccomended: 3-4 ")
done = False
while done != True:
    numWords = int(numWords)
    x = getRandWordsArray(words,numWords)
    finalPass = modifyPassArray(x,specialChars)
    print(finalPass)
    satisfied = input("Are you satisfied with this password? [y/n] ")
    if satisfied.lower() == 'y':
        print("Your password is: " + finalPass)
        done = True
