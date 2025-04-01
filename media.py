#acquisire tramite input una sequenza di numeri fino a che l'utente non scrive exit e calcolare la loro media

""" valori = []
valori = input("inserisci i numeri separati da uno spazio: ")
valori = [int(i) for i in valori]  
media = sum(valori) / len(valori)
print("La media è:", media)
 """


somma = 0
numeri_letti = 0
valore_stringa = input("inserisci un numero (o 'exit' per terminare): ")
while valore_stringa != "exit":
    numeri_letti += 1
    somma += int(valore_stringa)
    valore_stringa = input("inserisci un numero (o 'exit' per terminare): ")

print ("La somma è:", somma)
print ("La media è:", somma / numeri_letti)
