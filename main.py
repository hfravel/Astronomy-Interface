import tkinter as tk

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

button = tk.Button(
    text="Other SUP",
    width=25, height=2,
    fg="purple", bg="yellow"
)
button.pack(fill=tk.X)

window.mainloop()
