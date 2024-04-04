import cv2
import subprocess #for opening calc

##module for the voice assistant
import speech_recognition as sr
import pyttsx3
import webbrowser
#module for the voice assistant


cap = cv2.VideoCapture(0)

from cvzone.HandTrackingModule import HandDetector

handDetector = HandDetector()

import os

import time

while True:
    status , photo = cap.read()
    findHand = handDetector.findHands(photo , draw=True)
    
    if findHand[0]:
        mylmlist = findHand[0][0]
        myfingerup  = handDetector.fingersUp(mylmlist)
    
        if myfingerup == [ 1,1,1,1,1]:
            print("i m all ok 5 five finger up")
            os.system(("shutdown /l /t 0"))            
            time.sleep(2)
        elif myfingerup == [ 0,1,0,0,0]:
            print("One finger")
            os.system("chrome")
            time.sleep(2)    
        elif myfingerup == [ 0, 1, 1, 0 ,0]:
            print("2 finger up")
            os.system("notepad")
            time.sleep(2)
        elif myfingerup == [ 0, 1, 1, 1 ,0]:
            print("3 finger up")
            subprocess.Popen('calc.exe')
            time.sleep(2)
        elif myfingerup == [ 0, 1, 1, 1 ,1]:

            # Initialize Text-to-Speech engine
            engine = pyttsx3.init()
            
            # Function to speak text
            def speak(text):
                engine.say(text)
                engine.runAndWait()
            
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
            speak("Hello Samir sir I am your assistant")
            speak("How may I help you?")
            query = listen()
            if query: # Perform Google search
                search_url = "https://www.google.com/search?q=" + query.replace(" ", "+")
                webbrowser.open(search_url)
                speak("opening the google chrome")
                speak("Here are the search results for " + query)
                speak("Goodbye sir, have a nice day!")
            break            
        else:
            print("idk")
    
    
    cv2.imshow("myphoto"  ,  photo)
    if cv2.waitKey(100) == 13:
        break
        
        
cv2.destroyAllWindows()

cap.release()
