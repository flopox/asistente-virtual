from cProfile import label
from importlib.metadata import files
from tkinter import font
import speech_recognition as sr         #pip install speechrecognition
import subprocess as sub
import pyttsx3                          #pip install pyttsx3
import pywhatkit                        #pip install pywhatkit
import wikipedia                        #pip install wikipedia
import datetime                         #pip install datetime
import keyboard                         #pip install keyboard
import colores
import os
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer                #pip install pygame
import threading as tr

main_window = Tk()
main_window.title("emma AI")

main_window.geometry("800x500")
main_window.resizable(0,0)
main_window.configure(bg='#1EA274')

comandos =  """
            - Reproduce...
            - Busca...
            - Abre...
            - Alarma...
            - Archivo...
            - Colores...
            - Termina...
            """

label_title = Label(main_window, text="Emma IA", bg= "#C4E0E5", fg="#373B44",
                            font=('Times New Roman', 30, 'bold'))
label_title.pack(pady= 10)

canvas_comandos = Canvas(bg= "#6be585", height=450, width=200)
canvas_comandos.place(x=0, y=0)
canvas_comandos.create_text(90, 80, text= comandos, fill="#434343", font= 'Times New Roman')

text_info = Text(main_window, bg="6be585", fg="434334")
text_info.place(x=0, y=180, height= 280, width= 195)

emma_photo = ImageTk.PhotoImage(Image.open("emma-prototipo.jpeg"))
window_photo = Label(main_window, image=emma_photo)
window_photo.pack(pady= 5)

def mexican_voice():
    change_voice(0)
    pass
def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145) 

name = "Emma"
Listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites = dict()
files = dict()
programas = dict()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def leeyresponde():
    text= text_info.get("1.0", "end")
    talk(text)

def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)

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
            talk(wiki)
            write_text(search + ": " + wiki)
            break

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

def open_w_files():
    window_files = Toplevel()
    window_files.title("Agrega archivos:")
    window_files.configure(bg="#434343")
    window_files.geometry("300x200")
    window_files.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow{str(window_files)}center')

    title_label = Label(window_files, text="Agrega una archivo: ", fg="white", bg="#434343", font=('Arial', 15, 'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_files, text="Nombre del archivo: ", fg="white", bg="#434343", font=('Arial', 10, 'bold'))
    name_label.pack(pady=2)

    namefile_entry = Entry(window_files, width=35)
    namefile_entry.pack(pady=1)

    save_button = Button(window_files, text="Guardar", bg="white", width=8, height=1)
    save_button.pack(pady=4)
def open_w_apps():
    pass
def open_w_pages():
    pass

button_voice_mx = Button(main_window, text="Voz Mexico", fg="white", bg="#24FE41",
                            font=("Times New Roman", 14, "bold"), command=mexican_voice)
button_voice_mx.place(x=400, y=100, width=100, height=300)

button_listen = Button(main_window, text="Escuchar", fg="white", bg="#134E5E",
                        font=("Times New Roman", 15, "bold"),width=120, command=run_emma)
button_listen.pack(pady=10)

button_speak_mx = Button(main_window, text="Hablar", fg="white", bg="#00e0f0",
                            font=("Times New Roman", 14, "bold"), command=leeyresponde)
button_speak_mx.place(x=400, y=200, width=100, height=300)


button_add_files = Button(main_window, text="Agregar archivos", fg="white", bg="#00e0f0",
                            font=("Times New Roman", 14, "bold"), command=open_w_files)
button_add_files.place(x=400, y=240, width=120, height=300)
button_add_apps = Button(main_window, text="Agregar apps", fg="white", bg="#00e0f0",
                            font=("Times New Roman", 14, "bold"), command=open_w_apps)
button_add_apps.place(x=400, y=280, width=120, height=300)
button_add_pages = Button(main_window, text="Agregar paginas", fg="white", bg="#00e0f0",
                            font=("Times New Roman", 14, "bold"), command=open_w_pages)
button_add_pages.place(x=400, y=320, width=120, height=300)


main_window.mainloop()