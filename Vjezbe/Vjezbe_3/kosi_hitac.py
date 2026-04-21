import numpy as np

class Projectile:
    def __init__(self, v0, kut, x0, y0, p, Cd, A, m):
        self.v0 = v0
        self.kut = np.radians(kut)
        self.x0 = x0
        self.y0 = y0
        self.p = p
        self.Cd = Cd
        self.A = A
        self.m = m

        self.ax = 0
        self.ay = 0

        self.vx = self.v0 * np.cos(self.kut)
        self.vy = self.v0 * np.sin(self.kut)
        self.x = self.x0
        self.y = self.y0

    def reset(self):
        self.ax = 0
        self.ay = 0

        self.vx = self.v0 * np.cos(self.kut)
        self.vy = self.v0 * np.sin(self.kut)
        self.x = self.x0
        self.y = self.y0

    def __move(self, dt, euler):
        g = 9.81

        r = ((self.p * self.Cd * self.A) / (2 * self.m))
        
        if euler:
            self.ax = -np.sign(self.vx) * r * (self.vx ** 2)
            self.vx = self.vx + self.ax * dt
            self.x = self.x + self.vx * dt

            self.ay = -g - np.sign(self.vy) * r * (self.vy ** 2)
            self.vy = self.vy + self.ay * dt
            self.y = self.y + self.vy * dt
        else:
            vx0 = self.vx
            vy0 = self.vy
            x0 = self.x
            y0 = self.y

            def ax(vx):
                return -np.sign(vx) * r * vx ** 2

            def ay(vy):
                return -g - np.sign(vy) * r * vy ** 2

            k1vx = ax(vx0)
            k1x = vx0
            k2vx = ax(vx0 + 0.5 * dt * k1vx)
            k2x = vx0 + 0.5 * dt * k1vx
            k3vx = ax(vx0 + 0.5 * dt * k2vx)
            k3x = vx0 + 0.5 * dt * k2vx
            k4vx = ax(vx0 + dt * k3vx)
            k4x = vx0 + dt * k3vx

            self.vx = vx0 + (dt / 6) * (k1vx + 2 * k2vx + 2 * k3vx + k4vx)
            self.x = x0  + (dt / 6) * (k1x  + 2 * k2x  + 2 * k3x  + k4x)

            k1vy = ay(vy0)
            k1y = vy0
            k2vy = ay(vy0 + 0.5 * dt * k1vy)
            k2y = vy0 + 0.5 * dt * k1vy
            k3vy = ay(vy0 + 0.5 * dt * k2vy)
            k3y = vy0 + 0.5 * dt * k2vy
            k4vy = ay(vy0 + dt * k3vy)
            k4y = vy0 + dt * k3vy

            self.vy = vy0 + (dt / 6) * (k1vy + 2 * k2vy + 2 * k3vy + k4vy)
            self.y = y0  + (dt / 6) * (k1y  + 2 * k2y  + 2 * k3y  + k4y)
    
    def kosi_hitac(self, dt=0.01, euler=True):
        x = [self.x]
        y = [self.y]
        self.__move(dt, euler)
        while self.y > 0:
            x.append(self.x)
            y.append(self.y)
            self.__move(dt, euler)
        return x, y