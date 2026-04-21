import numpy as np
import matplotlib.pyplot as plt

x0 = 0
y0 = 0
z0 = 0

pq = 1
pm = 1

eq = -1
em = 1

E = [0, 0, 0]
B = [0, 0, 1]
v = [0.1, 0.1, 0.1]

vrijeme = 20
dt = 0.001

p_x = [x0]
p_y = [y0]
p_z = [z0]

e_x = [x0]
e_y = [y0]
e_z = [z0]

p_vx = [v[0]]
p_vy = [v[1]]
p_vz = [v[2]]

e_vx = [v[0]]
e_vy = [v[1]]
e_vz = [v[2]]

trenutno_vrijeme = 0
while trenutno_vrijeme <= vrijeme:
    Ex = E[0]
    Ey = E[1]
    Ez = E[2]

    Bx = B[0]
    By = B[1]
    Bz = B[2]

    p_ax = (pq / pm) * (Ex + (p_vy[-1] * Bz - p_vz[-1] * By))
    p_ay = (pq / pm) * (Ey + (p_vz[-1] * Bx - p_vx[-1] * Bz))
    p_az = (pq / pm) * (Ez + (p_vx[-1] * By - p_vy[-1] * Bx))

    e_ax = (eq / em) * (Ex + (e_vy[-1] * Bz - e_vz[-1] * By))
    e_ay = (eq / em) * (Ey + (e_vz[-1] * Bx - e_vx[-1] * Bz))
    e_az = (eq / em) * (Ez + (e_vx[-1] * By - e_vy[-1] * Bx))

    p_vx.append(p_vx[-1] + p_ax * dt)
    p_vy.append(p_vy[-1] + p_ay * dt)
    p_vz.append(p_vz[-1] + p_az * dt)

    e_vx.append(e_vx[-1] + e_ax * dt)
    e_vy.append(e_vy[-1] + e_ay * dt)
    e_vz.append(e_vz[-1] + e_az * dt)

    p_x.append(p_x[-1] + p_vx[-1] * dt)
    p_y.append(p_y[-1] + p_vy[-1] * dt)
    p_z.append(p_z[-1] + p_vz[-1] * dt)

    e_x.append(e_x[-1] + e_vx[-1] * dt)
    e_y.append(e_y[-1] + e_vy[-1] * dt)
    e_z.append(e_z[-1] + e_vz[-1] * dt)

    trenutno_vrijeme += dt

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(p_x, p_y, p_z, 'r')
ax.plot(e_x, e_y, e_z, 'b')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.view_init(elev=15, azim=45)

plt.show()