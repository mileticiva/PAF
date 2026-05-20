import arithm

brojevi = []
    
for i in range(10):
    b = float(input(f"Unesite točku {i+1}:"))
    brojevi.append(b)

arithm.aritm(brojevi)
arithm.aritm2(brojevi)
