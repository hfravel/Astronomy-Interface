import math
from inspect import signature

class AstronomyEquations:
    # This is a class that holds all my equations and
    # all of the methods to print the equations
    def __init__(self):
        # Constants
        self.G = 6.67408 * 10**(-11)
        # Supersciprt and Subscript Numbers 0-9
        #                 0        1        2        3        4        5        6        7        8        9
        self.supNums = ['\u2070','\u00b9','\u00b2','\u00b3','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079']
        self.subNums = ['\u2080','\u2081','\u2082','\u2083','\u2084','\u2085','\u2086','\u2087','\u2088','\u2089']
        self.sqrt = '\u221A'
        self.cbrt = '\u221B'
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
        return [["Velocity", " (m/s):  v ="],
                "v = x / t",
                ["Displacement (m):  x =",
                 "Time (s):  t ="]]
    # Acceleration
    # values[0] = Velocity
    # values[1] = Time
    def phyAccelerationEquation(self, values):
        return values[0] / values[1]
    # Acceleration = Velocity / Time
    def phyAccelerationPrint(self):
        return [["Acceleration", " (m/s^2):  a ="],
                "a = v / t",
                ["Velocity (m/s):  v =", "Time (s):  t ="]]
    # Final Velocity
    # values[0] = Initial Velocity
    # values[1] = Acceleration
    # values[2] = Time
    def phyFinalVelocity1Equation(self, values):
        return values[0] + values[1] * values[2]
    # Final_Velocity = Initial_Velocity + Acceleration * Time
    def phyFinalVelocity1Print(self):
        return [["Final Velocity", " (m/s):  v%s ="%(self.subNums[1])],
                "v%s = v%s + at" % (self.subNums[1], self.subNums[0]),
                ["Initial Velocity (m/s):  v%s ="%(self.subNums[0]),
                 "Acceleration (m/s^2):  a =",
                 "Time (s):  t ="]]    # Final Velocity
    # values[0] = Initial Velocity
    # values[1] = Acceleration
    # values[2] = Initial Position
    # values[3] = Final Position
    def phyFinalVelocity2Equation(self, values):
        return (values[0]**2 + 2*values[1] * (values[3] - values[2]))**(1./2.)
    #
    def phyFinalVelocity2Print(self):
        return [["Final Velocity", " (m/s):  v%s = "%(self.subNums[1])],
                "v%s = %s(v%s%s + 2a(x%s - x%s))" % (self.subNums[1], self.sqrt, self.subNums[0], self.supNums[2], self.subNums[1], self.subNums[0]),
                ["Initial Velocity (m/s):  v%s = "%(self.subNums[0]),
                 "Acceleration (m/s^2):  a =",
                 "Initial Position (m):  x%s ="%(self.subNums[0]),
                 "Final Position (m):  x%s ="%(self.subNums[1])]]
    # Final Position
    # values[0] = Initial Position
    # values[1] = Initial Velocity
    # values[2] = Time
    # values[3] = Acceleration
    def phyFinalPositionEquation(self, values):
        return values[0] + values[1]*values[2] + 0.5 * values[3] * values[2]**2
    # Final_Pos = Initial_Pos + Initial_Vel * Time + 1/2 * Acceleration * Time^2
    def phyFinalPositionPrint(self):
        return [["Final Position", " (m):  x%s ="%(self.subNums[1])],
                "x%s = x%s + v%st + 0.5at%s" % (self.subNums[1], self.subNums[0], self.subNums[0], self.supNums[2]),
                ["Initial Position (m):  x%s ="%(self.subNums[0]),
                 "Initial Velocity (m/s):  v%s ="%(self.subNums[0]),
                 "Time (s):  t =",
                 "Acceleration (m/s^2):  a ="]]

    # Astronomy Equations

    # Flux Ration
    # values[0] = Star 1's Magnitude
    # values[1] = Star 2's Magnitude
    def astFluxRatioEquation(self, values):
        return 2.512**(values[1] - values[0])
    # Flux_Ratio = 2.512^(Magnitude2 - Magnitude1)
    def astFluxRatioPrint(self):
        return [["Flux Ratio", ":  (F%s / F%s) ="%(self.subNums[1], self.subNums[2])],
                "F%s / F%s = 2.512^(m%s - m%s)" % (self.subNums[1], self.subNums[2], self.subNums[2], self.subNums[1]),
                ["Star 1's Magnitue:  m%s ="%(self.subNums[1]),
                 "Star 2's Magnitue:  m%s ="%(self.subNums[2])]]
    # Magnitude Difference
    # values[0] = Flux Ratio (F1 / F2)
    def astMagDiffEquation(self, values):
        return 2.5 * math.log(values[0])
    # (Magnitude2 - Magnitude1) = 2.5 log (Flux Ratio)
    def astMagDiffPrint(self):
        return [["Magnitude Difference", ":  (m%s - m%s) ="%(self.subNums[2], self.subNums[1])],
                "(m%s - m%s) = 2.5 log(F%s / F%s)" % (self.subNums[2], self.subNums[1], self.subNums[1], self.subNums[2]),
                ["Flux Ratio:  (F%s / F%s) ="%(self.subNums[1], self.subNums[2])]]
    # Object Diameter
    # values[0] = Angular Size
    # values[1] = Object Distance
    def astObjectDiameterEquation(self, values):
        return values[0] * values[1] / 206265
    # Object_Diameter = Angular_Size * Object_Distance / 206265
    def astObjectDiameterPrint(self):
        return [["Object's Diameter", " (km):  D ="],
                "D = %sd / 206265" % (self.greek['alpha']),
                ["Angular Size (arc secs):  %s ="%(self.greek['alpha']),
                 "Object's Distance (Km):  d ="]]
    # Object Distance
    # values[0] = Angular Size
    # values[1] = Object Diameter
    def astObjectDistanceEquation(self, values):
        return 206265 * values[1] / values[0]
    # Object_Distance = 206265 * Object_Diameter / Angular_Size
    def astObjectDistancePrint(self):
        return [["Object's Distance", " (km): d ="],
                "d = 206265D / %s" % (self.greek['alpha']),
                ["Angular Size (arc secs):  %s ="%(self.greek['alpha']),
                 "Object's Diameter (km):  D ="]]
    # Object Distance
    # values[0] = Paralax
    def astObjectDistance2Equation(self, values):
        return 1 / values[0]
    # Distance = 1 / Paralax
    def astObjectDistance2Print(self):
        return [["Object's Distance", " (km):  d ="],
                "d = 1 / p",
                ["Paralax (arc secs):  p ="]]
    # Orbital Period -- Kepler's Third Law
    # values[0] = Semi-major Axis
    def astOrbitalPeriodEquation(self, values):
        return math.sqrt(values[0]**3)
    # Period = sqrt(Semi-Major_Axis^3)
    def astOrbitalPeriodPrint(self):
        return [["Orbital Period", " (yrs):  p ="],
                "p = %s(a%s)" % (self.sqrt, self.supNums[3]),
                ["Semi-Major Axis (AU):  a ="]]
    # Semi-major Axis -- Kepler's Third Law
    # values[0] = Orbital Period
    def astSemiMajorAxisEquation(self, values):
        return (values[0]**2)**(1./3.)
    # Period = sqrt(Semi-Major_Axis^3)
    def astSemiMajorAxisPrint(self):
        return [["Semi-Major Axis", " (AU):  a ="],
                "a = %s(p%s)" % (self.cbrt, self.supNums[2]),
                ["Orbital Period (yrs):  p ="]]
    # Escape Velocity
    # values[0] = Mass of planet/star
    # values[1] = Radius of planet/star
    def astEscapeVelocityEquation(self, values):
        return ((2 * self.G * values[0]) / values[1])**(1./2.)
    # Escape_Velocity = sqrt( (2*Gravitational_Constant * Mass) / Radius)
    def astEscapeVelocityPrint(self):
        return [["Escape Velocity", " (m/s): v ="],
                "v = %s( (2GM) / r )"%(self.sqrt),
                ["Planet/Star Mass (kg):  M =",
                 "Planet/Star Radius (m):  r ="]]




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