import matplotlib.pyplot as plt
from kosi_hitac import Projectile

p = Projectile(100, 45, 0, 0, 1.22521, 0.2, 1, 10)
x1, y1 = p.kosi_hitac(dt=0.1)
p.reset()
x2, y2 = p.kosi_hitac(dt=0.01)
p.reset()
x3, y3 = p.kosi_hitac(dt=0.001)
p.reset()
x4, y4 = p.kosi_hitac(dt=0.01, euler=False)
p.reset()

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.grid()
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("x - y graf")
plt.ylim(min(x4) - 10, max(y4) + 10)
plt.show()