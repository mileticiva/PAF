#Za česticu početne brzine v0 = 10 m/s
#i kuta otklona θ = 60o nacrtajte graf ovisnosti relativne pogreške
#numeričkog riješenja o vrijednosti vremenskog koraka ∆t.
from particle import Particle
import numpy as np
import matplotlib.pyplot as plt

v0 = 10
kut = 60
x = 0
y = 0

p = Particle(v0, kut, x, y)

err = []
dts = []
dt = 0
while dt <= 1:
    dt += 0.001
    dts.append(dt)
    numericki_domet = p.range(dt)
    analiticki_domet = ((v0 ** 2) * np.sin(2 * np.radians(kut))) / 9.81
    
    odstupanje = abs(analiticki_domet - numericki_domet)
    err.append((odstupanje / analiticki_domet) * 100)

plt.plot(dts, err)
plt.xlabel("dt [s]")
plt.ylabel("err [%]")
plt.title("Absolute relative error for range of projectile")
plt.ylim(-1, max(err) + 10)
plt.grid()
plt.show()