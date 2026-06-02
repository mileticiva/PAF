import matplotlib.pyplot as plt
import numpy as np
M =  [0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #Nm
phi =  [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] #rad

suma_Mphi = 0
suma_M2 = 0
suma_phi2 = 0

for i in range(len(M)):
    suma_Mphi += M[i] * phi[i]
    suma_M2 += M[i] **2
    suma_phi2 += phi[i] **2

Dt = suma_Mphi / suma_phi2
korijen = (1 / len(M)) * ((suma_M2 / suma_phi2) - (Dt ** 2))
sigma_Dt = korijen ** 0.5

print(f"modul torzije: Dt = ({Dt:.4f} ± {sigma_Dt:.4f}) Nm/rad")

phi_np = np.array(phi)
M_reg = Dt * phi_np

plt.figure(figsize=(8, 6))
plt.scatter(phi, M, label='Mjerenja')
plt.plot(phi_np, M_reg, label=f'Regresija: M = {Dt:.4f}·φ')
plt.xlabel('Kut zakreta φ (rad)')
plt.ylabel('Moment M (Nm)')
plt.grid(True)
plt.legend()
plt.show()