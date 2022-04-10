import tkinter as tk
import webbrowser # Not Used?
from functools import partial # Used in hyperlinking
from PIL import ImageTk, Image # Used for added image into text

# root=tk.Tk()
# root.title("Testing window")
# root.geometry("500x500")

# # Test lambda functions
# def func(thing):
#     print(thing)
#
# cmd = lambda t="SUP": func(t)
#
# button1=tk.Button(text="LEFT",command = cmd)
# button1.pack(side=tk.LEFT)

""" This is my Seperator"""

# # Test file read
# class HyperlinkManager:
#     def __init__(self, text):
#         self.text = text
#         self.text.tag_config("hyper", foreground="blue", underline=1)
#         self.text.tag_bind("hyper", "<Enter>", self._enter)
#         self.text.tag_bind("hyper", "<Leave>", self._leave)
#         self.text.tag_bind("hyper", "<Button-1>", self._click)
#         self.reset()
#
#     def reset(self):
#         self.links = {}
#
#     def add(self, action):
#         # add an action to the manager.  returns tags to use in
#         # associated text widget
#         tag = "hyper-%d" % len(self.links)
#         self.links[tag] = action
#         return "hyper", tag
#
#     def _enter(self, event):
#         self.text.config(cursor="hand2")
#
#     def _leave(self, event):
#         self.text.config(cursor="")
#
#     def _click(self, event):
#         for tag in self.text.tag_names(tk.CURRENT):
#             if tag[:6] == "hyper-":
#                 self.links[tag]()
#                 return
#
# testFile = open("test.txt")
#
# myText = tk.Text()
# scroll = tk.Scrollbar(cursor="hand2", command=myText.yview)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)
# myText.config(yscrollcommand=scroll.set)
# myText.pack(fill=tk.BOTH, expand=True)
#
# hyperlink = HyperlinkManager(myText)
# imgs = []
# i=0
# for line in testFile:
#     if line[0] == "#":
#         splitLine = line.split()
#         if splitLine[1] == "Hyper":
#             myText.insert(tk.END, splitLine[2]+"\n", hyperlink.add(partial(webbrowser.open,splitLine[3])))
#         elif splitLine[1] == "Image":
#             imgs.append(ImageTk.PhotoImage(Image.open(splitLine[2])))
#             myText.image_create(tk.END, image=imgs[i])
#             i+=1
#             myText.insert(tk.END, "\n")
#
#     else:
#         myText.insert(tk.END, line)
# myText.config(state="disable")

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

#root.mainloop()