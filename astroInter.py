import tkinter as tk

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
        self.buttons = []
        for i in range(len(self.mainButtons)):
            self.buttons.append(tk.Button(
                text=self.mainButtons[i],
                command=self.mainFuncs[i],
                height=2, anchor="w"
            ))
            self.buttons[i].pack(fill=tk.BOTH,
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
        equationLabel = tk.Label(
            text="Equations List",
            height=2,
            font=("Times 15 bold underline")
        )
        equationLabel.pack(fill=tk.X)

        backButton = tk.Button(
            text="Back",
            command=self.createMain
        )
        backButton.pack(fill=tk.BOTH, expand=True)
        # End create Equation

    # Used to create the Data Page
    def createData(self):
        self.destroyWidgets()
        dataLabel = tk.Label(
            text="Equations List",
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

        # Create the canvas
        canvas = tk.Canvas(self.window,
                        width=200, height = 200,
                        bg="black")
        canvas.pack()

        backButton = tk.Button(
            text="Back",
            command=self.createMain
        )
        backButton.pack(fill=tk.BOTH, expand=True)
        # End createSimulation



# Execution Part
ai = AstronomyInterface()
