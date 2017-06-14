# BuildABot
Build a chatbot

We build a rudimentary chatbot using simple rules (if-then-else statements). As we progress through versions, we will start leveraging NLU. 

This chatbot does not parse Natural language and works on a fixed command structure - <command> <parameter>
The command can be a list of predefined set of keywords and their synonyms
The parameter is the word whose meaning or synonyms you are trying to get

The organization of the chatbot is pretty simple:

A command line loop gets input from user, decodes the command, triggers an action and responds to the user from the reply sent from the action. For example:

whatis set

a. checks whether 'whatis' is a valid command and maps it to an id 

b. The id is used to dispatch to an action routine

c. The action routine responds with a result 

d. The result is displayed to the user

