from engineering_notation import EngNumber

# manual:
# https://www.ti.com/lit/an/slva477b/slva477b.pdf

def max_duty_cycle(vin, vout, n):
    # n = eficiência
    return vout / (vin * n)


def inductor(vin, vout, dl, f):
    return (vout * (vin - vout)) / (dl * f * vin)


def capacitor(vout, dl, f):
    return dl / (8 * f * vout)


def inductor_ripple_current(vin, vout, d, f, l):
    return ((vin - vout) * d) / (f * l)


vin = 12
vout = 5
iout = 1
# dl = current ripple
dl = 0.3 * iout
f = 150e3
n = 0.9

l = inductor(vin, vout, iout, f)
print(f"L: {EngNumber(l)}H")

d = max_duty_cycle(vin, vout, n)
l_current_ripple = inductor_ripple_current(vin, vout, d, f, l)
print(f"L Ripple Current: {EngNumber(l_current_ripple)}A")

print(f"C: {EngNumber(capacitor(vout, dl, f))}F")
