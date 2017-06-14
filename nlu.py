'''
NLU - (An apology for a) Natural Language Understanding Module
'''

from intents import *

def getCommand(word):
    if word in ['define','whatis']:
        return (GETWORDINFO)
    elif word in ['quit','q','exit']:
        return (QUIT)
    elif word in ['alternates', 'synonyms']:
        return (SYNONYMS)
    else:
        return (HELP)
def extractInfo(text):
    if len(text):
        wordlist = text.split()
        if len(wordlist) > 1:
            return(getCommand(wordlist[0]),wordlist[1])
        else:
            return (getCommand(wordlist[0]), "")
    else:
        return(EMPTYSTRING,"")

if __name__ == "__main__":
    print(extractInfo("define exotic"))
    print(extractInfo("synonyms exotic"))
    print(extractInfo("help "))
    print(extractInfo(""))
