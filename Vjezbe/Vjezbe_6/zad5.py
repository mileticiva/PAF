import numpy as np

malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000)

def a(lista, naziv):
    n = len(lista)
    sigma_n = np.std(lista, ddof=0)
    s = np.std(lista, ddof=1)
    sigma_x = s / np.sqrt(n)
    rel_pogreska = abs(sigma_n - s) / s * 100

    print(naziv)
    print("Broj mjerenja =", n)
    print(f"sigma_n = {sigma_n:.6f}")
    print(f"s   = {s:.6f}")
    print(f"sigma_x = {sigma_x:.6f}")
    print(f"Relativna pogreška između sigma_n i s = {rel_pogreska:.4f}%")

a(malo_n, "Mali skup")
a(veliko_n, "Veliki skup")