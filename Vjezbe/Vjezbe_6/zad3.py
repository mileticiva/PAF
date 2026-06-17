import math
import numpy as np

def svrijednost(lista):
    return sum(lista) / len(lista)

def izracunaj_sigma(lista, sv):
    n = len(lista)
    if n <= 1:
        return 0
    return math.sqrt(sum((x - sv) ** 2 for x in lista) / (n * (n - 1)))

def volumen_valjka(R, L):
    return (R ** 2) * math.pi * L

def sigma_volumena(R, sigma_R, L, sigma_L):
    dV_dR = 2 * math.pi * R * L
    dV_dL = math.pi * (R ** 2)
    return math.sqrt((dV_dR * sigma_R) ** 2 + (dV_dL * sigma_L) ** 2)

def gustoca(m, V):
    return m / V
def sigma_gustoce(m, sigma_m, V, sigma_V):
    drho_dm = 1 / V
    drho_dV = -m / (V ** 2)
    return math.sqrt((drho_dm * sigma_m) ** 2 + (drho_dV * sigma_V) ** 2)

def pokreni(ime, D_lista, L_lista, m_lista):
    sv_D = svrijednost(D_lista)
    sigma_D = izracunaj_sigma(D_lista, sv_D)

    sv_L = svrijednost(L_lista)
    sigma_L = izracunaj_sigma(L_lista, sv_L)

    sv_m = svrijednost(m_lista)
    sigma_m = izracunaj_sigma(m_lista, sv_m)

    sv_R = (sv_D / 10) / 2
    sigma_R = (sigma_D / 10) / 2
    
    sv_l = sv_L / 10
    sigma_l = sigma_L / 10

    V = volumen_valjka(sv_R, sv_l)
    sigma_V = sigma_volumena(sv_R, sigma_R, sv_l, sigma_l)

    rho = gustoca(sv_m, V)
    sigma_rho = sigma_gustoce(sv_m, sigma_m, V, sigma_V)

    print(f"Rezultati za {ime}:")
    print(f"  Gustoća rho = {rho:.4e} ± {sigma_rho:.4e} g/cm³\n")

D1 = [19.98, 20.18, 20.10, 20.08, 19.74]
L1 = [49.80, 49.00, 50.48, 49.80, 49.96]
m1 = [138.92, 138.98, 139.20, 138.90, 138.92]
pokreni("VALJAK 1", D1, L1, m1)

D2 = [19.92, 19.82, 19.96, 19.98, 19.88]
L2 = [52.56, 52.50, 52.62, 52.58, 52.54]
m2 = [128.65, 128.60, 128.65, 128.35, 128.50]
pokreni("VALJAK 2", D2, L2, m2)

D3 = [24.96, 24.98, 24.98, 24.92, 24.94]
L3 = [55.34, 55.40, 55.30, 55.44, 55.48]
m3 = [71.89, 71.90, 71.79, 71.85, 71.70]
pokreni("VALJAK 3", D3, L3, m3)