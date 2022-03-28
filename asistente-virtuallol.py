from multiprocessing.connection import Listener
from sys import _enablelegacywindowsfsencoding
import speech_recognition as sr
import pyttsx3, pywhatkit

name = "maría"
Listener = sr.Recognizer()
engine = pyttsx3.init()
 
voices =  engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
for i in voices :
    print (i)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen(): 
    try: 
        with sr.Microphone() as source: 
            print ("Escuchando...")
            pc = Listener.listen(source) 
            rec = Listener.recognize_google(pc)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec

def run_maría():
    rec = listen() 
    if ' reproduce ' in rec: 
        music = rec.replace('reproduce', '')
        print ("reproduciendo..." + music)
        talk ("reproduciendo..." + music)
        pywhatkit.playonyt(music)
if __name__ == '__main__': 
    run_maría()
    