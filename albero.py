ampiezza = int(input("inserisci un numero per la base: "))
carattere = input("inserisci un carattere: ")

if ampiezza % 2 == 0:
    ampiezza += 1

for lettera in range(1, ampiezza + 1, 2):
    spazi = (ampiezza - lettera) // 2
    print(" " * spazi + carattere * lettera)

