import tkinter as tk
import webbrowser # Not Used?
from functools import partial # Used in hyperlinking
from PIL import ImageTk, Image # Used for added image into text
from tkinter import font

root=tk.Tk()
root.title("Testing window")
root.geometry("500x500")

# # Test lambda functions
# def func(thing):
#     print(thing)
#
# cmd = lambda t="SUP": func(t)
#
# button1=tk.Button(text="LEFT",command = cmd)
# button1.pack(side=tk.LEFT)

""" This is my Seperator"""

# Test file read
class HyperlinkManager:
    def __init__(self, text):
        self.text = text
        self.text.tag_config("hyper", foreground="blue", underline=1)
        self.text.tag_bind("hyper", "<Enter>", self._enter)
        self.text.tag_bind("hyper", "<Leave>", self._leave)
        self.text.tag_bind("hyper", "<Button-1>", self._click)
        self.reset()

    def reset(self):
        self.links = {}

    def add(self, action):
        # add an action to the manager.  returns tags to use in
        # associated text widget
        tag = "hyper-%d" % len(self.links)
        self.links[tag] = action
        return "hyper", tag

    def _enter(self, event):
        self.text.config(cursor="hand2")

    def _leave(self, event):
        self.text.config(cursor="")

    def _click(self, event):
        for tag in self.text.tag_names(tk.CURRENT):
            if tag[:6] == "hyper-":
                self.links[tag]()
                return

testFile = open("./texts/test.txt")

myText = tk.Text()
scroll = tk.Scrollbar(cursor="hand2", command=myText.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
myText.config(yscrollcommand=scroll.set)
myText.pack(fill=tk.BOTH, expand=True)

hyperlink = HyperlinkManager(myText)
imgs = []
i=0
for line in testFile:
    if line[0] == "#":
        splitLine = line.split()
        if splitLine[1] == "Hyper":
            myText.insert(tk.END, splitLine[2]+"\n", hyperlink.add(partial(webbrowser.open,splitLine[3])))
        elif splitLine[1] == "Image":

            imgs.append(ImageTk.PhotoImage(Image.open(splitLine[2])))
            myText.image_create(tk.END, image=imgs[i])
            # myText.image_create(tk.END, image=ImageTk.PhotoImage(Image.open(splitLine[2])))
            #i+=1
            myText.insert(tk.END, "\n")

    else:
        myText.insert(tk.END, line)
myText.config(state="disable")

""" This is my Seperator"""

# # Test for image inside text file
# text = tk.Text()
# text.pack(padx = 20, pady = 20, fill=tk.BOTH, expand=True)
# text.insert(tk.END,"WADDUP\n\n")
#
# img = ImageTk.PhotoImage(Image.open("M83 Galaxy.jpg"))
# text.image_create(tk.END, image=img)

""" This is my Seperator"""

# # Test for text widget scrollbar
# text = tk.Text()
# text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# for i in range(100):
#     text.insert(tk.END, "The number " + str(i) + ".\n")
# scroll = tk.Scrollbar(cursor="hand2", command=text.yview)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)
# text['yscrollcommand'] = scroll.set

"""This is my seperator"""

# Accessing variable inside of nested function
# def func():
#     x = 0
#     print(x)
#     x+=1
#     def func2():
#         global x
#         print(x)
#         x+=1
#     func2()
#     x+=1
#     print(x)
#
# func()

"""This is my serperator"""

# textBox = tk.Text(root, font="Times 12", bg="white")
# scrollBar = tk.Scrollbar(textBox, cursor="hand2", command=textBox.yview)
# scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
# textBox.config(yscrollcommand=scrollBar.set)
# textBox.pack(fill=tk.BOTH, expand=True)
#
# fonts = list(font.families())
# print(fonts)
# for f in fonts:
#     # textBox.config(font=f)
#     textBox.tag_configure(f, font=(f, 12))
#     textBox.insert(tk.END, f"{f} - ")
#     textBox.insert(tk.END, f"{f}\n", f)

"""This is my serperator"""

# func = lambda x: x+1
# print(func(5))

"""This is my seperator"""

# # Used to create the Learn page
# def createLearn(self, middle):
#     sections = {"Learn": ["Solar System", "Galaxy", "Universe"],
#                 "Solar System": ["Sun", "Mercury", "Venus", "Earth", "Mars", "Astroid Belt",
#                                  "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Oort Cloud"],
#                 "Galaxy": ["Galaxy", "Super Massive Black Hole", "Black Hole", "White Dwarf", "Neutron Star"],
#                 "Universe": ["Big Bang", "IDK other stuff maybe"]}
#
#     def changePage(s):
#         self.currLearn = s
#         self.createPageStructure(s, lambda m: self.createLearn(m))
#
#     def createLearnButtons():
#         output = []
#         for sec in sections[self.currLearn]:
#             output.append([sec, lambda s=sec: changePage(s)])
#
#         scframe = self.createScrollButton(middle, output)
#         scframe.pack(side=tk.BOTTOM, fill=tk.BOTH, pady=5, expand=True)
#
#     def createLearnText():
#         fileName = self.currLearn.replace(" ", "")
#         self.readTextFile(middle, f"{fileName}.txt")
#
#     def findPreviousPage():
#         for page, pageList in sections.items():
#             if self.currLearn in pageList:
#                 return lambda: changePage(page)
#         return self.backToMain
#
#     if self.currLearn in sections:
#         createLearnButtons()
#     else:
#         createLearnText()
#     return findPreviousPage()
# # End createLearn
# # Used to create the Data page
# def createData(self, middle):
#     sections = {"Data": ["Solar System", "Galaxy", "Universe"],
#                 "Solar System": ["Sun", "Mercury", "Venus", "Earth", "Mars", "Astroid Belt",
#                                  "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Oort Cloud"],
#                 "Galaxy": ["Galaxy", "Super Massive Black Hole", "Black Hole", "White Dwarf", "Neutron Star"],
#                 "Universe": ["Big Bang", "IDK other stuff maybe"]}
#
#     def changePage(s):
#         self.currData = s
#         self.createPageStructure(s, lambda m: self.createData(m))
#
#     output = []
#     for sec in sections[self.currData]:
#         output.append([sec, lambda s=sec: changePage(s)])
#
#     scframe = self.createScrollButton(middle, output)
#     scframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
#     if (self.currData == "Data"):
#         return self.backToMain
#     else:
#         return (lambda: changePage("Data"))
# End createData

root.mainloop()