import tkinter

master=tkinter.Tk()
master.title("pack() method")
master.geometry("450x350")

def func(thing):
    print(thing)

cmd = lambda t="SUP": func(t)

button1=tkinter.Button(master, text="LEFT",
             command = cmd)
button1.pack(side=tkinter.LEFT)

master.mainloop()