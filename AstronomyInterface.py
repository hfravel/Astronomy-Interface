import tkinter as tk
from Equations import AstronomyEquations
from VerticalScrolledFrame import VerticalScrolledFrame
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
        self.ae = AstronomyEquations()
        self.backToMain = lambda: self.createPage(self.title, "", "createMain")
        self.backToEqua = lambda: self.createPage("Equation", self.backToMain, "createEquation")

        # Create the astonromy interface window
        self.window = tk.Tk(className=self.title)
        self.window.geometry("500x500")
        self.createPage(self.title, "", "createMain")
        self.window.mainloop()
    # End init

    # Clear the window for new page
    def destroyWidgets(self):
        for widget in self.window.winfo_children():
            widget.destroy()
    # End destroyWidgets

    # Creates the main page
    def createMain(self, middle):
        btnNum = 1
        for mainBtn in self.mainButtons:
            currButton = tk.Button(
                text=str(btnNum) + ") " + mainBtn,
                command = lambda pageName=mainBtn:
                    self.createPage(pageName, self.backToMain, "create"+pageName),
                height=2, anchor="w"
            )
            currButton.pack(in_=middle,fill=tk.BOTH, expand=True, padx=10, pady=10)

            btnNum+=1
    # End of createMain

    # Start of the basic page creation
    def createPage(self, title, backFunc, middleFunc, eq=""):
        self.destroyWidgets()
        top = tk.Frame()
        middle = tk.Frame()
        bottom = tk.Frame()
        top.pack(side=tk.TOP, fill = tk.X)
        middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)

        # This is where the middle goes
        if eq=="":
            getattr(self, middleFunc)(middle)
        else:
            getattr(self, middleFunc)(middle, eq)
        # End the middle part

        topLabel = tk.Label(
            text=title,
            height=2,
            font=("Times 15 bold underline")
        )
        topLabel.pack(in_=top, fill=tk.X)

        # Creates the back Button
        if middleFunc != "createMain":
            backButton = tk.Button(
                text="Back", height=2,
                command=backFunc
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

        scframe.interior.grid_rowconfigure(0,weight=1)
        scframe.interior.grid_columnconfigure(0,weight=2)
        scframe.interior.grid_columnconfigure(1,weight=3)

        currRow = 0
        # Create physics equation buttons in scrollframe
        currRow = self.addEquationsToFrame(scframe.interior, "Physics Equations", currRow)
        # Create astronomy equation buttons in scrollframe
        currRow = self.addEquationsToFrame(scframe.interior, "Astronomy Equations", currRow)

        switchButton=tk.Button(text="Switch View Button")
        switchButton.pack(in_=middle, side=tk.TOP,fill=tk.X)
    # End createEquation

    # Adds the equationType to scrollFrame starting at currRow
    # If equationType = "Physics Equations" add physics equations to scrollFrame
    # Else add astronomy equations to scrollFrame
    def addEquationsToFrame(self, scrollFrame, equationType, currRow):
        equations=[]
        prints=[]
        if (equationType == "Physics Equations"):
            equations = self.ae.getPhyEquations()
            prints = self.ae.getPhyPrints()
        else:
            equations = self.ae.getAstEquations()
            prints = self.ae.getAstPrints()

        typeLabel = tk.Label(
            text=equationType,
            height=2,
            font=("Times 15 bold underline")
        )
        typeLabel.grid(in_=scrollFrame, row=currRow, column=0, pady=15, padx=5, columnspan=2, sticky=tk.EW)
        currRow+=1

        for i in range(len(equations)):
            aboutEquation = getattr(self.ae, prints[i])()
            equationName = tk.Label(text=aboutEquation[0])
            equationName.grid(in_=scrollFrame, row=currRow, column=0, pady=15,padx=5,sticky=tk.EW)

            equationButton = tk.Button(height=1, width=20, relief=tk.FLAT,
                            bg="gray99", fg="purple3",
                            font="Dosis", text=aboutEquation[1],
                            command=lambda pr=getattr(self.ae, prints[i])(), eq=equations[i]:
                                self.createPage(pr[1], self.backToEqua, "openEquation", eq))
            #btn.pack(padx=10, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)
            equationButton.grid(in_=scrollFrame, row=currRow, column=1, sticky=tk.EW)
            currRow+=1

        return currRow
    # End addEquationsToFrame

    # Opens a specific a page for a specific equation
    def openEquation(self, middle, eq):
        printEq = getattr(self.ae, eq[0:len(eq)-8] + "Print")()

        middle.grid_columnconfigure(1,weight=1)
        paramEntries = []
        rowNum = 0
        for param in printEq[2]:
            paramText = tk.Label(text=param)
            paramText.grid(in_=middle, row=rowNum, column=0, padx = 10, pady=5)
            paramEntries.append(tk.Entry())
            paramEntries[rowNum].grid(in_=middle, row=rowNum, column=1, padx=10, sticky="NEW")
            rowNum+=1

        resultText = tk.Label(text=printEq[0])
        resultText.grid(in_=middle, row=rowNum+1, column=0, padx=10, pady=5)
        resultEntry = tk.Entry()
        calculateButton = tk.Button(text="Calculate",
                                    command = lambda pE=paramEntries, rE=resultEntry, eq=eq:
                                        self.calculate(pE, rE, eq))
        calculateButton.grid(in_=middle, row=rowNum, column=0, columnspan=2, padx=10, pady=5)
        resultEntry.grid(in_=middle, row=rowNum+1, column=1, padx=10, sticky=tk.EW)
    # End openEquation

    # Method that calss each equation's function to calculate the result
    def calculate(self, paramEntries, resultEntry, equation):
        try:
            numParams = len(paramEntries)
            resultEntry.delete(0,tk.END)

            params = []
            i=0
            for entry in paramEntries:
                params.append(float(entry.get()))
            resultEntry.insert(0, getattr(self.ae, equation)(params))
        except:
            resultEntry.insert(0, "ERROR")
    # End calculate

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
