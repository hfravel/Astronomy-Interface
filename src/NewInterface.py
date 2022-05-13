import tkinter as tk
from Equations import AstronomyEquations
import Page

class NewInterface:
    def __init__(self):
        self.loadInterfaceStructure()
        self.window = tk.Tk(className=self.title)
        self.window.geometry("500x500")
        # print(self.interfaceStructure[1])
        Page.createButtonListPage(self.window, self.title, self.interfaceStructure[1])
        self.window.mainloop()
    # End __init__

    def loadInterfaceStructure(self):
        structureFile = open("./format/default.txt")
        fileLines = structureFile.read().split("\n")
        firstLine = fileLines[0].split(":")
        self.title = firstLine[0]
        self.interfaceStructure = firstLine[1:]

        if firstLine[1] == "buttonList":
            self.interfaceStructure[1], lineNums = self.loadButtonList(1, firstLine[2], fileLines)
    # End loadInterfaceStructure
            
    def loadButtonList(self, lineNum, numBtns, fileLines):
        buttonListDict = {}
        for i in range(int(numBtns)):
            currLine = fileLines[lineNum].strip().split(":")
            buttonListDict[currLine[0]] = currLine[1:]
            lineNum += 1
            if (currLine[1] == "buttonList"):
                buttonListDict[currLine[0]][1], lineNum = self.loadButtonList(lineNum, currLine[2], fileLines)
            # End If
        # End For
        return buttonListDict, lineNum
    # End loadButtonList
    
# End NewInterface


if (__name__ == "__main__"):
    astroInterface = NewInterface()