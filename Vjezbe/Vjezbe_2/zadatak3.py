import calculus
import math
import sympy
import matplotlib.pyplot as plt


def kubna(x):
    return (5 * (x ** 3)) - (2 * (x ** 2)) + (2 * x) - 3


def trigonometrijska(x):
    return math.sin(x)


donja = -5
gornja =5
korak = 0.1

x = sympy.Symbol("x")

tocke, numericki = calculus.druga(kubna, donja, gornja, korak)

f = kubna(x)
analiticka = sympy.diff(f, x)

analiticke = []
for t in tocke:
    analiticke.append(float(analiticka.subs(x, t)))

plt.figure()

plt.plot(tocke, analiticke, label="analiticka derivacija")
plt.plot(tocke, numericki, ls='', marker='.', label="numericka derivacija")

plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("Derivacija kubne funkcije")
plt.legend()

plt.show()



tocke2, numericki2 = calculus.druga(trigonometrijska, donja, gornja, korak)

analiticke2 = []
for t in tocke2:
    analiticke2.append(math.cos(t))

plt.figure()

plt.plot(tocke2, analiticke2, label="cos(x) analiticki")
plt.plot(tocke2, numericki2, ls='', marker='.', label="numericki")

plt.ylim(-1.5, 1.5)
plt.legend()
plt.title("Derivacija sin(x)")
plt.show()