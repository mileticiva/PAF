from particle import Particle
import numpy as np

v0 = 10
kut = 45
x = 0
y = 0

p = Particle(v0, kut, x, y)
numericki_domet = p.range()
print(f"Domet je: {numericki_domet}")

analiticki_domet = ((v0 ** 2) * np.sin(2 * np.radians(kut))) / 9.81
odstupanje = abs(analiticki_domet - numericki_domet)
print(f"Analiticki domet: {analiticki_domet}, odstupanje je: {odstupanje}")

p.plot_trajectory()
p.reset()