# #Import the required libraries
# from tkinter import *
# import webbrowser
#
# #Create an instance of tkinter frame
# win = Tk()
# win.geometry("750x250")
#
# #Define a callback function
# def callback(url):
#    webbrowser.open_new_tab(url)
#
# #Create a Label to display the link
# link = Label(win, text="Tutorial: www.tutorialspoint.com",font=('Helveticabold', 15), fg="blue", cursor="hand2")
# link.pack()
# link.bind("<Button-1>", lambda e:
# callback("http://www.tutorialspoint.com"))
# win.mainloop()

from tkinter import *
import webbrowser

def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="Google Hyperlink -- soemthing", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

root.mainloop()