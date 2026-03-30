#Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t
#i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte
#numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima

import numpy as np
import matplotlib.pyplot as plt

F = float(input("sila (N): "))
m = float(input("masa (kg): "))

a = F / m

korak = 1
koraci = int(10 / korak)

t = np.linspace(0, 10, koraci)

akc = []
for i in range(koraci):
    akc.append(a)

x = []
v = []
for i in range(koraci):
    x.append(0)
    v.append(0)

for i in range(1, koraci):
    v[i] = v[i-1] + a * korak     #Eulerova metoda nnumerickog rjesavanja   
    x[i] = x[i-1] + v[i-1] * korak

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.ylabel("Pomak (m)")
plt.title("x-t graf")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, v)
plt.ylabel("Brzina (m/s)")
plt.title("v-t graf")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, akc)
plt.xlabel("Vrijeme (s)")
plt.ylabel("Ubrzanje (m/s²)")
plt.title("a-t graf")
plt.grid()

plt.show()