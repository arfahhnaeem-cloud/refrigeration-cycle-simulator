from CoolProp.CoolProp import PropsSI
import matplotlib.pyplot as plt
#user inputs
evap_celsius = input("Enter the evaporator temperature in Celsius: ")
evap_kelvin = float(evap_celsius) + 273.15
print(f"Evaporator temperature in Kelvin: {evap_kelvin}")
cond_celsius = input("Enter the condenser temperature in Celsius: ")
cond_kelvin = float(cond_celsius) + 273.15
print(f"Condenser temperature in Kelvin: {cond_kelvin}")
#pressures
P_evap = PropsSI('P', 'T', evap_kelvin, 'Q', 1, 'R134a')
P_cond = PropsSI('P', 'T', cond_kelvin, 'Q', 0, 'R134a')
print(f"Evaporator pressure: {P_evap:.2f} kPa")
print(f"Condenser pressure: {P_cond:.2f} kPa")
#state 1: saturated vapor 
h1 = PropsSI('H', 'T', evap_kelvin, 'Q', 1, 'R134a')
s1 = PropsSI('S', 'T', evap_kelvin, 'Q', 1, 'R134a')
print(f"State 1 enthaly: {h1:.2f} J/kg")
print(f"State 1 entropy: {s1:.2f} J/kg.K")
#state 2: superheated vapor
h2 = PropsSI('H', 'P', P_cond, 'S', s1, 'R134a')
s2 = s1
print(f"State 2 enthaly: {h2:.2f} J/kg")
print(f"State 2 entropy: {s2:.2f} J/kg.K")
#state 3: saturated liquid 
h3 = PropsSI('H', 'T', cond_kelvin, 'Q', 0, 'R134a')
print(f"State 3 enthaly: {h3:.2f} J/kg")
#state 4: subcooled liquid
h4 = h3
print(f"State 4 enthaly: {h4:.2f} J/kg")
Q_in = h1 - h4
print(f"Heat absorbed in the evaporator: {Q_in:.2f} J/kg")
W_comp = h2 - h1
print(f"Work done by the compressor: {W_comp:.2f} J/kg")
COP = Q_in / W_comp
print(f"Coefficient of Performance (COP): {COP:.2f}")
# P-h diagram
h_values = [h1, h2, h3, h4, h1]
p_values = [P_evap, P_cond, P_cond, P_evap, P_evap]
plt.plot(h_values, p_values, marker='o')
plt.xlabel('Enthalpy (J/kg)')
plt.ylabel('Pressure (kPa)')
plt.title('R134a P-h Diagram')
plt.grid(True)
plt.savefig('R134a_P-h_Diagram.png', dpi=300)
plt.show()