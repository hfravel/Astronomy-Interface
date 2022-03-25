import tkinter as tk
from equations import AstronomyEquations
from scrollBarTest import VerticalScrolledFrame
from inspect import signature

# Astronomy Class Declaration
class AstronomyInterface:
    # Create the Interface
    def __init__(self):
        self.title = "Astronomy Interface"
        self.mainButtons = ["Help",
                            "Equation",
                            "Data",
                            "Learn",
                            "Simulation"]
        # self.mainFuncs = [self.createHelp,
        #                   self.createEquation,
        #                   self.createData,
        #                   self.createLearn,
        #                   self.createSimulation]

        # Create the astonromy interface window
        self.window = tk.Tk(className=self.title)
        self.window.geometry("500x500")
        self.createMain()
        #self.createEquation()
        self.window.mainloop()
    # End init

    # Clear the window for new page
    def destroyWidgets(self):
        for widget in self.window.winfo_children():
            widget.destroy()
    # End destroyWidgets

    # Creates the main page
    def createMain(self):
        self.destroyWidgets()
        # Create the Astronomy Interface Title
        greeting = tk.Label(
            text=self.title,
            height=2,
            font=("Times 15 bold underline")
        )
        greeting.pack(fill=tk.X)

        # Loops through our list to create the buttons

        buttons = []
        for i in range(len(self.mainButtons)):
            buttons.append(tk.Button(
                text=str(i+1) + ") " + self.mainButtons[i],
                command = lambda pageName=self.mainButtons[i]: self.createPage(pageName, "createMain", "create"+pageName),
                height=2, anchor="w"
            ))
            buttons[i].pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    # End of createMain

    def openEquation(self, eq):
        self.destroyWidgets()
        top = tk.Frame()
        middle = tk.Frame()
        bottom = tk.Frame()
        top.pack(side=tk.TOP, fill = tk.X)
        middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)

        ae = AstronomyEquations()
        topLabel = tk.Label(
        text=getattr(ae, eq[0:len(eq)-8] + "Print")(),
        height=2,
        font=("Times 15 bold underline")
        )
        topLabel.pack(in_=top, fill=tk.X)

        params = signature(getattr(ae, eq)).parameters
        middle.grid_columnconfigure(1,weight=1)
        for i, param in enumerate(params):
            #middle.grid_rowconfigure(i, weight=1)
            paramText = tk.Label(text=param)
            paramText.grid(in_=middle, row=i, column=0, padx = 10, pady=5)
            paramEntry = tk.Entry()
            paramEntry.grid(in_=middle, row=i, column=1, padx=10, sticky="NEW")

        resultText = tk.Label(text="Result")
        resultText.grid(in_=middle, row=len(params), column=0, padx=10, pady=5)
        resultValue = tk.Entry()
        resultValue.grid(in_=middle, row=len(params), column=1, padx=10, sticky=tk.EW)

        backButton = tk.Button(
            text="Back", height=2,
            command=lambda: self.createPage("Equation", "createMain", "createEquation")
        )
        backButton.pack(in_=bottom, fill=tk.BOTH, expand=True)
    # End openEquation

    # Start of the basic page creation
    def createPage(self, title, backFunc, middleFunc):
        self.destroyWidgets()
        top = tk.Frame()
        middle = tk.Frame()
        bottom = tk.Frame()
        top.pack(side=tk.TOP, fill = tk.X)
        middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)

        # This is where the middle goes
        getattr(self, middleFunc)(middle)
        # End the middle part

        topLabel = tk.Label(
            text=title,
            height=2,
            font=("Times 15 bold underline")
        )
        topLabel.pack(in_=top, fill=tk.X)

        # Creates the back Button
        backButton = tk.Button(
            text="Back", height=2,
            command=getattr(self, backFunc)
        )
        backButton.pack(in_=bottom, fill=tk.X, expand=True)
    # End createPage

    # Used to create the Help page
    def createHelp(self, middle):
        print("Help")
    # End createHelp

    # Used to create the Equation page
    def createEquation(self, middle):
        scframe = VerticalScrolledFrame(middle)
        scframe.pack(in_=middle, side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        astEq = AstronomyEquations()
        lis = astEq.getAllPrints()
        lis2 = astEq.getAllEquations()
        scframe.interior.grid_rowconfigure(0,weight=1)
        scframe.interior.grid_columnconfigure(0,weight=2)
        scframe.interior.grid_columnconfigure(1,weight=3)
        for i, x in enumerate(lis):
            lblbtn = getattr(astEq, x)()
            lbl = tk.Label(text=lblbtn[0])
            lbl.grid(in_=scframe.interior, row=i, column=0, pady=15,padx=5,sticky=tk.EW)

            btn = tk.Button(height=1, width=20, relief=tk.FLAT,
                            bg="gray99", fg="purple3",
                            font="Dosis", text=lblbtn[1],
                            command=lambda i=i, lis2=lis2: self.openEquation(lis2[i]))
            #btn.pack(padx=10, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)
            btn.grid(in_=scframe.interior, row=i, column=1, sticky=tk.EW)

        btn=tk.Button(text="Switch View Button")
        btn.pack(in_=middle, side=tk.TOP,fill=tk.X)
    # End createEquation

    # Used to create the Data page
    def createData(self, middle):
        print("Data")
    # End createData

    # Used to create the Learn page
    def createLearn(self, middle):
        print("Learn")
    # End createLearn

    # Used to create the Simulation page
    def createSimulation(self, middle):
        canvas = tk.Canvas(width=200, height = 200, bg="black")
        canvas.pack(in_=middle)
    # End createSimulation


# Execution Part
if (__name__ == '__main__'):
    ai = AstronomyInterface()
