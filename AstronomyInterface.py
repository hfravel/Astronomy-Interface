import math
import tkinter as tk
from Equations import AstronomyEquations
from VerticalScrolledFrame import VerticalScrolledFrame

# Astronomy Class Declaration
class AstronomyInterface:
    # Create the Interface
    def __init__(self):
        self.title = "Astronomy Interface"
        self.titlefont = "Times 20 bold underline"
        self.currData = "Data"
        self.currLearn = "Learn"
        self.mainfont = "Times 12"
        self.BG = "white"
        self.buttonColor = "light blue"
        self.mainButtons = ["Help",
                            "Learn",
                            "Data",
                            "Equation",
                            "Simulation"]
        self.ae = AstronomyEquations()
        self.backToMain = lambda: self.createPageStructure(self.title, "createMain")
        self.backToEqua = lambda: self.createPageStructure("Equation", "createEquation")
        #self.backToData = lambda: self.createPage("Data", self.backToMain, "createData")

        # Create the astonromy interface window
        self.window = tk.Tk(className=self.title)
        self.window.geometry("500x500")
        self.createPageStructure(self.title, "createMain")
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

    # Creates a tkinter button with preset values
    def createButton(self, frame, title, command, anchor, height):
        return tk.Button(frame, text=title, command=command, anchor=anchor, height=height,
                         background='light blue', activebackground='purple',
                         font=self.mainfont, cursor='hand2')
    # End createButton

    # Creates a scrollbox of buttons
    def createScrollButton(self, frame, buttons):
        scframe = VerticalScrolledFrame(frame)
        #scframe.pack(in_=middle, side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # scframe.interior.grid_rowconfigure(0,weight=1)
        # scframe.interior.grid_columnconfigure(0,weight=1)

        #row = 0
        for b in buttons:
            currButton = self.createButton(scframe.interior, b[0], b[1], 'w', 2)
            currButton.pack(fill=tk.X, pady=5, padx=15)
            #row += 1

        return scframe

    # Creates all basic page Structures
    def createPageStructure(self, title, middleFunc, eq=""):
        self.destroyWidgets()
        top = tk.Frame(self.window, bg=self.BG, height=1)
        middle = tk.Frame(self.window, bg=self.BG, height=1)
        bottom = tk.Frame(self.window, bg=self.BG, height=1)
        top.pack(fill=tk.X)
        middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(fill=tk.X)

        # This is where the middle goes
        if eq=="":
            backFunc = getattr(self, middleFunc)(middle)
        else:
            backFunc = getattr(self, middleFunc)(middle, eq)
        # End the middle part

        topLabel = tk.Label(
            text=title,
            height=1, bg = self.BG,
            font=self.titlefont
        )
        topLabel.pack(in_=top, fill=tk.X)

        # Creates the back Button
        if middleFunc != "createMain":
            backButton = self.createButton(bottom, "Back", backFunc, "center", 1)
            backButton.pack(fill=tk.X, expand=True)
            bottom.lift()
    # End createPageStructure

    # Creates the main page
    def createMain(self, middle):
        xpad = 10
        ypad = 10
        buttonNum = 1
        buttons = []
        for mainBtn in self.mainButtons:
            buttons.append([f"{buttonNum}) {mainBtn}",
                            lambda title=mainBtn: self.createPageStructure(title, f"create{title}")])
            buttonNum += 1

        scframe = self.createScrollButton(middle, buttons)
        scframe.pack(fill=tk.BOTH, expand=True)
        return "" # No back button to return
    # End of createMain

    # Used to create the Help page
    def createHelp(self, middle):
        print("Help")
        return self.backToMain
    # End createHelp

    # Used to create the Learn page
    def createLearn(self, middle):
        sections = {"Learn": ["Solar System", "Galaxy", "Universe"],
                    "Solar System" : ["Sun", "Mercury", "Venus", "Earth", "Mars", "Astroid Belt",
                                     "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Oort Cloud"],
                    "Galaxy"       : ["Galaxy", "Super Massive Black Hole", "Black Hole", "White Dwarf", "Neutron Star"],
                    "Universe"     : ["Big Bang", "IDK other stuff maybe"] }

        def changePage(s):
            self.currLearn = s;
            self.createPageStructure(s, "createLearn")

        output = []
        for sec in sections[self.currLearn]:
            output.append([sec, lambda s=sec: changePage(s)])

        scframe = self.createScrollButton(middle, output)
        scframe.pack(side=tk.BOTTOM, fill=tk.BOTH, pady=5, expand=True)
        if (self.currLearn == "Learn"):
            return self.backToMain
        else:
            return (lambda: changePage("Learn"))
    # End createLearn

    # Used to create the Data page
    def createData(self, middle):
        sections = {"Data": ["Solar System", "Galaxy", "Universe"],
                    "Solar System" : ["Sun", "Mercury", "Venus", "Earth", "Mars", "Astroid Belt",
                                     "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Oort Cloud"],
                    "Galaxy"       : ["Galaxy", "Super Massive Black Hole", "Black Hole", "White Dwarf", "Neutron Star"],
                    "Universe"     : ["Big Bang", "IDK other stuff maybe"] }

        def changePage(s):
            self.currData = s;
            self.createPageStructure(s, "createData")

        output = []
        for sec in sections[self.currData]:
            output.append([sec, lambda s=sec: changePage(s)])

        scframe = self.createScrollButton(middle, output)
        scframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        if (self.currData == "Data"):
            return self.backToMain
        else:
            return (lambda: changePage("Data"))
    # End createData

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
        return self.backToMain
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
            text=equationType, bg='white',
            height=2,
            font=("Times 15 bold underline")
        )
        typeLabel.grid(in_=scrollFrame, row=currRow, column=0,
                       pady=ypad, padx=xpad, columnspan=2, sticky=tk.EW)
        currRow+=1

        for i in range(len(equations)):
            aboutEquation = getattr(self.ae, prints[i])()
            equationName = tk.Label(scrollFrame, text=aboutEquation[0][0], bg=self.BG)
            equationName.grid(row=currRow, column=0,
                              pady=ypad, padx=xpad, sticky=tk.EW)

            equationButton = self.createButton(scrollFrame, aboutEquation[1],
                                               lambda t=aboutEquation[0][0]+": "+aboutEquation[1], eq=equations[i]:self.createPageStructure(t, "openEquation", eq),
                                               "center", 1)
            equationButton.grid(row=currRow, column=1, sticky=tk.EW)
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
        return self.backToEqua
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
        except Exception as e:
            if (isinstance(e, ZeroDivisionError)):
                resultEntry.insert(0,"Invalid: Division by 0")
            elif (isinstance(e, ValueError)):
                resultEntry.insert(0, "Invalid: Improper Entry")
            else:
                resultEntry.insert(0, e)
    # End calculate

    # Used to create the Simulation page
    def createSimulation(self, middle):
        jovianView = 0
        terrView = 1
        positions = [0.0 for i in range (9)]
        sim = False
        view = 0
        numViews = 2
        size = 7
        speed = 1

        # Creates the canvas in which our solar system will lie
        canvas = tk.Canvas(bg="black")
        # Create the buttons at the top
        startSim = tk.Button(text="Start", width = 1,
                             bg = self.buttonColor,
                             font = self.mainfont)
        switchView = tk.Button(text="Terrestrial View", width = 1,
                             bg = self.buttonColor,
                             font = self.mainfont)
        # Configure the row and column weight
        middle.grid_rowconfigure(1, weight=1)
        middle.grid_columnconfigure(0, weight=1)
        middle.grid_columnconfigure(1, weight=1)
        # Add the buttons and canvas to the frame
        startSim.grid(in_=middle,
                      row=0, column=0,
                      sticky=tk.EW)
        switchView.grid(in_=middle,
                      row=0, column=1,
                      sticky=tk.EW)
        canvas.grid(in_=middle,
                    row=1, columnspan=2,
                    sticky=tk.NSEW)

        # Data for each object
        # (Name, Perihelion (10^6 km), Aphelion (10^6 km), orbital period (days), colour)
        objs = [("Sun",      0.0,    0.0,    0.0,     "yellow"),
                 ("Mercury", 46.0,   69.8,   88,      "grey"),
                 ("Venus",   107.5,  108.9,  224.6,   "orange"),
                 ("Earth",   147.1,  152.1,  365.2,   "green"),
                 ("Mars",    206.7,  249.3,  687.0,   "red"),
                 ("Jupiter", 740.6,  816.4,  4331.0,  "tan"),
                 ("Saturn",  1357.6, 1506.5, 10747.0, "brown"),
                 ("Uranus",  2732.7, 3001.4, 30589.0, "light blue"),
                 ("Neptune", 4471.1, 4558.9, 59800.0, "blue")]

        # Create the sun and 8 planets: couldn't fit pluto
        bodies = []
        for i in range(9):
            bodies.append(canvas.create_oval((0,0,size,size), fill=objs[i][4], tags=objs[i][0]))

        # Updates planets positions in terrestial view
        def updatePlanets():
            # Makes sure winfo.width() gets right size of canvas
            self.window.update()
            width = canvas.winfo_width()
            # make sure the solar system is the size of the window
            if view==jovianView:
                block = width / (objs[8][2] * 1.1) / 2
            else:
                block = width / (objs[4][2] * 1.1) / 2
            centerX = (width - size) / 2
            centerY = (canvas.winfo_height() - size) / 2

            for i in range(9):
                oldPos = canvas.coords(bodies[i])
                newXPos = centerX + (math.cos(positions[i]) * (block * objs[i][2])) + size/2
                newYPos = centerY + (math.sin(positions[i]) * (block * objs[i][1])) + size/2
                canvas.move(bodies[i], newXPos - oldPos[0], newYPos - oldPos[1])

            self.window.update()
        # End updatePlanets

        # Start or stop simulation
        def simulation():
            nonlocal positions
            nonlocal sim
            nonlocal startSim
            sim = not sim
            try:
                startSim.config(text="Stop")
                while(sim):
                    for i in range(1,9):
                        positions[i]+= speed / objs[i][3]
                    updatePlanets()
                    self.window.update()
                # End While
                startSim.config(text="Start")
            except Exception as e:
                print(e)
        # End simulation

        # Switch the view Terrestrial <-> Jovian
        def switch():
            nonlocal view
            nonlocal speed
            nonlocal switchView
            view = (view + 1) % numViews
            if view == jovianView:
                switchView.config(text="Terrestial View")
                speed = 1
            else:
                switchView.config(text="Jovian View")
                speed = 0.2
            updatePlanets()

        # If cursor is over an object, change it to a clicker
        def check_hand(e):
            hand = ""
            for body in bodies:
                bbox = canvas.bbox(body)
                if bbox[0] < e.x and bbox[2] > e.x and bbox[1] < e.y and bbox[3] > e.y:
                    hand="hand2"
            canvas.config(cursor=hand)


        canvas.bind("<Motion>", check_hand)
        canvas.bind("<Configure>", lambda e: updatePlanets())
        startSim.config(command=simulation)
        switchView.config(command=switch)
        canvas.tag_bind(objs[0][0], "<Button-1>", lambda e: switch())
        return self.backToMain
    # End createSimulation


# Execution Part
if (__name__ == '__main__'):
    ai = AstronomyInterface()
