````markdown
# Refrigeration Cycle Simulator

I built this to model an ideal vapor-compression refrigeration cycle and calculate its COP (Coefficient of Performance), since I wanted to actually understand refrigeration cycles beyond just the textbook equations. It uses CoolProp to pull real refrigerant properties (R134a) instead of relying on hand-calculated approximations, and plots the cycle on a P-h diagram so you can actually see what's happening at each stage.

## What it does

You give it an evaporator and condenser temperature, and it walks through the ideal cycle:

1. Saturated vapor leaves the evaporator
2. Gets compressed (isentropically) to condenser pressure
3. Condenses down to saturated liquid
4. Throttles back down through the expansion valve to the evaporator pressure

From there it calculates the refrigeration effect, compressor work, and COP, and plots everything on a P-h diagram.

## Requirements

- Python 3.8+
- CoolProp
- matplotlib

Install with:

```bash
pip install CoolProp matplotlib
```

## Running it

```bash
git clone https://github.com/arfahhnaeem-cloud/refrigeration-cycle-simulator.git
cd refrigeration-cycle-simulator
python refrigeration.py
```

It'll ask for evaporator and condenser temps in °C, then print out the pressures, enthalpies, entropies at each state, and the COP, and pop up the P-h diagram.

### Example run

```
Enter the evaporator temperature in Celsius: -10
Enter the condenser temperature in Celsius: 45

Evaporator pressure: 200.63 kPa
Condenser pressure: 1160.20 kPa
State 1 enthalpy: 392.71 J/kg
State 2 enthalpy: 435.19 J/kg
State 3 enthalpy: 264.15 J/kg
COP: 3.02
```

(Replace with your own actual output — numbers change depending on the temps you enter.)

## Some notes on the assumptions

This is the *ideal* cycle, so it's simplified compared to a real system:

- No superheat at the evaporator exit
- No subcooling at the condenser exit
- Compression is isentropic (no compressor inefficiency)
- No pressure drops anywhere in the system

Real systems will always have a lower COP than what this spits out, since none of that non-ideal stuff is accounted for. That's actually the next thing I want to add — a "detailed mode" that includes superheat, subcooling, and compressor efficiency to get closer to real-world numbers.

## Why R134a

That's just the refrigerant I started with since it's common and well-documented in CoolProp. Swapping to a different refrigerant (R32, R410A, ammonia, etc.) is just a matter of changing the fluid string in the `PropsSI()` calls.

## About this project

This is one of a few thermal/fluids projects I'm working through to get more comfortable with refrigeration and HVAC systems — built by **arfahhnaeem-cloud**.
````
