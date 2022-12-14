import tkinter as tk
from tkinter import *
import pyttsx3

engine = pyttsx3.init()

root = Tk()

def speakNow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()
def Reset():
    text.delete(0,END)

textv=StringVar()
obj=LabelFrame(root, text="Text To speech", font=20, bd=1,highlightcolor="gray", bg="#2d2d2d",fg="white")
obj.pack(fill="both", expand="yes", padx=10, pady=10)

lb1=Label(obj, text="Text", font=30, bg="#2d2d2d",fg="white")
lb1.pack(side=tk.LEFT, padx=5)

text=Entry(obj, textvariable=textv, font=20,width=40, bd=2)
text.pack(side=tk.LEFT, padx=10)

btn=Button(obj, text="Speech", bg="lightgreen", command=speakNow,bd=5, fg="black", width=15)
btn.pack(side=tk.LEFT, padx=10)
btn_reset = Button(obj, bd=5, fg="black",  bg="lightblue", width=10, text="Reset" , command=Reset)
btn_reset.pack(side=tk.LEFT, padx=10)
root.title("Text To speech")
root.geometry("800x300")
root.resizable(False, False)
root.mainloop()