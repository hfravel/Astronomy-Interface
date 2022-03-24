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
    def velocityEquation(self, Displacement, Time):
        return Displacement / Time
    def velocityPrint(self):
        return "Velocity < v = d / t >"
    # Acceleration
    def accelerationEquation(self, Velocity, Time):
        return Velocity / Time
    def accelerationPrint(self):
        return "Acceleration < a = v / t >"
    # Motion Equations
    def motion1Equation(self, Initial_Velocity, Acceleration, Time):
        return Initial_Velocity + Acceleration*Time
    def motion1Print(self):
        return "Motion < v%s = v%s + at >" % (self.subNums[1], self.subNums[0])
    def motion2Equation(self, Initial_Position, Initial_Velocity, Acceleration, Time):
        return Initial_Position + Initial_Velocity*Time + 0.5*Acceleration*Time**2
    def motion2Print(self):
        return "Motion < d%s = d%s + v%st + 0.5at%s >" % (self.subNums[1], self.subNums[0], self.subNums[0], self.supNums[2])
    def motion3Equation(self, Initial_Velocity, Acceleration, Final_Position, Initial_Position):
        return Initial_Velocity**2 + 2*Acceleration * (Final_Position - Initial_Position)
    def motion3Print(self):
        return "Motion < v%s%s = v%s%s + 2a(d%s - d%s) >" % (self.subNums[1], self.supNums[2], self.subNums[0], self.supNums[2], self.subNums[1], self.subNums[0])
    #@staticmethod
    def motion4Equation(self, Final_Velocity, Initial_Velocity):
        return 1/2 * (Final_Velocity + Initial_Velocity)
    def motion4Print(self):
        return "Motion < v%s = 0.5(v%s + v%s) >" % ('\u0304', self.subNums[1], self.subNums[0])

    # Astronomy Equations
    def astDistance1Equation(self, alpha, d):
        return alpha * d / 206265
    def astDistance1Print(self):
        return 'AST Distance < D = %sd / 206265 >' % (self.greek['a'])
    def astDistance2Equation(self, alpha, D):
        return 206265 * D / alpha
    def astDistance2Print(self):
        return 'AST Distance < d = 206265D / %s >' % (self.greek['a'])
    def astDistance3Equation(self, theta):
        return 1 / theta
    def astDistance4Print(self):
        return 'AST Distance < d = 1 / %s >' % (self.greek['o'])



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