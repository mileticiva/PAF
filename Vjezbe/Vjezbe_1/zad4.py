#Napišite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije točke. Neka ta funkcija na
#ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu funkciju u svom programu.

def jednadzba(A, B):
    k = (B[1]-A[1])/(B[0]-A[0])
    kx1 = -(k * A[0]) + A[1]

    print("y = " + str(k) + "x + " + str(kx1))

uneseni = False
while uneseni == False:
    try:
        x = int(input("x za tocku A: "))
        y = int(input("y za tocku A: "))

        A = (x, y)

        x = int(input("x za tocku B: "))
        y = int(input("y za tocku B: "))

        B = (x, y)

        uneseni = True
    except ValueError:
        print("nije broj")

jednadzba(A, B)