
from actions import *
from nlu import *
from intents import *
import sys


context = None

print(getGreeting())
reply = getHelp("")
for term in reply:
    print(term)

while True:
    message = input("User: ")
    action, word = extractInfo(message)

    if action == GETWORDINFO:
        reply = getMeaning(word)
    elif action == GREETING:
        reply = getGreeting()
    elif action == QUIT:
        sys.exit()
    elif action == SYNONYMS:
        reply = getSynonyms(word)
    else:
        reply = dontknow(action)

    if action == GREETING:
        print("WordBot: " + reply)
    else:
        print ("WordBot: "+ ' '.join(reply))
