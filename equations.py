from inspect import signature

class AstronomyEquations:
    # This is a class that holds all my equations and
    # all of the methods to print the equations
    def __init__(self):
        # Supersciprt and Subscript Numbers 0-9
        #                 0        1        2        3        4        5        6        7        8        9
        self.supNums = ['\u2070','\u00b9','\u00b2','\u00b3','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079']
        self.subNums = ['\u2080','\u2081','\u2082','\u2083','\u2084','\u2085','\u2086','\u2087','\u2088','\u2089']

        # Greek Characters
        # a = alpha, o = theta
        self.greek = {'a': '\u03B1', 'o': '\u03B8'}
        # End init

    # Returns a list of all the equation methods
    def getAllEquations(self):
        equationMethods = [method for method in dir(AstronomyEquations) if (method.startswith('__') or method.endswith('Print')) is False]
        equationMethods.remove('getAllEquations')
        equationMethods.remove('getAllPrints')
        return equationMethods

    #Returns a list of all the equation print methods
    def getAllPrints(self):
        printMethods = [method for method in dir(AstronomyEquations) if (method.startswith('__') or method.endswith('Equation')) is False]
        printMethods.remove('getAllEquations')
        printMethods.remove('getAllPrints')
        return printMethods

    # Physics Equations

    # Velocity
    # values[0] = Displacement
    # values[1] = Time
    def velocityEquation(self, values):
        return values[0] / values[1]
    def velocityPrint(self):
        return ["Velocity", "v = d / t", ["Displacement", "Time"]]
    # Acceleration
    # values[0] = Velocity
    # values[1] = Time
    def accelerationEquation(self, values):
        return values[0] / values[1]
    def accelerationPrint(self):
        return ["Acceleration", "a = v / t", ["Velocity", "Time"]]
    # Motion Equations
    # values[0] = Initial_Velocity
    # values[1] = Acceleration
    # values[2] = Time
    def motion1Equation(self, values):
        return values[0] + values[1] * values[2]
    def motion1Print(self):
        return ["Motion",
                "v%s = v%s + at" % (self.subNums[1], self.subNums[0]),
                ["Initial_Velocity", "Acceleration", "Time"]]
    # values[0] = Initial Position
    # values[1] = Initial Velocity
    # values[2] = Acceleration
    # values[3] = Time
    def motion2Equation(self, values):
        return values[0] + values[1]*values[3] + 0.5 * values[2] * values[3]**2
    def motion2Print(self):
        return ["Motion",
                "d%s = d%s + v%st + 0.5at%s" % (self.subNums[1], self.subNums[0], self.subNums[0], self.supNums[2]),
                ["Initial_Position", "Initial_Velocity", "Acceleration", "Time"]]
    # values[0] = Initial Velocity
    # values[1] = Acceleration
    # values[2] = Final Position
    # values[2] = Initial Position
    def motion3Equation(self, Initial_Velocity, Acceleration, Final_Position, Initial_Position):
        return values[0]**2 + 2*values[1] * (values[2] - values[3])
    def motion3Print(self):
        return ["Motion",
                "v%s%s = v%s%s + 2a(d%s - d%s)" % (self.subNums[1], self.supNums[2], self.subNums[0], self.supNums[2], self.subNums[1], self.subNums[0]),
                ["Initial_Velocity", "Acceleration", "Final_Position", "Initial_Position"]]
    # values[0] = Final Velocity
    # values[1] = Initial Velocity
    def motion4Equation(self, values):
        return 0.5 * (values[0] + values[1])
    def motion4Print(self):
        return ["Motion",
                "v%s = 0.5(v%s + v%s)" % ('\u0304', self.subNums[1], self.subNums[0]),
                ["Final_Velocity", "Initial_Velocity"]]

    # Astronomy Equations
    # values[0] = alpha
    # values[1] = d
    def astDistance1Equation(self, values):
        return values[0] * values[1] / 206265
    def astDistance1Print(self):
        return ["AST Distance",
                "D = %sd / 206265" % (self.greek['a']),
                ["alpha", "d"]]
    # values[0] = alpha
    # values[1] = D
    def astDistance2Equation(self, values):
        return 206265 * values[1] / values[0]
    def astDistance2Print(self):
        return ["AST Distance",
                "d = 206265D / %s" % (self.greek['a']),
                ["alpha", "D"]]
    # values[0] = theta
    def astDistance3Equation(self, values):
        return 1 / values[0]
    def astDistance3Print(self):
        return ["AST Distance",
                "d = 1 / %s" % (self.greek['o']),
                ["theta"]]



if (__name__ == '__main__'):
    ae = AstronomyEquations()
    #print("EQUATIONS")
    em = ae.getAllEquations()
    #print("PRINTS")
    #pm = ae.getAllPrints()
    for eq in ae.getAllPrints():
        pass
        #print(getattr(ae, eq)())
    str1 = "motion4Equation"
    print(len(signature(getattr(ae, str1)).parameters))
    print(len(signature(ae.motion4Equation).parameters))