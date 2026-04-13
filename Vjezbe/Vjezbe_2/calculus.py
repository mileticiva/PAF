def derivacija(f, x, h, two_point=False):
    if two_point:
        return (f(x + h) - f(x)) / h
    return (f(x + h) - f(x - h)) / (2 * h)

def druga(funkc, donja, gornja, korak, two_point=False):
    tocke = []
    derivacije = []

    i = donja
    while i <= gornja:
        tocke.append(i)
        derivacije.append(derivacija(funkc, i, korak, two_point))
        i += korak

    return tocke, derivacije

def pravokutna_aproks(f, a, b, n):
    gornja = 0
    dx = (b - a) / n
    i = 1
    while i <= n:
        x = a + (i * dx)
        gornja += f(x) * dx
        i += 1

    donja = 0
    i = 0
    while i <= n - 1:
        x = a + (i * dx)
        donja += f(x) * dx
        i += 1

    return donja, gornja

def trapezna(f, a, b, n):
    vrijednost = 0
    dx = (b - a) / n
    
    for k in range(1, n + 1):
        x_k = a + (k * dx)
        x_k_1 = a + ((k - 1) * dx)
        vrijednost += f(x_k_1) + f(x_k)

    return (dx / 2) * vrijednost