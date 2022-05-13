import tkinter as tk
import Helpers
from VerticalScrolledFrame import VerticalScrolledFrame

buttonCommand = {"text"             :   lambda: createTextPage(),
                  "buttonList"      :   lambda w, t, bl: createButtonListPage(),
                  "detailedButtons" :   lambda: createDetailedButtonsPage(),
                  "simulation"      :   lambda: createSimulationPage()}

def createPageFrames(window):
    top = tk.Frame(window, bg=Helpers.BG, height=1)
    middle = tk.Frame(window, bg=Helpers.BG, height=1)
    bottom = tk.Frame(window, bg=Helpers.BG, height=1)
    top.pack(fill=tk.X)
    middle.pack(fill=tk.BOTH, expand=True)
    bottom.pack(fill=tk.X)
    return top, middle, bottom

def createTitleBack(title, top, bottom):
    topLabel = tk.Label(top, text=title, height=1, bg=Helpers.BG, font=Helpers.titleFont)
    topLabel.pack(fill = tk.BOTH)
    backButton = tk.Button(bottom, text="Back")
    backButton.pack(fill = tk.BOTH)
# window, title, textFile
def createTextPage():
    pass

def createButtonListPage(window, title, buttonDict):
    top, middle, bottom = createPageFrames(window)
    scrollFrame = VerticalScrolledFrame(middle)
    for btnKey in buttonDict:
        currBtn = Helpers.createButton(scrollFrame.interior, btnKey, buttonCommand["text"])
        currBtn.pack(fill = tk.X)
    scrollFrame.pack(fill=tk.BOTH, expand=True)
    createTitleBack(title, top, bottom)

def createDetailedButtonsPage():
    pass
def createSimulationPage():
    pass