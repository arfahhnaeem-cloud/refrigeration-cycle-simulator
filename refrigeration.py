from CoolProp.CoolProp import PropsSI
import matplotlib.pyplot as plt
# User Inputs
evap_celsius = input("Enter the evaporator temperature in Celsius: ")
evap_kelvin = float(evap_celsius) + 273.15
print(f"Evaporator temperature in Kelvin: {evap_kelvin}")
cond_celsius = input("Enter the condenser temperature in Celsius: ")
cond_kelvin = float(cond_celsius) + 273.15
print(f"Condenser temperature in Kelvin: {cond_kelvin}")
# Pressures
P_evap = PropsSI('P', 'T', evap_kelvin, 'Q', 1, 'R134a') 
P_cond = PropsSI('P', 'T', cond_kelvin, 'Q', 0, 'R134a')
P_evap_kPa = P_evap / 1000
P_cond_kPa = P_cond / 1000
print(f"Evaporator pressure: {P_evap_kPa:.2f} kPa")
print(f"Condenser pressure: {P_cond_kPa:.2f} kPa")
# State 1: saturated vapor leaving evaporator
h1 = PropsSI('H', 'T', evap_kelvin, 'Q', 1, 'R134a')
s1 = PropsSI('S', 'T', evap_kelvin, 'Q', 1, 'R134a')
print(f"State 1 enthalpy: {h1:.2f} J/kg")
print(f"State 1 entropy: {s1:.2f} J/kg.K")
# State 2: Compressor outlet
h2 = PropsSI('H', 'P', P_cond, 'S', s1, 'R134a')
s2 = s1
print(f"State 2 enthalpy: {h2:.2f} J/kg")
print(f"State 2 entropy: {s2:.2f} J/kg.K")
# State 3: saturated liquid leaving condenser
h3 = PropsSI('H', 'T', cond_kelvin, 'Q', 0, 'R134a')
print(f"State 3 enthalpy: {h3:.2f} J/kg")
# State 4: after throttling (isenthalpic expansion)
h4 = h3
print(f"State 4 enthalpy: {h4:.2f} J/kg")

# Cycle Performance Calculations

q_L = h1 - h4
print(f"Heat absorbed in the evaporator: {q_L:.2f} J/kg")

w_comp = h2 - h1
print(f"Work done by the compressor: {w_comp:.2f} J/kg")

COP = q_L / w_comp
print(f"Coefficient of Performance (COP): {COP:.2f}")

# P-h diagram

h_values = [h1, h2, h3, h4, h1]
p_values = [P_evap_kPa, P_cond_kPa, P_cond_kPa, P_evap_kPa, P_evap_kPa]

plt.plot(h_values, p_values, marker='o')

plt.xlabel('Enthalpy (J/kg)')
plt.ylabel('Pressure (kPa)')
plt.title('R134a Vapor Compression Cycle')

# Label cycle states
states = ['1', '2', '3', '4']
for h, p, state in zip(h_values[:-1], p_values[:-1], states):
    plt.annotate(state, (h, p), xytext=(5, 5), textcoords="offset points")
plt.grid(True)
plt.savefig('R134a_P-h_Diagram.png', dpi=300, bbox_inches='tight')
plt.show()