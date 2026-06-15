import numpy as np
import matplotlib.pyplot as plt
np . random . seed (42)
mase_ciste = np . random . normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]

plt.figure(figsize=(8, 5))
plt.hist(mase_ciste, bins=10, edgecolor = "black", alpha=0.6, label='Podaci')

sredina = np.mean(mase_ciste)
medijan_np = np.median(mase_ciste)

plt.axvline(sredina, color='red', linestyle='dashed', linewidth=2, label='Aritm. sredina')
plt.axvline(medijan_np, color='blue', linestyle='dashed', linewidth=2, label='Medijan')

plt.title("Histogram")
plt.xlabel("Masa zvijezde")
plt.ylabel("Frekvencija")
plt.legend()
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(mase_ciste, bins=3, edgecolor='black', alpha=0.6, color='orange')
plt.title("k = 3")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(mase_ciste, bins=40, edgecolor='black', alpha=0.6, color='red')
plt.title("k = 40")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.show()