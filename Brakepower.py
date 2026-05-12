import math

print("\n Brake Power Calculator \n")

N = float(input("Enter the speed of engine in rpm : "))
T = float(input("Enter the torque in Nm : "))

BP = (2*math.pi*N*T)/(60000) #in KW.

print(f"{BP:.3f} KW")