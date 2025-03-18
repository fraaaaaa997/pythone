giorno = int(input("Inserisci un numero:"))

giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]

print(giorni[giorno - 1])

#########################################################################################

giorno = int(input("Inserisci un numero:"))

giorni ="Lunedì   "+"Martedì  "+"Mercoledì"+"Giovedì  "+"Venerdì  "+"Sabato   "+"Domenica "

p = (giorno -1) * 9

print(giorni[p:p+9])
