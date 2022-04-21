import math
import tkinter as tk
from Equations import AstronomyEquations
from VerticalScrolledFrame import VerticalScrolledFrame
from PIL import ImageTk, Image # Used for added image into text
from tkinter import font

# Astronomy Class Declaration
class AstronomyInterface:
    # Create the Interface
    def __init__(self):
        self.title = "Astronomy Interface"
        self.titlefont = ["Times New Roman", 24, "bold underline"]
        self.mainfont = ["Arial CYR", 15]
        self.BG = "white"
        self.pad = [10, 5]
        self.mainButtons = ["Help", "Learn", "Data", "Equation", "Simulation"]

        learnPages = {"Learn": ["Solar System", "Galaxy", "Universe"],
                      "Solar System" : ["Sun", "Mercury", "Venus", "Earth", "Mars", "Astroid Belt",
                                     "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Oort Cloud"],
                      "Galaxy"       : ["Galaxy", "Super Massive Black Hole", "Black Hole", "White Dwarf", "Neutron Star"],
                      "Universe"     : ["Big Bang", "IDK other stuff maybe"] }
        dataPages = {"Data" : ["Sun", "Mercury", "Venus", "Earth", "Mars", "Astroid Belt",
                               "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "Oort Cloud"]}
        self.infoPages = {"Learn" : learnPages,
                          "Data"  : dataPages}
        self.textImages = []
        self.backPath = []
        self.currToolTip=(0, None)
        self.ae = AstronomyEquations()
        self.supNums = ['\u2070', '\u00b9', '\u00b2', '\u00b3', u'\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
        self.backToMain = lambda: self.createPageStructure(self.title, lambda m: self.createMain(m))
        self.backToEqua = lambda: self.createPageStructure("Equation", lambda m: self.createEquation(m))

        # Create the astonromy interface window
        self.window = tk.Tk(className=self.title)
        self.window.geometry("500x500")
        self.createPageStructure(self.title, lambda m: self.createMain(m))
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

        for b in buttons:
            currButton = self.createButton(scframe.interior, b[0], b[1], 'w', 2)
            currButton.pack(fill=tk.X, padx=self.pad[0], pady=self.pad[1])

        return scframe

    # Creates all basic page Structures
    def createPageStructure(self, title, middleFunc):
        self.destroyWidgets()
        self.backPath.append([title, middleFunc])
        top = tk.Frame(self.window, bg=self.BG, height=1)
        middle = tk.Frame(self.window, bg=self.BG, height=1)
        bottom = tk.Frame(self.window, bg=self.BG, height=1)
        top.pack(fill=tk.X)
        middle.pack(fill=tk.BOTH, expand=True)
        bottom.pack(fill=tk.X)

        # This is where the middle goes
        middleFunc(middle)
        # End the middle part

        topLabel = tk.Label(
            text=title,
            height=1, bg = self.BG,
            font=self.titlefont
        )
        topLabel.pack(in_=top, fill=tk.X)

        def getBackFunc():
            self.backPath.pop(len(self.backPath)-1)
            backFunc = self.backPath.pop(len(self.backPath)-1)
            self.createPageStructure(backFunc[0], backFunc[1])

        # Creates the back Button
        if title != self.title:
            backButton = self.createButton(bottom, "Back", getBackFunc, "center", 1)
            backButton.pack(fill=tk.X, expand=True)
            bottom.lift()
    # End createPageStructure

    # Read
    def readTextFile(self, frame, file):
        textBox = tk.Text(frame, font=self.mainfont, bg=self.BG, width=1, height=1)
        scrollBar = tk.Scrollbar(frame, cursor="hand2", command=textBox.yview)
        scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        textBox.config(yscrollcommand=scrollBar.set)
        textBox.pack(fill=tk.BOTH, expand=True, pady=self.pad[1])

        try:
            readFile = open(f"./texts/{file}")
        except:
            textBox.insert(tk.END, f"No such file found: ./texts/{file}.")
            return 0

        self.textImages = []
        i = 0
        for line in readFile:
            if line[0] == "#":
                splitLine = line.split()
                if splitLine[1] == "Image":
                    self.textImages.append(ImageTk.PhotoImage(Image.open(splitLine[2])))
                    textBox.image_create(tk.END, image=self.textImages[i])
                    i += 1
                else:
                    textBox.insert(tk.END, f"error <{line}>")
                textBox.insert(tk.END, "\n")

            else:
                textBox.insert(tk.END, eval(f'f"""{line}"""'))
        textBox.config(state="disable")
    # End readTextFile

    # Creates the main page
    def createMain(self, middle):
        buttonNum = 1
        buttons = []
        # Creates the list of buttons.  Structure = (Button Name, Button Function)
        for mainBtn in self.mainButtons:
            buttonFunc = lambda m, f=getattr(self,f"create{mainBtn}"): f(m)
            buttons.append([f"{buttonNum}) {mainBtn}",
                            lambda t=mainBtn, f=buttonFunc: self.createPageStructure(t, f)])
            buttonNum += 1
        # Creates a scrollbar with the buttons from the loop above
        scframe = self.createScrollButton(middle, buttons)
        scframe.pack(fill=tk.BOTH, expand=True)
    # End of createMain

    # Used to create the Help page
    def createHelp(self, middle):
        self.readTextFile(middle, "help.txt")
    # End createHelp

    # Used to create the Learn and Data pages
    def createInfo(self, middle, which, currPage):
        # Adds a list of buttons to the page
        if currPage in self.infoPages[which]:
            output = []
            for page in self.infoPages[which][currPage]:
                func1 = lambda m, p=page: self.createInfo(m, which, p)
                func2 = lambda p=page, f=func1: self.createPageStructure(p, f)
                output.append([page, func2])

            scframe = self.createScrollButton(middle, output)
            scframe.pack(side=tk.BOTTOM, fill=tk.BOTH, pady=5, expand=True)
        # Adds the text to the page
        else:
            fileName = currPage.replace(" ", "")
            self.readTextFile(middle, f"{which}/{fileName}.txt")
    # End createInfo

    # Creates the Learn Page
    def createLearn(self, middle, page="Learn"):
        self.createInfo(middle, "Learn", page)
    # End createLearn

    # Creates the Data Page
    def createData(self, middle, page="Data"):
        self.createInfo(middle, "Data", page)
    # End createData

    # Used to create the Equation page
    def createEquation(self, middle):
        scframe = VerticalScrolledFrame(middle)
        scframe.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=self.pad[1])

        scframe.interior.grid_rowconfigure(0,weight=1)
        scframe.interior.grid_columnconfigure(0,weight=2)
        scframe.interior.grid_columnconfigure(1,weight=3)

        currRow = 0
        # Create physics and astronomy equation buttons in scrollframe
        currRow = self.addEquationsToFrame(scframe.interior, "Physics Equations", currRow)
        currRow = self.addEquationsToFrame(scframe.interior, "Astronomy Equations", currRow)
    # End createEquation

    # Adds the equationType to scrollFrame starting at currRow
    # equationType can be "Physics Equations" or "Astronomy Equations"
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
            text=equationType, bg=self.BG,
            height=1,
            font=self.mainfont + ["bold underline"]
        )
        typeLabel.grid(in_=scrollFrame, row=currRow, column=0,
                       padx=self.pad[0], pady=self.pad[1], columnspan=2, sticky=tk.EW)
        currRow+=1

        for i in range(len(equations)):
            aboutEquation = getattr(self.ae, prints[i])()

            equationName = tk.Label(scrollFrame, text=aboutEquation[0][0], bg=self.BG)
            equationName.grid(row=currRow, column=0,
                              padx=self.pad[0], pady=self.pad[1], sticky=tk.EW)
            equationFunction = lambda t=aboutEquation[0][0]+": "+aboutEquation[1], eq=equations[i]:self.createPageStructure(t, lambda m: self.openEquation(m, eq))

            equationButton = self.createButton(scrollFrame, aboutEquation[1], equationFunction, "center", 1)
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
        calculateButton = self.createButton(middle, "Calculate",
                                            lambda pE=paramEntries, rE=resultEntry, eq=eq: self.calculate(pE, rE, eq),
                                            "center", 1)
        calculateButton.grid(row=rowNum, column=1,
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
        # Configure the row and column weight
        middle.grid_rowconfigure(1, weight=1)
        middle.grid_columnconfigure(0, weight=1)
        middle.grid_columnconfigure(1, weight=1)

        # Initialize our variables
        positions = [0.0 for i in range (9)]
        sim = False
        view = "Jovian"
        size = 7
        speed = 1
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

        # Updates planets positions in terrestial view
        def updatePlanets():
            # Makes sure winfo.width() gets right size of canvas
            self.window.update()
            width = canvas.winfo_width()
            height = canvas.winfo_height()
            # make sure the solar system is the size of the window
            if view=="Jovian":
                block = width / (objs[8][2] * 1.1) / 2
            else:
                block = width / (objs[4][2] * 1.1) / 2
            centerX = (width - size) / 2
            centerY = (height - size) / 2

            for i in range(9):
                oldPos = canvas.coords(bodies[i])
                newXPos = centerX + (math.cos(positions[i]) * (block * objs[i][2])) + size/2
                newYPos = centerY + (math.sin(positions[i]) * (block * objs[i][1])) + size/2
                canvas.move(bodies[i], newXPos - oldPos[0], newYPos - oldPos[1])

            self.window.update()
        # End updatePlanets

        # Start or stop simulation
        def simulation():
            nonlocal positions, sim, startSimulationButton
            sim = not sim
            try:
                startSimulationButton.config(text="Stop")
                while(sim):
                    for i in range(1,9):
                        positions[i]+= speed / objs[i][3]
                    updatePlanets()
                    self.window.update()
                # End While
                startSimulationButton.config(text="Start")
            except Exception as e:
                print(e)
        # End simulation

        # Switch the view Terrestrial <-> Jovian
        def switchView():
            nonlocal view, speed, switchViewButton
            if view == "Jovian":
                view = "Terrestrial"
                speed = 0.2
            elif view == "Terrestrial":
                view = "Jovian"
                speed = 1
            switchViewButton.config(text=f"Switch View ({view})")
            updatePlanets()

        def showToolTip(objNum):
            nonlocal self, canvas, objs, bodies
            canvas.config(cursor="hand2")
            bbox = canvas.bbox(bodies[objNum-1])
            x = bbox[0] + canvas.winfo_rootx() - 45
            y = bbox[1] + canvas.winfo_rooty() - 55
            # creates a toplevel window
            tw = tk.Toplevel(canvas)
            # Leaves only the label and removes the app window
            tw.wm_overrideredirect(True)
            tw.wm_geometry("+%d+%d" % (x, y))
            tipText = f"{objs[objNum-1][0]}\nLeft-click to Learn\nRight-click for Data"
            # tipText = objs[objNum-1][0] + " \nOther"
            label = tk.Label(tw, text=tipText, justify='center',
                             background=self.BG, relief='solid', borderwidth=1,
                             wraplength=200)
            label.pack(ipadx=1)
            self.currToolTip = (objNum, tw)

        def destroyToolTip(objNum):
            nonlocal self, canvas
            canvas.config(cursor="")
            if (objNum != self.currToolTip[0]): return
            tw = self.currToolTip[1]
            self.currToolTip = (0, None)
            if tw:
                tw.destroy()

        # Creates the canvas in which our solar system will lie
        canvas = tk.Canvas(middle, bg="black")
        # Create the buttons at the top
        startSimulationButton = self.createButton(middle, "Start", simulation, "center", 1)
        switchViewButton = self.createButton(middle, "Switch View (Jovian)", switchView, "center", 1)
        # Add the buttons and canvas to the frame
        startSimulationButton.grid(row=0, column=0, sticky=tk.EW)
        switchViewButton.grid(row=0, column=1, sticky=tk.EW)
        canvas.grid(row=1, columnspan=2, sticky=tk.NSEW)

        # Create the sun and 8 planets: couldn't fit pluto
        bodies = []
        for i in range(9):
            bodies.append(canvas.create_oval((0,0,size,size), fill=objs[i][4], tags=objs[i][0]))

        canvas.bind("<Configure>", lambda e: updatePlanets())
        # Set up the links to the simulation
        i = 1
        for body in objs:
            learnFunc = lambda m, b=body[0]: self.createInfo(m, "Learn", b)
            dataFunc = lambda m, b=body[0]: self.createInfo(m, "Data", b)
            canvas.tag_bind(body[0], "<Button-1>", lambda e, b=body[0], f=learnFunc: self.createPageStructure(b, f))
            canvas.tag_bind(body[0], "<Button-3>", lambda e, b=body[0], f=dataFunc: self.createPageStructure(b, f))
            canvas.tag_bind(body[0], "<Enter>", lambda e, i=i: showToolTip(i))
            canvas.tag_bind(body[0], "<Leave>", lambda e, i=i: destroyToolTip(i))
            i+=1
        # End for
    # End createSimulation


# Execution Part
if (__name__ == '__main__'):
    ai = AstronomyInterface()
