import math
from inspect import signature

class AstronomyEquations:
    # This is a class that holds all my equations and
    # all of the methods to print the equations
    def __init__(self):
        # Supersciprt and Subscript Numbers 0-9
        #                 0        1        2        3        4        5        6        7        8        9
        self.supNums = ['\u2070','\u00b9','\u00b2','\u00b3','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079']
        self.subNums = ['\u2080','\u2081','\u2082','\u2083','\u2084','\u2085','\u2086','\u2087','\u2088','\u2089']

        self.sqrt = '\u221A'

        # Greek Characters
        self.greek = {'alpha': '\u03B1', 'theta': '\u03B8'}
        # End init

    # Returns a list of all the physics equation methods
    def getPhyEquations(self):
        equationMethods = [method for method in dir(AstronomyEquations) if (method.startswith('phy') and method.endswith('Equation'))]
        return equationMethods
    # End getPhyEquations

    # Returns a list of all the physics equation methods
    def getPhyPrints(self):
        equationMethods = [method for method in dir(AstronomyEquations) if (method.startswith('phy') and method.endswith('Print'))]
        return equationMethods
    # End getPhyEquations

    # Returns a list of all the physics equation methods
    def getAstEquations(self):
        equationMethods = [method for method in dir(AstronomyEquations) if (method.startswith('ast') and method.endswith('Equation'))]
        return equationMethods
    # End getPhyEquations

    # Returns a list of all the physics equation methods
    def getAstPrints(self):
        equationMethods = [method for method in dir(AstronomyEquations) if (method.startswith('ast') and method.endswith('Print'))]
        return equationMethods
    # End getPhyEquations

    # Physics Equations

    # Velocity
    # values[0] = Displacement
    # values[1] = Time
    def phyVelocityEquation(self, values):
        return values[0] / values[1]
    # Velocity = Displacement / Time
    def phyVelocityPrint(self):
        return ["Velocity (m/s)",
                "v = x / t",
                ["Displacement(x) (m)", "Time(t) (s)"]]
    # Acceleration
    # values[0] = Velocity
    # values[1] = Time
    def phyAccelerationEquation(self, values):
        return values[0] / values[1]
    # Acceleration = Velocity / Time
    def phyAccelerationPrint(self):
        return ["Acceleration (m/s^2)",
                "a = v / t",
                ["Velocity (m/s)", "Time (s)"]]
    # Final Velocity
    # values[0] = Initial Velocity
    # values[1] = Acceleration
    # values[2] = Time
    def phyFinalVelocityEquation(self, values):
        return values[0] + values[1] * values[2]
    # Final_Velocity = Initial_Velocity + Acceleration * Time
    def phyFinalVelocityPrint(self):
        return ["Final Velocity (m/s)",
                "v%s = v%s + at" % (self.subNums[1], self.subNums[0]),
                ["Initial Velocity (m/s)", "Acceleration (m/s^2)", "Time (s)"]]
    # Final Position
    # values[0] = Initial Position
    # values[1] = Initial Velocity
    # values[2] = Acceleration
    # values[3] = Time
    def phyFinalPositionEquation(self, values):
        return values[0] + values[1]*values[3] + 0.5 * values[2] * values[3]**2
    # Final_Pos = Initial_Pos + Initial_Vel * Time + 1/2 * Acceleration * Time^2
    def phyFinalPositionPrint(self):
        return ["Final Position (m)",
                "x%s = x%s + v%st + 0.5at%s" % (self.subNums[1], self.subNums[0], self.subNums[0], self.supNums[2]),
                ["Initial Position (m)", "Initial Velocity (m/s)", "Acceleration (m/s^2)", "Time (s)"]]
    # Final Velocity
    # values[0] = Initial Velocity
    # values[1] = Acceleration
    # values[2] = Final Position
    # values[2] = Initial Position
    def phyMotion3Equation(self, Initial_Velocity, Acceleration, Final_Position, Initial_Position):
        return values[0]**2 + 2*values[1] * (values[2] - values[3])
    #
    def phyMotion3Print(self):
        return ["Final Velocity (m/s)",
                "v%s = %s(v%s%s + 2a(x%s - x%s))" % (self.subNums[1], self.sqrt, self.subNums[0], self.supNums[2], self.subNums[1], self.subNums[0]),
                ["Initial Velocity (m/s)", "Acceleration (m/s^2)", "Final Position (m)", "Initial Position (m)"]]

    # Astronomy Equations

    # Flux Ration
    # values[0] = Star 1's Magnitude
    # values[1] = Star 2's Magnitude
    def astFlux1Equation(self, values):
        return 2.512**(values[1] - values[0])
    # Flux_Ratio = 2.512^(Magnitude2 - Magnitude1)
    def astFlux1Print(self):
        return ["Flux Ratio",
                "F%s / F%s = 2.512^(m%s - m%s)" % (self.subNums[1], self.subNums[2], self.subNums[2], self.subNums[1]),
                ["Star 1's Magnitue", "Star 2's Magnitue"]]
    # Magnitude Difference
    # values[0] = Flux Ratio (F1 / F2)
    def astFlux2Equation(self, values):
        return 2.5 * math.log(values[0])
    # (Magnitude2 - Magnitude1) = 2.5 log (Flux Ratio)
    def astFlux2Print(self):
        return ["Magnitude Difference",
                "(m%s - m%s) = 2.5 log(F%s / F%s)" % (self.subNums[2], self.subNums[1], self.subNums[1], self.subNums[2]),
                ["Flux Ratio"]]
    # Object Diameter
    # values[0] = Angular Size
    # values[1] = Object Distance
    def astDiameterEquation(self, values):
        return values[0] * values[1] / 206265
    # Object_Diameter = Angular_Size * Object_Distance / 206265
    def astDiameterPrint(self):
        return ["Object's Diameter (km)",
                "D = %sd / 206265" % (self.greek['alpha']),
                ["Angular Size (arc secs)", "Object's Distance (Km)"]]
    # Object Distance
    # values[0] = Angular Size
    # values[1] = Object Diameter
    def astDistanceEquation(self, values):
        return 206265 * values[1] / values[0]
    # Object_Distance = 206265 * Object_Diameter / Angular_Size
    def astDistancePrint(self):
        return ["Object's Distance (km)",
                "d = 206265D / %s" % (self.greek['alpha']),
                ["Angular Size (arc secs)", "Object's Diameter (km)"]]
    # Object Distance
    # values[0] = Paralax
    def astParalaxDistanceEquation(self, values):
        return 1 / values[0]
    # Distance = 1 / Paralax
    def astParalaxDistancePrint(self):
        return ["Object's Distance (km)",
                "d = 1 / p",
                ["Paralax (arc secs)"]]
    # Orbital Period
    # values[0] = Semi-major Axis
    def astKeplersThirdEquation(self, values):
        return math.sqrt(values[0]**3)
    # Period = sqrt(Semi-Major_Axis^3)
    def astKeplersThirdPrint(self):
        return ["Orbital Period (yrs)",
                "p = %s(a%s)" % (self.sqrt, self.supNums[3]),
                ["Semi-Major Axis (AU)"]]




if (__name__ == '__main__'):
    ae = AstronomyEquations()

    pe = ae.getPhyEquations()
    pp = ae.getPhyPrints()
    aeq = ae.getAstEquations()
    ap = ae.getAstPrints()

    print("PHY Equations")
    for e in pe:
        print(e)
    print("PHY Prints")
    for e in pp:
        print(e)
    print("AST Equations")
    for e in aeq:
        print(e)
    print("AST Prints")
    for e in ap:
        print(e)