import tkinter as tk

def mainUI():
    window = tk.Tk()
    greeting = tk.Label(
        text="Astronomy Interface",
        height=2,
        font=("Times 15 bold underline")
    )
    greeting.pack(fill=tk.X)

    helpButton = tk.Button(
        text="1) Help",
        height=2,
        anchor="w",
        padx=10,
        pady=10
    )
    helpButton.pack(fill=tk.X)
    equationButton = tk.Button(
        text="2) Equations",
        height=2,
        anchor="w"
    )
    equationButton.pack(fill=tk.X)
    dataButton = tk.Button(
        text="3) Data",
        height=2,
        anchor="w"
    )
    dataButton.pack(fill=tk.X)
    learnButton = tk.Button(
        text="4) Learn",
        height=2,
        anchor="w"
    )
    learnButton.pack(fill=tk.X)

    window.mainloop()
mainUI()