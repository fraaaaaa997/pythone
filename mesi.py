#programma che traduce i numeri da 1 a 12 nei corrispondendi mesi

mese = int(input("Inserisci un numero:"))

mesi ="Gennaio  "+"Febbraio "+"Marzo    "+ "Aprile   "+ "Maggio   "+ "Giugno   "+ "Luglio   "+ "Agosto   "+ "Settembre"+ "Ottobre  "+"Novembre "+ "Dicembre "

p = (mese  -1) * 9

print(mesi[p:p+9])
