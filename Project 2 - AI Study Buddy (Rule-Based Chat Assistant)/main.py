# Rule based AI chatbot

import datetime
import time

name = input("Welcome , Enter your name :- ")
presentHour= datetime.datetime.now().hour

if 5<=presentHour <=11:
    print("Good Morning , " , name)
elif 11<= presentHour <=17:
    print("Good Afternoon , " , name)
elif 17<= presentHour <=20:
    print("Good Evening , " , name)
else:
    print("Good Night , " , name)

print("Namaste ! Welcome to Your ChatBot")
print("You can ask me basic question, Type 'Bye' to exit from the bot")

# Chatbot Memory Creation [ dictionary of responses]

responses = {
    "hello": "Hi, Welcome.How can I help you?",
    "how are you" : "I am very fine.Thank you",
    "who are you" : "I am smart AI chatbot",
    "motivate me" : "Keep going.Every bug of your project makes you a better deleloper",
    "happy":"Great to hear that",
    "functions kya hote hai": "jakar chapter 7 padho",
    "bye":"bye , see you soon"
}

# Method/Function to get response of ChatBot

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am not able to tell that yet. I am still in learning mode"

# Take user input

while True:
    userInput = input("Please ask your question :- ")
    reply=getResponseBot(userInput)
    print("bot Response :- " , reply)

    if "bye" in userInput.lower():
        break