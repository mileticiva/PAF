import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def model_perioda(theta, l):
    g = 9.81  # m/s^2
    return 2 * np.pi * np.sqrt(l / (g * np.cos(theta)))

kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
kut_rad = np.radians(kut_deg) 

T_120 = np.array([0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653, 
                  0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373, 1.9100, 2.5460])

T_240 = np.array([1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720, 
                  1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840, 2.4473, 3.1573])

teorijsko_L1 = 0.120  # m (120 mm)
teorijsko_L2 = 0.240  # m (240 mm)

popt_120, pcov_120 = curve_fit(model_perioda, kut_rad, T_120, p0=[teorijsko_L1])
popt_240, pcov_240 = curve_fit(model_perioda, kut_rad, T_240, p0=[teorijsko_L2])

dobiveno_L1 = popt_120[0]
dobiveno_L2 = popt_240[0]

pogreska_L1 = np.sqrt(pcov_120[0, 0])
pogreska_L2 = np.sqrt(pcov_240[0, 0])

rel_pogreska_120 = abs(dobiveno_L1 - teorijsko_L1) / teorijsko_L1
rel_pogreska_240 = abs(dobiveno_L2 - teorijsko_L2) / teorijsko_L2

print(f"Za teorijsku duljinu L = 120 mm:")
print(f"  - Dobivena eksperimentalna duljina l: {dobiveno_L1 * 1000:.2f} ± {pogreska_L1 * 1000:.2f} mm")
print(f"  - Relativna pogreška mjerenja duljine: {rel_pogreska_120 * 100:.2f} %")

print(f"\nZa teorijsku duljinu L = 240 mm:")
print(f"  - Dobivena eksperimentalna duljina l: {dobiveno_L2 * 1000:.2f} ± {pogreska_L2 * 1000:.2f} mm")
print(f"  - Relativna pogreška mjerenja duljine: {rel_pogreska_240 * 100:.2f} %")

kut_kontinuirano = np.linspace(0, 85, 500)
kut_kontinuirano_rad = np.radians(kut_kontinuirano)

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12
plt.figure(figsize=(10, 6))

plt.scatter(kut_deg, T_120, color='blue', label='Mjerni podaci (L = 120 mm)', zorder=3)
plt.plot(kut_kontinuirano, model_perioda(kut_kontinuirano_rad, dobiveno_L1), 
         color='darkblue', linestyle='--', label=f'Fit: $l$ = {dobiveno_L1*1000:.1f} mm')

plt.scatter(kut_deg, T_240, color='red', label='Mjerni podaci (L = 240 mm)', zorder=3)
plt.plot(kut_kontinuirano, model_perioda(kut_kontinuirano_rad, dobiveno_L2), 
         color='darkred', linestyle='-', label=f'Fit: $l$ = {dobiveno_L2*1000:.1f} mm')

plt.title('Ovisnost perioda titranja fizikalnog njihala o kutu otklona $\\theta$')
plt.xlabel('Kut otklona $\\theta$ [°]')
plt.ylabel('Period titranja $T$ [s]')
plt.xlim(-5, 90)
plt.grid(True, which='both', linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()