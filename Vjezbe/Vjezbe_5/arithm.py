#(a) Napišite program arithm.py koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. Formula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2.
#(b) Napišite program pod (a) koristeći gotove module.
import numpy as np

def aritm(brojevi):
    
    asredina = sum(brojevi) / len(brojevi)

    suma = 0
    for broj in brojevi:
        suma += (broj - asredina) ** 2

    sdevijacija = (suma / (len(brojevi) * (len(brojevi)-1))) ** 0.5

    print("aritmeticka sredina:", asredina)
    print("standardna devijacija:", sdevijacija)

def aritm2(brojevi):
    asredina2 = np.mean(brojevi)
    sdevijacija2 = (np.std(brojevi, ddof=1)) / (len(brojevi)) ** 0.5

    print("aritmeticka sredina 2:", asredina2)
    print("standardna devijacija 2:", sdevijacija2)