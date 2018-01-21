#xkcd password generator, with special characters
#link to original xkcd:
#https://xkcd.com/936/
#made by: Lachi Balabanski
import random
import argparse
p = argparse.ArgumentParser()
p.add_argument('-n','--number', required=True, help='number of words in password', type=str)
arguments = p.parse_args()
numWords = int(arguments.number)
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
numWords = int(numWords)
x = getRandWordsArray(words,numWords)
finalPass = modifyPassArray(x,specialChars)
print(finalPass)
