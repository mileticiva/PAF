import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54       #(m)
m = 0.5257      #(kg)
r = 4.025e-3    #(m)
g = 9.81        #(m/s^2)

h_izmjeri = np.array([0.14, 0.17, 0.19, 0.22, 0.25, 0.28, 0.31, 0.34, 0.37, 0.40])
t = np.array([1.740, 1.793, 2.043, 2.190, 2.280, 2.417, 2.540, 2.640, 2.670, 2.813])
h = h_izmjeri[::-1]

s = h0 - h
n = len(t)

x = np.log10(t)
y = np.log10(s)

x_mean = np.mean(x)
y_mean = np.mean(y)
xy_mean = np.mean(x * y)
x2_mean = np.mean(x * x)
y2_mean = np.mean(y * y)

a = (xy_mean - x_mean * y_mean) / (x2_mean - x_mean**2)
b = y_mean - a * x_mean

sigma_a = np.sqrt((1/n) * ((y2_mean - y_mean**2) / (x2_mean - x_mean**2) - a**2))
sigma_b = sigma_a * np.sqrt(x2_mean - x_mean**2)

print("(a)")
print(f"Nagib pravca a = {a:.3f} ± {sigma_a:.3f}")
print(f"Presjek s y-osi b = {b:.3f} ± {sigma_b:.3f}\n")

#b
X_t2 = t**2
Y_s = s

nagib_t2 = np.sum(X_t2 * Y_s) / np.sum(X_t2 * X_t2)

Y_pred = nagib_t2 * X_t2
sigma_y_s = np.sqrt(np.sum((Y_s - Y_pred)**2) / (n - 1))
pogreska_nagib_t2 = sigma_y_s / np.sqrt(np.sum(X_t2 * X_t2))

a_ef = 2 * nagib_t2
pogreska_a_ef = 2 * pogreska_nagib_t2

print("(b)")
print(f"Nagib pravca s(t^2) = {nagib_t2:.4f} ± {pogreska_nagib_t2:.4f}")
print(f"Efektivna akceleracija a_ef = {a_ef:.3f} ± {pogreska_a_ef:.3f} m/s^2\n")

#c
I_z = m * (r**2) * ((g / a_ef) - 1)

derivacija = - (m * g * (r**2)) / (a_ef**2)
pogreska_Iz = np.abs(derivacija) * pogreska_a_ef

print("(c)")
print(f"Moment tromosti I_z = {I_z:.4e} ± {pogreska_Iz:.4e} kg m^2\n")


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

y_fit_log = a * x + b
ax1.scatter(x, y, color="red", label="Mjerni podaci")
ax1.plot(x, y_fit_log, color="blue", label=f"Fit: log s = {a:.2f} log t + {b:.2f}")
ax1.set_xlabel(r"$\log\ t$")
ax1.set_ylabel(r"$\log\ s$")
ax1.set_title("Linearizacija: log(s) vs log(t)")
ax1.grid(True)
ax1.legend()

y_fit_s = nagib_t2 * X_t2
ax2.scatter(X_t2, Y_s, color="green", label="Mjerni podaci")
ax2.plot(X_t2, y_fit_s, color="orange", label=f"Fit: s = {nagib_t2:.4f} * t^2")
ax2.set_xlabel(r"$t^2\ [\mathrm{s^2}]$")
ax2.set_ylabel(r"$s\ [\mathrm{m}]$")
ax2.set_title(r"Graf ovisnosti $s$ o $t^2$")
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()