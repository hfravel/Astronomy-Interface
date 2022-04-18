files = ["Mercury", "Venus", "Earth", "Mars","Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
supNums = ['\u2070','\u00b9','\u00b2','\u00b3','\xb4','\u2075','\xb6','\u2077','\u2078','\u2079']
#supNums = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
data = {f"Mass (10{supNums[2]}{supNums[4]} kg):": [0.330,4.87,5.97,0.642,1898,568,86.8,102,0.0130],
        f"Diameter (km):": [4879,12104,12756,6792,142984,120536,51118,49528,2376],
        f"Density (kg/m{supNums[3]}):": [5429,5243,5514,3934,1326,687,1270,1638,1850],
        f"Gravity (m/s{supNums[2]}):": [3.7,8.9,9.8,3.7,23.1,9.0,8.7,11.0,0.7],
        f"Escape Velocity (km/s):": [4.3,10.4,11.2,5.0,59.5,35.5,21.3,23.5,1.3],
        f"Rotation Period (hours):": [1407.6,-5832.5,23.9,24.6,9.9,10.7,-17.2,16.1,-153.3],
        f"Length of Day (hours):": [4222.6,2802.0,24.0,24.7,9.9,10.7,17.2,16.1,153.3],
        f"Distance from Sun (10{supNums[6]} km):": [57.9,108.2,149.6,228.0,778.5,1432.0,2867.0,4515.0,5906.4],
        f"Perihelion (10{supNums[6]} km):": [46.0,107.5,147.1,206.7,740.6,1357.6,2732.7,4471.1,4436.8],
        f"Aphelion (10{supNums[6]} km):": [69.8,108.9,152.1,249.3,816.4,1506.5,3001.4,4558.9,7375.9],
        f"Orbital Period (days):": [88.0,224.7,365.2,687.0,4331,10747,30589,59800,90560],
        f"Orbital Velocity (km/s):": [47.4,35.0,29.8,24.1,13.1,9.7,6.8,5.4,4.7],
        f"Orbital Inclination (degrees):": [7.0,3.4,0.0,1.8,1.3,2.5,0.8,1.8,17.2],
        f"Orbital Eccentricity:": [0.206,0.007,0.017,0.094,0.049,0.052,0.047,0.010,0.244],
        f"Obliquity to Orbit (degrees):": [0.034,177.4,23.4,25.2,3.1,26.7,97.8,28.3,122.5],
        f"Mean Temperature (C):": [167,464,15,-65,-110,-140,-195,-200,-225],
        f"Surfaec Pressure (bars):": [0,92,1,0.01,"Unknown","Unknown","Unknown","Unknown",0.00001],
        f"Number of Moons:": [0,0,1,2,79,82,27,14,5],
        f"Ring System:": ["No","No","No","No","Yes","Yes","Yes","Yes","No"],
        f"Global Magnetic Field:": ["Yes","No","Yes","No","Yes","Yes","Yes","Yes","Unknown"]
    }

i = 0
for f in files:
    file = open(f"./texts/{f}Data.txt", "w")
    for d in data:
        s = f"{d}   {data[d][i]}\n"
        file.write(s)
    i+=1