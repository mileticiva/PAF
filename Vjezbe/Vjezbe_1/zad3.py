#Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. Nakon što je korisnik uspješno upisao dvije koordinate
#ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.

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

k = (B[1]-A[1])/(B[0]-A[0])    
l = -(k * A[0]) + A[1]

print("y = " + str(k) + "x + " + str(l))