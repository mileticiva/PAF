import calculus
import matplotlib.pyplot as plt
import sympy

def f1(x):
    return 2 * (x ** 2) + 3

a = 0
b = 1

x = sympy.symbols("x")
analiticka = sympy.integrate(2 * x ** 2 + 3, (x, a, b))

tocke = []
gornje = []
donje = []
trapezne = []
for n in range(50, 1000, 50):
    tocke.append(n)
    pravokutna = calculus.pravokutna_aproks(f1, a, b, n)
    gornje.append(pravokutna[1])
    donje.append(pravokutna[0])
    trapezne.append(calculus.trapezna(f1, a, b, n))

plt.plot(tocke, trapezne, ls='', marker='.')
plt.plot(tocke, gornje, ls='', marker='.')
plt.plot(tocke, donje, ls='', marker='.')
plt.plot(tocke, [analiticka for _ in range(len(tocke))])
plt.xlabel("N")
plt.ylabel("Integral")
plt.title("")
plt.show()