import tkinter as tk
BG = "white"
titleFont = ["Times New Roman", 24, "bold underline"]
mainFont = ["Arial CYR", 15]
buttonBG = "light blue"
activeBG = "purple"

def createButton(frame, title, command):
    return tk.Button(frame, text=title, command=command,
                     background=buttonBG, activebackground=activeBG, font=mainFont,
                     cursor="hand2", height=1)