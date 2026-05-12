import math

print("\n Brake Power and BSFC Calculator \n")

N = float(input("Enter the speed of engine in rpm : "))
T = float(input("Enter the torque in Nm : "))

BP = (2*math.pi*N*T)/(60000) #in KW.

Mf = float(input("Enter mass flow rate of fuel in kg/s : "))
BSFC = Mf/BP 
print(f"Brake power of engine is: {BP:.3f} KW")
print(f"BSFC of engine is: {BSFC:.3f} kg/kWh")
