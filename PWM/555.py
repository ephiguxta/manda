from engineering_notation import EngNumber

def th(ra, rb, ca):
    return (0.693 * (ra + rb) * ca)

def tl(rb, ca):
    return (0.693 * rb * ca)

def freq(ra, rb, ca):
    return (1.44 / ((ra + 2 * rb) * ca))

ra = 3.5e3      # 3.5k
rb = 10e3       # 10k
ca = 471e-12    # 471p

print(f"Th: {EngNumber(th(ra, rb, ca))}")
print(f"Tl: {EngNumber(tl(rb, ca))}")
print(f"f: {EngNumber(freq(ra, rb, ca))}")
