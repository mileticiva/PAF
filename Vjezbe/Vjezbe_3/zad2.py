import matplotlib.pyplot as plt
from kosi_hitac import Projectile

p = Projectile(100, 45, 0, 0, 1.22521, 0.2, 1, 10)
euler_x, euler_y = p.kosi_hitac(dt=0.01, euler=True)
p.reset()
runge_x, runge_y = p.kosi_hitac(dt=0.01, euler=False)
p.reset()

plt.plot(euler_x, euler_y, color = "red")
plt.plot(runge_x, runge_y, color = "blue")
plt.grid()
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("x - y graf")
plt.ylim(min(runge_x) - 10, max(runge_y) + 10)
plt.show()