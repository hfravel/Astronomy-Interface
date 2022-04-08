import tkinter as tk
from Equations import AstronomyEquations

class VerticalScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kw):
        tk.Frame.__init__(self, parent, *args, **kw)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, cursor="hand2")
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # Allow the scrollwheel to work
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview("scroll", (int)(e.delta / -30), "units"))

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(canvas, bg='white')
        interior_id = canvas.create_window(0, 0, window=self.interior,
                                           anchor=tk.NW)

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if self.interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=self.interior.winfo_reqwidth())

        self.interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if self.interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)

if (__name__ == '__main__'):
    root = tk.Tk()
    root.title("Scrollable Frame Demo")
    root.configure(background="gray99")

    scframe = VerticalScrolledFrame(root)
    scframe.pack()

    astEq = AstronomyEquations()
    lis = astEq.getAstPrints()
    lis2 = astEq.getAstEquations()
    for i, x in enumerate(lis):
        lbl = tk.Label(text="test")
        lbl.grid(in_ = scframe.interior, row=i, column=0)
        btn = tk.Button(height=1, width=20, relief=tk.FLAT,
                        bg="gray99", fg="purple3",
                        font="Dosis", text=getattr(astEq, x)(),
                        command=lambda i=i, x=x: openlink(i))
        #btn.pack(padx=10, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)
        btn.grid(in_= scframe.interior, row=i, column=1)
        #mylist.insert(tk.END, getattr(astEq, eq)())

    def openlink(i):
        print(lis2[i])

    root.mainloop()