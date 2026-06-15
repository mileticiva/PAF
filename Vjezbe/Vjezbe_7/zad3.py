import numpy as np
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
    
a = [3, 1, 4, 1, 5, 9, 2, 6]      
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"medijan za a: {medijan(a)}")
print(f"medijan za b: {medijan(b)}")

rucno = medijan(mase)
np = np.median(mase)
print(f"medijan rucno: {rucno}")
print(f"medijan sa numpy: {np}")