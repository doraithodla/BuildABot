
from actions import *
from nlu import *
from intents import *
import sys

def print_greeting_help():
    print("Hello, Welcome to WordBot")
    reply = getHelp("")
    for term in reply:
        print(term)
context = None

print_greeting_help()
while True:
    message = input("User ::  ")
    action, word = extractInfo(message)

    if action == GETWORDINFO:
        reply = getMeaning(word)
    elif action == QUIT:
        sys.exit()
    elif action == SYNONYMS:
        #print(action, word)
        reply = getSynonyms(word)
    else:
        reply = dontknow(word)

    print("WordBot  ::")
    print(' '.join(reply))

    #print(reply)
