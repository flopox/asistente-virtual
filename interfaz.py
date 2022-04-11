from importlib.metadata import files
from tkinter import font
import speech_recognition as sr
import subprocess as sub
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import colores
import os
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import threading as tr

main_window = Tk()
main_window.title("emma AI")

main_window.geometry("800x500")
main_window.resizable(0,0)
main_window.configure(bg='#4286f4')

comandos = """
            - Reproduce...
            - Busca...
            - Abre...
            - Alarma...
            - Archivo...
            - Colores...
            - Termina...
"""

label_title = Label(main_window, text="Emma AI", bg= "#C4E0E5", fg="#373B44",
                            font=('Times New Roman', 30, 'bold'))
label_title.pack(pady= 10)

canvas_comandos = Canvas(bg= "#6be585", height=450, width=200)

emma_photo = ImageTk.PhotoImage(Image.open("emma-prototipo.jpeg"))
window_photo = Label(main_window, image=emma_photo)
window_photo.pack(pady= 5)

def mexican_voice():
    change_voice(0)
    pass
def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145) 

name = "emma"
Listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites = {
    'google': 'google.com',
    'youtube': 'youtube.com',
    'facebook': 'facebook.com',
    'whatsapp': 'whatsapp.com',
    'twitter': 'twitter.com',
    'instagram': 'instagram.com'

}
files = {
    'mensaje': 'Luca.Llop_Mensaje-Oculto.xlsx',
    'unidades': 'Luca-Llop_UNIDADES DE ALMACENAMIENTO-Tarea2.docx',
    'evolucion': 'SISTEMAS OPERATIVOS - TP N°2 - Evolución de versiones de SO -.docx'

}
programas = {
    'chrome': r"C:\Program Files\Google\Chrome\Application",
    'visual': r"C:\Program Files\Microsoft VS Code",
    'word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
}


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
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
            print("Reproduciendo " + music)
            talk("Reproduciendo" + music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
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
            for app in programas:
                if app in rec:
                    talk(f'Abriendo {app}')
                    os.startfile(programas[app])

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

button_voice_mx = Button(main_window, text="Voz Mexico", fg="white", bg="#24FE41",
                            font=("Times New Roman", 14, "bold"), command=mexican_voice)
button_voice_mx.place(x=400, y=100, width=100, height=300)

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#134E5E",
                        font=("Times New Roman", 15, "bold"),width=120, command=run_emma)
button_listen.pack(pady=10)

main_window.mainloop()