from nltk.tokenize import sent_tokenize
import random
import tkinter as tk
from gtts import gTTS
import os 
import playsound

def ttm():
	with open(femormasc, 'r') as file:
	    data = file.read()

	z = [i for i in sent_tokenize(data)]

	phrase = random.choice(z)

	narr.configure({"text": phrase})
	tts = gTTS(text =phrase, lang='en')
	filename="DaniTemp.mp3"
	tts.save(filename)    
	playsound.playsound(filename)
	os.remove(filename)


def setfem():
	global femormasc
	femormasc = 'dirtyphrasesf.txt'

def setmasc():
	global femormasc
	femormasc = 'dirtyphrasesm.txt'

window = tk.Tk()
window.title("Dani's Sexy Emporium")

narr = tk.Label(height=40, width=60, text="Ready", relief=tk.SUNKEN, fg="black", bg="white", wraplength=80)
narr.pack(side=tk.TOP)

btn_go = tk.Button(height=5, width=10, text="Go", padx=10, master=window, relief=tk.GROOVE, command=ttm)
btn_go.pack(side=tk.BOTTOM)

btn_f = tk.Button(height=5, width=10, text="Female", padx=10, master=window, relief=tk.GROOVE, command=setfem)
btn_f.pack(side=tk.LEFT)

btn_m = tk.Button(height=5, width=10, text="male", padx=10, master=window, relief=tk.GROOVE, command=setmasc)
btn_m.pack(side=tk.RIGHT)

window.resizable(False,False)
window.wm_iconbitmap('Danicon3.ico')
window.mainloop()