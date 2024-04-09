#Final code for the AI Camera

import cv2
import subprocess #for opening calc
import os
import time
##module for the voice assistant
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
#module for the voice assistant


cap = cv2.VideoCapture(0)

from cvzone.HandTrackingModule import HandDetector

handDetector = HandDetector()

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    current = datetime.now()
    hour = current.hour  # Extract the hour directly from the datetime object
    print(f'Time is {current}')
    if 1 <= hour < 12:
        print("Good Morning Sir!")
        speak("Good Morning Sir")
    elif 12 <= hour < 16:
        print('Good Afternoon')
        speak("Good Afternoon Sir")
    elif 16 <= hour < 21:
        print('Good Evening')
        speak("Good Evening Sir")
    else:
        print("Good Night")
        speak("Good Night Sir")




while True:
    status , photo = cap.read()
    findHand = handDetector.findHands(photo , draw=True)
    
    if findHand[0]:
        mylmlist = findHand[0][0]
        myfingerup  = handDetector.fingersUp(mylmlist)
    
        if myfingerup == [ 1,1,1,1,1]:
            speak("i m all ok 5  finger up")
            time.sleep(2)
        elif myfingerup == [ 0,1,0,0,0]:
            print("One finger")
            speak("Opening chrome")
            os.system("chrome")
            time.sleep(2)    
        elif myfingerup == [ 0, 1, 1, 0 ,0]:
            print("2 finger up")
            speak("opening notepad")
            os.system("notepad")
            time.sleep(2)
        elif myfingerup == [ 0, 1, 1, 1 ,0]:
            print("3 finger up")
            speak("opening the calculator ")
            subprocess.Popen('calc.exe')
            time.sleep(2)
        elif myfingerup == [ 0, 1, 1, 1 ,1]:

          
            
            # Function to listen to user input
            def listen():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                
                try:
                    print("Recognizing...")
                    query = r.recognize_google(audio)
                    print("You said:", query)
                    return query
                except sr.UnknownValueError:
                    print("Sorry, I didn't understand.")
                    return ""
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
                    return ""
            
            # Say "Hello sir"
            greet()
            speak(" I am your assistant")
            speak("How may I help you?")
            query = listen()
            if query: # Perform Google search
                search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")
                webbrowser.open(search_url)
                speak("opening the google chrome")
                speak("Here are the search results for " + query)
                speak("Goodbye sir, have a nice day!")
                           
        else:
            print("idk")
    
    
    cv2.imshow("myphoto"  ,  photo)
    if cv2.waitKey(100) == 13:
        break
        
        
cv2.destroyAllWindows()

cap.release()
