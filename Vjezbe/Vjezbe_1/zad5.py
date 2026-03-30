#Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot tako da nacrtate unesene koordinate i pravac koji prolazi kroz njih. Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi
#kao PDF. Dopustite korisniku da bira ime pod kojim će se spremiti graf.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def jednadzba(A, B):
    plt.scatter([A[0], B[0]], [A[1], B[1]])

    k = (B[1]-A[1])/(B[0]-A[0])
    l = -(k * A[0]) + A[1]

    print("y = " + str(k) + "x + " + str(l))

    manja = min(A[0], B[0])
    visa = max(A[0], B[0])
    x = np.linspace(manja, visa, 100)
    y = k * x + l
    plt.plot(x, y)

    spremi = input("'prikazi' ili 'spremi': ")
    if spremi == "spremi":
        ime = input("ime fajla: ")
        plt.savefig(ime + ".pdf")
    else:
        plt.grid()
        plt.show()

uneseni = False
while uneseni == False:
    try:
        x = int(input("x za tocku A: "))
        y = int(input("y za tocku A: "))

        A = (x, y)

        x = int(input("x za tocku B: "))
        y = int(input("y za tocku B: "))

        B = (x, y)

        uneseni = True
    except ValueError:
        print("nije broj")

jednadzba(A, B)
