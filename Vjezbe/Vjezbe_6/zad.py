import math

def a(valjak, D_lista, L_lista, m_lista, rho_lit):
    n = len(D_lista)

    sv_D = sum(D_lista) / n
    sv_L = sum(L_lista) / n
    sv_m = sum(m_lista) / n

    sigma_D = math.sqrt(sum((x - sv_D) ** 2 for x in D_lista) / (n * (n - 1)))
    sigma_L = math.sqrt(sum((x - sv_L) ** 2 for x in L_lista) / (n * (n - 1)))
    sigma_m = math.sqrt(sum((x - sv_m) ** 2 for x in m_lista) / (n * (n - 1)))

    sv_r = (sv_D / 10) / 2     #cm
    sigma_r = (sigma_D / 10) / 2

    sv_l = sv_L / 10
    sigma_l = sigma_L / 10

    V = (sv_r ** 2) * math.pi * sv_l
    sigma_V = V * math.sqrt((2 * (sigma_r / sv_r)) ** 2 + ((sigma_l / sv_l) ** 2))

    rho = sv_m / V
    sigma_rho = rho * math.sqrt(((sigma_m / sv_m) ** 2) + ((sigma_V / V) **2))

    relpogreska = (abs(rho - rho_lit) / rho_lit) * 100

    print(f"\nREZULTATI ZA: {valjak}")
    print(f"D = {sv_D:.3f} ± {sigma_D:.3f} mm")
    print(f"L = {sv_L:.3f} ± {sigma_L:.3f} mm")
    print(f"m = {sv_m:.3f} ± {sigma_m:.3f} g")
    print(f"V = {V:.3f} ± {sigma_V:.3f} cm³")
    print(f"Gustoća rho = {rho:.3f} ± {sigma_rho:.3f} g/cm³")
    print(f"Relativna pogreška = {relpogreska:.2f} %")

a(
    valjak="VALJAK 1",
    D_lista=[19.98, 20.18, 20.10, 20.08, 19.74],
    L_lista=[49.80, 49.00, 50.48, 49.80, 49.96],
    m_lista=[138.92, 138.98, 139.20, 138.90, 138.92],
    rho_lit=8.96,
)

a(
    valjak="VALJAK 2",
    D_lista=[19.92, 19.82, 19.96, 19.98, 19.88],
    L_lista=[52.56, 52.50, 52.62, 52.58, 52.54],
    m_lista=[128.65, 128.60, 128.65, 128.35, 128.50],
    rho_lit=7.85,
)

a(
    valjak="VALJAK 3",
    D_lista=[24.96, 24.98, 24.98, 24.92, 24.94],
    L_lista=[55.34, 55.40, 55.30, 55.44, 55.48],
    m_lista=[71.89, 71.90, 71.79, 71.85, 71.70],
    rho_lit=2.70,
)