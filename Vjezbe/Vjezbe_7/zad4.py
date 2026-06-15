import numpy as np
import matplotlib.pyplot as plt
np . random . seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]

def medijan(podaci):
    podacisort = sorted(podaci)
    n = len(podacisort)
    if n % 2 != 0:
        indeks = n // 2
        return podacisort[indeks]
    else:
        indeks1 = (n // 2) - 1
        indeks2 = n // 2
        rez = (podacisort[indeks1] + podacisort[indeks2]) / 2
        return rez

sredina = np.mean(mase)
medijan1 = medijan(mase)
razlika = abs(sredina - medijan1)
print("\n1. S grubim pogreskama:")
print(f"   Aritmetička sredina: {sredina:.3f}")
print(f"   Medijan:             {medijan1:.3f}")
print(f"   Razlika: {razlika:.3f}")

sredinabez = np.mean(mase_ciste)
medijanbez = medijan(mase_ciste)
razlikabez = abs(sredinabez - medijanbez)
print("\n2. Bez grubih pogrešaka:")
print(f"   Aritmetička sredina: {sredinabez:.3f}")
print(f"   Medijan:             {medijanbez:.3f}")
print(f"   Razlika: {razlikabez:.3f}")

promjenasredine = abs(sredina - sredinabez)
promjenamedijana = abs(medijan1 - medijanbez)
print("\n3. Promjene vrijednosti:")
print(f"   Promjena aritmeticke sredine: {promjenasredine:.3f}")
print(f"   Promjena medijana: {promjenamedijana:.3f}")


plt.figure(figsize=(11, 6))
fiksni_stupci = np.linspace(min(mase), max(mase), 50)

plt.hist(mase, bins=fiksni_stupci, edgecolor='black', alpha=0.3, color='gray', label='Sve mase (s pogreškama)')
plt.hist(mase_ciste, bins=fiksni_stupci, edgecolor='darkgreen', alpha=0.5, color='green', label='Čiste mase')

# Crtanje vertikalnih linija
plt.axvline(sredina, color='red', linestyle='-', linewidth=2.5, label='Sredina (sve)')
plt.axvline(medijan1, color='blue', linestyle='-', linewidth=2.5, label='Medijan (sve)')
plt.axvline(sredinabez, color='orange', linestyle='--', linewidth=2.5, label='Sredina (čisto)')
plt.axvline(medijanbez, color='cyan', linestyle='--', linewidth=2.5, label='Medijan (čisto)')

plt.xlim(1.0, 3.0) 

plt.title("Usporedba rezultata")
plt.xlabel("Masa zvijezde (u masama Sunca)")
plt.ylabel("Frekvencija")

plt.legend(loc='upper right', fontsize=10)
plt.grid(axis='y', alpha=0.3)

plt.show()