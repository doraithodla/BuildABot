from nltk.corpus import wordnet
from intents import *
from help import help_text
from botdata import *
from random import randint

def getMeaning(word):
    syns = wordnet.synsets(word)
    try:
        return [syns[0].definition()]
    except IndexError:
        return ["Can't find the word"]


def getSynonyms(word):
    synonyms = []
    #print('insyn:'+word)
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms

def getAntonym(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return list(set(antonyms))

def getHelp(context):
    return [help_text]

def dontknow(action):
    return["Sorry. I don't understand %s" % action]

def getGreeting():
    return BOT_RESPONSES[randint(0,len(BOT_RESPONSES)-1)]

if __name__ == "__main__":
    print(getSynonyms("exotic"))
    print(getSynonyms("set"))
    print(getSynonyms("excellent"))
