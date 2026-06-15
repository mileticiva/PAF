import matplotlib.pyplot as plt
import numpy as np
np . random . seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]

def histogram(podaci, k):
    xmin = min(podaci)
    xmax = max(podaci)
    h = (xmax - xmin) / k
    rubovi = []
    for i in range(k + 1):
        rubovi.append(xmin + i * h)
    frekvencije = [0] * k
    for p in podaci:
        for i in range(k):
            if i == k - 1:
                if rubovi[i] <= p <= rubovi[i+1]:
                    frekvencije[i] += 1
                    break
            else:
                if rubovi[i] <= p < rubovi[i+1]:
                    frekvencije[i] += 1
                    break
    for i in range(k):
        print(f"[{rubovi[i]:.2f}, {rubovi[i+1]:.2f}): {frekvencije[i]}")
    return rubovi, frekvencije

rubovi, frekvencije = histogram(mase_ciste, 10)
sirina_stupca = (max(mase_ciste) - min(mase_ciste)) / 10
sredine_razreda = []
for i in range(len(rubovi) - 1):
    sredine_razreda.append((rubovi[i] + rubovi[i+1]) / 2)

plt.figure(figsize=(8, 5))
plt.bar(sredine_razreda, frekvencije, width=sirina_stupca, edgecolor='black', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.show()