# pip install pyttsx3 
# for text to speech

import pyttsx3

if __name__ == '__main__' :
    text_speech = pyttsx3.init()
    print("Welcome to RoboSpeaker")
    print("Press 'q' to quit")
    while True:
        answer = input("What you want to convert to speech : ")
        if answer == "q":
            text_speech.say("bye bye my friend")
            text_speech.runAndWait()
            break
        text_speech.say(answer)
        text_speech.runAndWait()
