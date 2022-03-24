import tkinter as tk
from equations import AstronomyEquations
from scrollBarTest import VerticalScrolledFrame
from inspect import signature

# Astronomy Class Declaration
class AstronomyInterface:
    # Create the Interface
    def __init__(self):
        self.title = "Astronomy Interface"
        self.mainButtons = ["1) Help",
                            "2) Equation",
                            "3) Data",
                            "4) Learn",
                            "5) Simulation"]
        self.mainFuncs = [self.createHelp,
                          self.createEquation,
                          self.createData,
                          self.createLearn,
                          self.createSimulation]

        # Create the astonromy interface window
        self.window = tk.Tk(className=self.title)
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
        #def createPage(self, title, backFunc, middleFunc):
        #command = lambda i=i, lis2=lis2: self.openEquation(lis2[i])

        buttons = []
        for i in range(len(self.mainButtons)):
            if (self.mainButtons[i] == "5) Simulation"):
                buttons.append(tk.Button(
                    text=self.mainButtons[i],
                    command = lambda title="Simulation", backFunc="createMain", middleFunc="createSim":
                        self.createPage(title, backFunc, middleFunc),
                    height=2, anchor="w"
                ))
            else:
                buttons.append(tk.Button(
                    text=self.mainButtons[i],
                    command=self.mainFuncs[i],
                    height=2, anchor="w"
                ))
            buttons[i].pack(fill=tk.BOTH,
                            expand=True, padx=10, pady=10)
        # End of createMain

    # Used to create the Help page
    def createHelp(self):
        self.destroyWidgets()
        helpLabel = tk.Label(
            text="Welcome to the Astronomy Interface",
            height=2,
            font=("Times 15 bold underline")
        )
        helpLabel.pack(fill=tk.X)

        backButton = tk.Button(
            text="Back",
            command=self.createMain
        )
        backButton.pack(fill=tk.BOTH, expand=True)
        # End createHelp

    # Used to create the Equation Page
    def createEquation(self):
        self.destroyWidgets()
        top = tk.Frame()
        middle = tk.Frame()
        bottom = tk.Frame()
        top.pack(side=tk.TOP)
        middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)

        equationLabel = tk.Label(
            text="Equations List",
            height=2,
            font=("Times 15 bold underline")
        )
        equationLabel.pack(in_=top, fill=tk.X)

        # scrolling = tk.Scrollbar()
        # scrolling.pack(in_=middle, side=tk.RIGHT, fill=tk.Y)
        #
        # mylist = tk.Listbox(self.window, yscrollcommand=scrolling.set, font=("Times 12"))
        # astEq = AstronomyEquations()
        # printEquations = astEq.getAllPrints()
        # for eq in astEq.getAllPrints():
        #     mylist.insert(tk.END, getattr(astEq, eq)())
        #
        # mylist.pack(in_=middle, side=tk.LEFT, fill=tk.BOTH, expand=True)
        # scrolling.config(command=mylist.yview)

        scframe = VerticalScrolledFrame(self.window)
        scframe.pack(in_=middle, fill=tk.BOTH, expand=True)

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

        backButton = tk.Button(
            text="Back",
            command=self.createMain
        )
        backButton.pack(in_=bottom, fill=tk.BOTH,expand=True)
        # End create Equation

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
        middle.grid_rowconfigure(0,weight=1)
        for i, param in enumerate(params):
            print(i)
            paramText = tk.Label(text=param)
            paramText.grid(in_=middle, row=i+1, column=0, padx = 10, pady=5)
            paramEntry = tk.Entry()
            paramEntry.grid(in_=middle, row=i+1, column=1, sticky=tk.EW)

        resultText = tk.Label(text="Result")
        resultText.grid(in_=middle, row=len(params)+1, column=0, padx=10, pady=5)
        resultValue = tk.Entry()
        resultValue.grid(in_=middle, row=len(params)+1, column=1, sticky=tk.EW)

        backButton = tk.Button(
            text="Back",
            command=self.createEquation
        )
        backButton.pack(in_=bottom, fill=tk.BOTH, expand=True)
    # End createEquation


    # Used to create the Data Page
    def createData(self):
        self.destroyWidgets()
        dataLabel = tk.Label(
            text="Data",
            height=2,
            font=("Times 15 bold underline")
        )
        dataLabel.pack(fill=tk.X)

        backButton = tk.Button(
            text="Back",
            command=self.createMain
        )
        backButton.pack(fill=tk.BOTH, expand=True)
        # End createData

    # Used to creat ehe learn page
    def createLearn(self):
        self.destroyWidgets()
        learnLabel = tk.Label(
            text="Learn",
            height=2,
            font=("Times 15 bold underline")
        )
        learnLabel.pack(fill=tk.X)

        backButton = tk.Button(
            text="Back",
            command=self.createMain
        )
        backButton.pack(fill=tk.BOTH, expand=True)
        # End createLearn

    # Used to creat ehe simulation page
    def createSimulation(self):
        self.destroyWidgets()
        simulationLabel = tk.Label(
            text="Simulation",
            height=2,
            font=("Times 15 bold underline")
        )
        simulationLabel.pack(fill=tk.X)

        # Create the simulation
        canvas = tk.Canvas(self.window,
                        width=200, height = 200,
                        bg="black")
        canvas.pack()

        # Creates the back Button
        backButton = tk.Button(
            text="Back",
            command=self.createMain
        )
        backButton.pack(fill=tk.BOTH, expand=True)
        # End createSimulation

    def createSim(self, midFrame):
        # Create the simulation
        canvas = tk.Canvas(width=200, height = 200, bg="black")
        canvas.pack(in_=midFrame)

    # Start of the basic page creation
    def createPage(self, title, backFunc, middleFunc):
        self.destroyWidgets()
        top = tk.Frame()
        middle = tk.Frame()
        bottom = tk.Frame()
        top.pack(side=tk.TOP, fill = tk.X)
        middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)

        topLabel = tk.Label(
            text=title,
            height=2,
            font=("Times 15 bold underline")
        )
        topLabel.pack(in_=top, fill=tk.X)

        # This is where the middle goes
        getattr(self, middleFunc)(middle)
        # End the middle part

        # Creates the back Button
        backButton = tk.Button(
            text="Back",
            command=getattr(self, backFunc)
        )
        backButton.pack(fill=tk.BOTH, expand=True)
        # End createSimulation




# Execution Part
if (__name__ == '__main__'):
    ai = AstronomyInterface()
