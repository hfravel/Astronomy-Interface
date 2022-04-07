import tkinter as tk
from Equations import AstronomyEquations
from VerticalScrolledFrame import VerticalScrolledFrame
from inspect import signature

# Astronomy Class Declaration
class AstronomyInterface:
    # Create the Interface
    def __init__(self):
        self.title = "Astronomy Interface"
        self.titlefont = "Times 20 bold underline"
        self.mainfont = "Times 12"
        self.BG = "white"
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
        # Gets rid of the mousewheel binding from VerticalScrollFrame
        self.window.unbind_all("<MouseWheel>")
        # Clears the window's widgets to add the new page's widgets
        for widget in self.window.winfo_children():
            widget.destroy()
    # End destroyWidgets

    # Creates the main page
    def createMain(self, middle):
        xpad = 10
        ypad = 10
        btnNum = 1
        for mainBtn in self.mainButtons:
            currButton = tk.Button(background = "light blue", activebackground='purple', font=self.mainfont,
                text=str(btnNum) + ") " + mainBtn,
                command = lambda pageName=mainBtn:
                    self.createPage(pageName, self.backToMain, "create"+pageName),
                height=2, anchor='w', cursor="hand2"
            )
            currButton.pack(in_=middle,fill=tk.BOTH, expand=True, padx=xpad, pady=ypad)

            btnNum+=1
    # End of createMain

    # Start of the basic page creation
    def createPage(self, title, backFunc, middleFunc, eq=""):
        self.destroyWidgets()
        top = tk.Frame(bg=self.BG)
        middle = tk.Frame(bg=self.BG)
        bottom = tk.Frame(bg=self.BG)
        # top.pack(side=tk.TOP, fill = tk.X)
        # middle.pack(fill=tk.BOTH, expand=True)
        # bottom.pack(side=tk.BOTTOM, fill=tk.X)
        self.window.grid_columnconfigure(0,weight=1)
        self.window.grid_rowconfigure(1,weight=1)
        top.grid(row=0,column=0, sticky=tk.NSEW)
        middle.grid(row=1,column=0, sticky=tk.NSEW)
        bottom.grid(row=2,column=0, sticky=tk.NSEW)

        # This is where the middle goes
        if eq=="":
            getattr(self, middleFunc)(middle)
        else:
            getattr(self, middleFunc)(middle, eq)
        # End the middle part

        topLabel = tk.Label(
            text=title,
            height=2, bg = self.BG,
            font=self.titlefont
        )
        topLabel.pack(in_=top, fill=tk.X)

        # Creates the back Button
        if middleFunc != "createMain":
            backButton = tk.Button(font=self.mainfont,
                text="Back", height=2,
                command=backFunc,
                cursor="hand2"
            )
            backButton.pack(in_=bottom, fill=tk.X, expand=True)
            self.window.update()
            print("BACK")
            print(backButton.winfo_height())
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

        switchButton=tk.Button(text="Switch View Button", cursor="hand2")
        switchButton.pack(in_=middle, side=tk.TOP,fill=tk.X)
    # End createEquation

    # Adds the equationType to scrollFrame starting at currRow
    # If equationType = "Physics Equations" add physics equations to scrollFrame
    # Else add astronomy equations to scrollFrame
    def addEquationsToFrame(self, scrollFrame, equationType, currRow):
        ypad = 15
        xpad = 5
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
        typeLabel.grid(in_=scrollFrame, row=currRow, column=0,
                       pady=ypad, padx=xpad, columnspan=2, sticky=tk.EW)
        currRow+=1

        for i in range(len(equations)):
            aboutEquation = getattr(self.ae, prints[i])()
            equationName = tk.Label(text=aboutEquation[0][0])
            equationName.grid(in_=scrollFrame, row=currRow, column=0,
                              pady=ypad, padx=xpad, sticky=tk.EW)

            equationButton = tk.Button(height=1, width=20, relief=tk.FLAT,
                            bg="gray99", fg="purple3",
                            font="Dosis", text=aboutEquation[1],
                            command=lambda t=aboutEquation[0][0]+": "+aboutEquation[1], eq=equations[i]:
                                self.createPage(t, self.backToEqua, "openEquation", eq),
                            cursor="hand2")
            #btn.pack(padx=10, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)
            equationButton.grid(in_=scrollFrame, row=currRow, column=1, sticky=tk.EW)
            currRow+=1

        return currRow
    # End addEquationsToFrame

    # Opens a specific a page for a specific equation
    def openEquation(self, middle, eq):
        ixpad = 15
        xpad = 10
        ypad = 5

        printEq = getattr(self.ae, eq[0:len(eq)-8] + "Print")()

        middle.grid_columnconfigure(1,weight=1)
        paramEntries = []
        rowNum = 0
        for param in printEq[2]:
            paramText = tk.Label(text=param, anchor=tk.E)
            paramText.grid(in_=middle, row=rowNum, column=0,
                           ipadx=ixpad, pady=ypad,
                           sticky="EW")
            paramEntries.append(tk.Entry())
            paramEntries[rowNum].grid(in_=middle, row=rowNum,
                                      column=1, padx=xpad, sticky="NEW")
            rowNum+=1

        resultText = tk.Label(text=printEq[0][0]+printEq[0][1], anchor=tk.E)
        resultText.grid(in_=middle, row=rowNum+1, column=0,
                        pady=ypad, ipadx=ixpad)
        resultEntry = tk.Entry()
        calculateButton = tk.Button(text="Calculate",
                                    command = lambda pE=paramEntries, rE=resultEntry, eq=eq:
                                        self.calculate(pE, rE, eq),
                                    cursor="hand2")
        calculateButton.grid(in_=middle, row=rowNum, column=1,
                             padx=xpad, pady=ypad)
        resultEntry.grid(in_=middle, row=rowNum+1, column=1,
                         padx=xpad, sticky=tk.EW)
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
        canvas = tk.Canvas(bg="black")
        canvas.pack(in_=middle, fill=tk.BOTH, expand=True)

        size = 7
        self.window.update()
        center_height = (canvas.winfo_height() - size) / 2
        center_width = (canvas.winfo_width() - size) / 2

        objs = [("Sun", 0.0, "yellow"),
                 ("Mercury", 0.387, "grey"),
                 ("Venus", 0.7, "orange"),
                 ("Earth", 1.0, "green"),
                 ("Mars", 1.524, "red"),
                 ("Jupiter", 5.203, "tan"),
                 ("Saturn", 9.555, "brown"),
                 ("Uranus", 19.8, "light blue"),
                 ("Neptune", 30.11, "blue")]
        #sun = canvas.create_oval((center_width, center_height, center_width+size, center_height+size), fill="yellow")

        bodies = []
        for i in range(9):
            bodies.append(canvas.create_oval((0,0,size,size), fill=objs[i][2]))

        def resize(e):
            self.window.update()
            width = canvas.winfo_width()
            centerX = (width - size) / 2
            centerY = (canvas.winfo_height() - size) / 2

            for i in range(9):
                currCoord = canvas.coords(bodies[i])
                canvas.move(bodies[i], ((objs[i][1] + 1) * width/32) - currCoord[0], centerY-currCoord[1])

            #canvas.move(sun, centerX-coord[0], centerY-coord[1])
            self.window.update()


        canvas.bind("<Configure>", resize)
    # End createSimulation


# Execution Part
if (__name__ == '__main__'):
    ai = AstronomyInterface()
