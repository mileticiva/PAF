#Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5.
#Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili.

def a(N):
    x = 5
    for i in range(N):
        x = x + 1/3
    for i in range(N):
        x = x - 1/3
    return x

print(a(200), a(2000), a(20000))


#opet rezultat nije onakav kakav smo ocekivali jer broj 1/3 u binarnom sustavu ne moze se zapisati tocno