from importlib.metadata import files
import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, colores, os
from pygame import mixer 

name = "emma"
Listener = sr.Recognizer()
engine = pyttsx3.init()
 
voices =  engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites={
            'google':'google.com',
            'youtube':'youtube.com',
            'facebook':'facebook.com',
            'whatsapp':'whatsapp.com',
            'twitter':'twitter.com',
            'instagram':'instagram.com'

        }
files={
            'mensaje':'Luca.Llop_Mensaje-Oculto.xlsx',
            'unidades':'Luca-Llop_UNIDADES DE ALMACENAMIENTO-Tarea2.docx',
            'evolucion':'SISTEMAS OPERATIVOS - TP N°2 - Evolución de versiones de SO -.docx'

        }

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen(): 
    try: 
        with sr.Microphone() as source: 
            print ("Escuchando...")
            pc = Listener.listen(source) 
            rec = Listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec

def run_emma():
    while True:
        rec = listen() 
        if 'reproduce' in rec: 
            music = rec.replace('reproduce', '')
            print ("Reproduciendo " + music)
            talk ("Reproduciendo" + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca','')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search +": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk("Alarma activada a las " + num + " horas ")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("No mas mimir >:(")
                    mixer.init()
                    mixer.music.load("auronplay-alarma.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif 'colores' in rec:
            talk("Enseguida")
            colores.capture()
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe{sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'abriendo {file}')
        elif 'escribe' in rec:
            try:
                with open("mensaje.xlsx", 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("mensaje.xlsx", 'w')
                write(file)
        elif 'termina' in rec:
            talk('Adios!')
            break
def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)



if __name__ == '__main__': 
    run_emma()
