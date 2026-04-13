import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, pocetna_brzina, kut, pocetni_x, pocetni_y):
        self.pocetna_brzina = pocetna_brzina
        self.kut = np.radians(kut)
        self.pocetni_x = pocetni_x
        self.pocetni_y = pocetni_y

        self.trenutni_x = self.pocetni_x
        self.trenutni_y = self.pocetni_y

        self.vx = self.pocetna_brzina * np.cos(self.kut)
        self.vy = self.pocetna_brzina * np.sin(self.kut)
    
    def vrati(self):
        self.trenutni_x = self.pocetni_x
        self.trenutni_y = self.pocetni_y

        self.vx = self.pocetna_brzina * np.cos(self.kut)
        self.vy = self.pocetna_brzina * np.sin(self.kut)

    def reset(self):
        self.pocetna_brzina = 0
        self.kut = np.radians(0)
        self.pocetni_x = 0
        self.pocetni_y = 0
        self.trenutni_x = 0
        self.trenutni_y = 0
        self.vx = 0
        self.vy = 0

    def __move(self, dt):
        g = 9.81

        self.trenutni_x += self.vx * dt
        self.trenutni_y += self.vy * dt

        self.vx = self.vx
        self.vy = self.vy - g * dt

    def range(self, dt=0.0001):
        self.__move(dt)
        while self.trenutni_y > 0:
            self.__move(dt)
        domet = self.trenutni_x - self.pocetni_x
        self.vrati()
        return domet

    def plot_trajectory(self):
        x = [self.trenutni_x]
        y = [self.trenutni_y]
        dt = 0.0001

        self.__move(dt)
        x.append(self.trenutni_x)
        y.append(self.trenutni_y)
        while self.trenutni_y > 0:
            self.__move(dt)
            x.append(self.trenutni_x)
            y.append(self.trenutni_y)

        self.vrati()

        plt.plot(x, y)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.title("x - y graf")
        plt.grid()
        plt.ylim(min(y) - 10, max(y) + 10)
        plt.show()