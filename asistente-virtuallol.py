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