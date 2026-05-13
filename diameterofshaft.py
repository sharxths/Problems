import math
print("\n Diameter Analysis \n")
print("-----------------------\n")
P = float(input("Enter the power of shaft in kW : "))
N = float(input("Enter the speed of shaft in RPM : "))
S = float(input("Enter the allowabale shear stress in MPa : "))

T = (9550*P)/N
d = ((16*T)/(math.pi*S))**(1/3)

print(f"Torque of the shaft is {T:.3f} Nm")
print(f"diameter of the shaft is {d:.3f} mm")