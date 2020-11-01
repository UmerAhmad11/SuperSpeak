import tkinter as tk
from tkinter import *
from gtts import gTTS
import os
import playsound
from PIL import ImageTk, Image
import win32gui
import pyautogui
from tkinter import messagebox
import speech_recognition as sr
from translate import Translator

window = tk.Tk()
window.title("Super Speak!")
window.geometry("450x220")
window.configure(bg="grey")
window.iconbitmap('c:/Users/SALMAN/Downloads/winshow.ico')

img = ImageTk.PhotoImage(Image.open('oki.png'))
panel = tk.Label(window, image = img)
panel.place(x=125, y=0)

def func_orig1(value):
    global ok
    ok = value
    print(ok)
    
var_orig1 = StringVar(window)
var_orig1.set("Language")

c_1 = OptionMenu(window, var_orig1, "en", "fr", "zh-cn", "es", "pt", "en-au", command=func_orig1)
c_1.config(width=10)
c_1.place(x=0, y=0)

def func_orig2(value):
    global obt
    obt = value
    print(obt)
    
var_orig2 = StringVar(window)
var_orig2.set("Translation To")

c_2 = OptionMenu(window, var_orig2, "en", "fr", "zh", "es", "pt", "la", "ur", "ar", command=func_orig2)
c_2.config(width=15)
c_2.place(x=300, y=50)

def func_orig3(value):
    global ott
    ott = value
    print(ott)
    
var_orig3 = StringVar(window)
var_orig3.set("Translation From")

c_3 = OptionMenu(window, var_orig3, "en", "fr", "zh", "es", "pt", "la", "ur", "ar", command=func_orig3)
c_3.config(width=15)
c_3.place(x=300, y=0)


def speak():
    filename = t.get()[0] + ".mp3"
    mytext = t.get()
    language = ok
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
   
def get_audio():
    t.delete(0, tk.END)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        said = r.recognize_google(audio)
        t.insert(0, said)

def trans():
    language1 = obt
    language2 = ott
    translator = Translator(to_lang=language1, from_lang=ott)
    transl = translator.translate(t.get())
    t.delete(0, tk.END)
    t.insert(0, transl)
        

t = tk.Entry(window, bd=5)
button = tk.Button(window, text="Speak", width=20, height=1, command=speak).place(x=100, y=160)
but = tk.Button(window, text="Write", width=20, height=1, command=get_audio).place(x=100, y=130)
butt = tk.Button(window, text="Translate", width=20, height=1, command=trans).place(x=100, y=190)


t.place(x=108, y=100)
window.mainloop()