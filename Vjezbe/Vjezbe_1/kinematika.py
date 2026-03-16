#Napišite svoj modul "kinematika.py" koji će sadržavati funckiju jednoliko_gibanje(). Neka funkcije kao
#ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, masa, ...) i neka crta iste grafove
#kao i u prošlom zadatku. Napravite novi program u kojem ćete uključiti razvijeni modul i pozvati funkciju.

import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(sila, masa, vrijeme):
    a = sila / masa
    
    korak = 0.5
    koraci = int(vrijeme / korak)

    t = np.linspace(0, vrijeme, koraci)

    akc = []
    for i in range(koraci):
        akc.append(a)

    x = []
    v = []
    for i in range(koraci):
        x.append(0)
        v.append(0)

    for i in range(1, koraci):
        v[i] = v[i-1] + a * korak
        x[i] = x[i-1] + v[i-1] * korak

    plt.subplot(3, 1, 1)
    plt.plot(t, x)
    plt.ylabel("Pomak (m)")
    plt.title("x-t graf")

    plt.subplot(3, 1, 2)
    plt.plot(t, v)
    plt.ylabel("Brzina (m/s)")
    plt.title("v-t graf")

    plt.subplot(3, 1, 3)
    plt.plot(t, akc)
    plt.xlabel("Vrijeme (s)")
    plt.ylabel("Ubrzanje (m/s²)")
    plt.title("a-t graf")

    plt.show()