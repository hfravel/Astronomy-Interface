import Tkinter as tk

window = tk.Tk()

greeting = tk.Label(
    text="SUP",
    fg='pink', bg='black',
    width=25, height=2)
greeting.pack(fill=tk.X)

entry = tk.Entry(
    fg="green", bg="blue",
    width=25
)
entry.pack(fill=tk.X)

button1 = tk.Button(
    text="Other SUP",
    width=25, height=2,
    fg="purple", bg="yellow"
)
button1.pack(fill=tk.X)

button2 = tk.Button(
    text="Other SUP",
    width=25, height=2,
    fg="purple", bg="yellow"
)
button2.pack(fill=tk.X)

window.mainloop()
