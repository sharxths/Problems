import math 
print("\n  Torsion Analysis \n ")

T = float(input("Enter the Torque in Nm: "))
d = float(input("Enter the Shaftdiameter in mm: "))

Shearstress = (16*T)/(math.pi*d**3)

print(f"Shearstress of a solidshaft is: {Shearstress:.2f}MPa")