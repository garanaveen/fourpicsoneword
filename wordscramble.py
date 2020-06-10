#!/usr/bin/python

import argparse

#Dictionary file in MacOs,
DICTIONARY_FILE='/usr/share/dict/words'


def DeleteALetterFromString(character, s):

    l = list(s)  # convert to list
    
    p = l.index(character) 
    del(l[p])         # delete it
    
    s = "".join(l)  # convert back to string
    return s

def DoesWordMeetsAllLetters(word):
    returnValue = True
    allowedLetters = allowedlettersInCAPS
    for i in word:
        if(i.upper() not in allowedLetters):
            #print "Returning False for word", word, "as", i , "not present in ", allowedLetters
            returnValue = False
            break
        else:
            #print "Deleting", i, "from", allowedLetters
            #Delete that character from the allowedString
            allowedLetters = DeleteALetterFromString(i.upper(), allowedLetters)
            #print "After Deleting", i, "NewAllowedLetters is ", allowedLetters

    #print "Returning", returnValue, "for word", word
    return returnValue

def DoesWordMeetsCondition(word):
    if(len(word) == int(args.sizeofword) and DoesWordMeetsAllLetters(word)):
        return True
    else:
        return False

def PrintLinesInFile():
  try:
    f = open(DICTIONARY_FILE)
    try:
        for line in f:
            words = line.split()
            if (words):
                if (True == DoesWordMeetsCondition(words[0])):
                    print words[0]
    finally:
        f.close()
  except IOError:
    print "File : ", DICTIONARY_FILE, " not found"




parser = argparse.ArgumentParser(description='4in1 game parameter parser')
parser.add_argument('--letters', dest='allowedletters', required=True, help='All possible english alphabets (enter without any space)')
parser.add_argument('--size', dest='sizeofword', required=False, help='Size of the word')

args = parser.parse_args()
print "allowedLetters:", args.allowedletters
if args.sizeofword is None: 
   args.sizeofword = len(args.allowedletters)
print "sizeOfWord:", args.sizeofword

allowedlettersInCAPS = args.allowedletters
allowedlettersInCAPS = allowedlettersInCAPS.upper()
print "allowedlettersInCAPS:", allowedlettersInCAPS

PrintLinesInFile()
