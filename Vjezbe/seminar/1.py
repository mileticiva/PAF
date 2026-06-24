import numpy as np
import matplotlib.pyplot as plt

class SimulacijaCestice:
    def __init__(self, tip_polja="promjenjivo"):
        self.x0 = 0
        self.y0 = 0
        self.z0 = 0

        self.eq = -7.0
        self.em = 1.0

        self.E = [0, 0, 0]
        self.v = [0.2, 0.2, 0.2]      

        self.vrijeme = 10         
        self.dt = 0.001          

        self.e_x = [self.x0]
        self.e_y = [self.y0]
        self.e_z = [self.z0]

        self.e_vx = [self.v[0]]
        self.e_vy = [self.v[1]]
        self.e_vz = [self.v[2]]
        
        self.tip_polja = tip_polja 

    def pokreni(self):
        x, y, z = self.x0, self.y0, self.z0
        vx, vy, vz = self.v[0], self.v[1], self.v[2]
        trenutno_vrijeme = 0
        while trenutno_vrijeme <= self.vrijeme:
            Ex, Ey, Ez = self.E[0], self.E[1], self.E[2]
            Bx = 0
            By = 0
            if self.tip_polja == "promjenjivo":
                Bz = 0.1 * trenutno_vrijeme
            else:
                Bz = 1.0 
            e_ax = (self.eq / self.em) * (Ex + (vy * Bz - vz * By))
            e_ay = (self.eq / self.em) * (Ey + (vz * Bx - vx * Bz))
            e_az = (self.eq / self.em) * (Ez + (vx * By - vy * Bx))
            vx += e_ax * self.dt
            vy += e_ay * self.dt
            vz += e_az * self.dt
            x += vx * self.dt
            y += vy * self.dt
            z += vz * self.dt
            self.e_vx.append(vx)
            self.e_vy.append(vy)
            self.e_z.append(z)
            self.e_x.append(x)
            self.e_y.append(y)
            trenutno_vrijeme += self.dt

    def nacrtaj_graf(self):
        plt.style.use('default')
        fig = plt.figure(figsize=(10, 8))  
        ax = fig.add_subplot(projection='3d')
        if self.tip_polja == "promjenjivo":
            boja = 'b'
            naslov = 'Elektron - Vremenski promjenjivo polje'
            ime_datoteke = 'epromjenjivo.png'
        else:
            boja = 'r'
            naslov = 'Elektron - Konstantno polje'
            ime_datoteke = 'ekonstantno.png'
        ax.plot(self.e_x[::5], self.e_y[::5], self.e_z[::5], boja, label=naslov)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.legend(loc='upper right', bbox_to_anchor=(0.85, 0.85))
        maks_skala = max(max(abs(np.array(self.e_x))), max(abs(np.array(self.e_y)))) * 1.1
        ax.set_xlim([-maks_skala, maks_skala])
        ax.set_ylim([-maks_skala, maks_skala])
        ax.set_zlim([0, max(self.e_z)])
        ax.view_init(elev=20, azim=45)
        plt.savefig(ime_datoteke, dpi=300, bbox_inches='tight')
        plt.show()

sim_promjenjivo = SimulacijaCestice(tip_polja="promjenjivo")
sim_promjenjivo.pokreni()
sim_promjenjivo.nacrtaj_graf()  

sim_konstantno = SimulacijaCestice(tip_polja="konstantno")
sim_konstantno.pokreni()
sim_konstantno.nacrtaj_graf()  